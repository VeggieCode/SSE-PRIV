import os.path
import textwrap
from datetime import datetime
from io import BytesIO

import pdfrw
from django.conf import settings

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .forms import CustomPasswordResetForm, CustomSetPasswordForm, CustomAuthenticationForm, StudentForm, \
    SignupUserForm, SeleccionCarreraForm, LicenciaturaForm, ContinuacionEstudiosForm, EmpleoDuranteEstudiosForm, \
    EmpleoInmediatoForm, BusquedaEmpleoForm, EmpresaForm, DesempenioRecomendacionesForm
from .models.carrera import Carrera
from .models.continuacion_estudios import ContinuacionEstudios
from .models.empleo import EmpleoDuranteEstudios, BusquedaEmpleo, EmpleoInmediato, Empresa, DesempenioRecomendaciones
from .models.licenciatura import Licenciatura
from .models.seleccion_carrera import SeleccionCarrera
from .models.student import Student
from .models.ubicacion import Estados, Municipios
from admin_module.models import Coordinador

STUDENT_INFO_TEMPLATE = 'student_module/student_info.html'


@login_required
def generate_pdf(request):
    # Obtén el objeto del estudiante
    usuario = request.user
    alumno = Student.objects.filter(matricula=usuario).first()
    full_name = alumno.nombre + ' ' + alumno.apellido_paterno + ' ' + alumno.apellido_materno

    # Abre el archivo PDF existente y crea un objeto PdfReader
    existing_pdf_path = os.path.join(settings.BASE_DIR, 'static', 'assets', 'docs', 'constancia_template.pdf')
    with open(existing_pdf_path, 'rb') as f:
        existing_pdf = pdfrw.PdfReader(f)

    # Crea un objeto PdfWriter para escribir en el archivo PDF nuevo
    output_pdf = pdfrw.PdfWriter()

    # Agrega las páginas del archivo PDF existente al objeto PdfWriter
    for i in range(len(existing_pdf.pages)):
        page = existing_pdf.pages[i]

        # Agrega contenido al PDF en la primera página
        if i == 0:
            canvas_data = BytesIO()
            pdf_canvas = canvas.Canvas(canvas_data, pagesize=letter, bottomup=0)

            def formato_fecha(date):
                fecha = f"{date}".split()[0]  # obtenemos solo la fehca YYYY-MM-DD
                year, month, day = fecha.split("-")  # separamos cada parte
                # creamos un diccionario con todos los mese
                months = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio",
                          8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
                # retornamos el resultado
                return f"{day} de {months[int(month)]} del {year}"

            # Agrega el texto con formato y margen
            pdf_canvas.setFont('Helvetica', 9.5)
            pdf_canvas.setFillColorRGB(0, 0, 0)
            text = (f"\nQue el estudiante {full_name} con matrícula {alumno.matricula}, ha concluido de manera "
                    f"satisfactoria el cuestionario de pre-egreso en la f"
                    f"echa de {formato_fecha(alumno.pre_egreso_fecha_fin)} como requisito de su proceso de titulación.")
            pdf_canvas.setLineWidth(0.5)
            margin = 125  # Establece el tamaño del margen
            y = 290  # Posición vertical de la primera línea
            for line in textwrap.wrap(text, width=100):
                pdf_canvas.drawString(margin, y, line)
                y += 12  # Distancia vertical entre líneas

            second_text = (f"\nSe extiende la presente a petición de la interesada y para los fines legales que a ésta "
                           f"convenga a la fecha de {formato_fecha(datetime.now())}, en la ciudad de Xalapa, "
                           f"Veracruz. ")

            margin_second_text = 125  # Establece el tamaño del margen
            y_second_text = 350  # Posición vertical de la primera línea
            lines = textwrap.wrap(second_text, width=100)
            for line in lines:
                pdf_canvas.drawString(margin_second_text, y_second_text, line)
                y_second_text += 12  # Distancia vertical entre líneas
            pdf_canvas.save()

            overlay_pdf = pdfrw.PdfReader(BytesIO(canvas_data.getvalue())).pages[0]

            # Crea una variable para guardar la página con el contenido añadido
            merged_page = pdfrw.PageMerge(page)
            merged_page.add(overlay_pdf)
            output_page = merged_page.render()

            # Añade la página al objeto PdfWriter
            output_pdf.addpage(output_page)

        else:
            output_pdf.addpage(page)

    # Guarda el archivo PDF nuevo en un archivo en el sistema de archivos
    with open(os.path.join(settings.BASE_DIR, 'static', 'assets', 'docs', 'constancia_template_f.pdf'), 'wb') as f:
        output_pdf.write(f)

    # Crea la respuesta HTTP con encabezado PDF para descargar el archivo nuevo
    response = HttpResponse(content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="constanciaFinalizacion.pdf"'
    with open(os.path.join(settings.BASE_DIR, 'static', 'assets', 'docs', 'constancia_template_f.pdf'), 'rb') as f:
        response.write(f.read())

    return response


class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'student_module/password_reset_email.html'
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    template_name = 'student_module/password_reset_form.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'student_module/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm
    post_reset_login = True
    success_url = reverse_lazy('password_reset_complete')
    template_name = 'student_module/password_reset_confirm.html'


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'student_module/password_reset_complete.html'


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.method == 'POST':
            # Si el formulario fue enviado por POST, mostramos el mensaje de error
            context['show_alert'] = True
        return context

    def form_valid(self, form):
        # Obtener el usuario autenticado
        user = form.get_user()
        ## Test if is correct
        try:
            coordinator = Coordinador.objects.get(usuario=user)
        except Coordinador.DoesNotExist:
            coordinator = None
        if coordinator is not None:
            form.add_error(None, 'El usuario no se encuentra registrado como estudiante')
            return self.form_invalid(form)
        # Limpiar el formulario
        self.request.session.flush()  # Limpia los datos de sesión
        self.request.session.modified = True
        return super().form_valid(form)

def municipios_por_estado(request, id_estado):
    municipios = Municipios.objects.filter(id_estado=id_estado).values('id', 'nombre').order_by('nombre')
    return JsonResponse(list(municipios), safe=False)


def return_full_name(request):
    student = Student.objects.filter(matricula=request.user).first()
    full_name = student.nombre + ' ' + student.apellido_paterno + ' ' + student.apellido_materno
    return full_name


def privacy_notice(request):
    return render(request, 'student_module/privacy_notice.html')


@login_required
def home(request):
    student = Student.objects.filter(matricula=request.user).first()
    name = student.nombre
    pre_graduation = student.pre_egreso_abierto
    start = 'block'
    continue_form = 'none'
    full_name = return_full_name(request)
    context = {'full_name': full_name, 'name': name, 'start': start, 'continue_form': continue_form}
    finish_pre_form = student.pre_egreso_terminado
    if finish_pre_form:
        return redirect('student_module:finish')
    if pre_graduation:
        return redirect('student_module:student_info')
    else:
        start = 'block'
        context = {'full_name': full_name, 'name': name, 'start': start, 'continue_form': continue_form}
        student.pre_egreso_abierto = True
        student.save()
        return render(request, 'student_module/home.html', context)


@login_required
def finish(request):
    student = Student.objects.filter(matricula=request.user).first()
    name = student.nombre

    full_name = return_full_name(request)
    context = {'full_name': full_name, 'name': name}
    return render(request, 'student_module/finish.html', context)


def logout_view(request):
    logout(request)
    return redirect('student_module:login')


@login_required
def student_info(request) -> object:
    estados = Estados.objects.all()
    prefix = 'sse'

    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        full_name = return_full_name(request)
        try:
            alumno = Student.objects.filter(matricula=usuario).first()
            if alumno is None:
                raise Student.DoesNotExist
        except Student.DoesNotExist:
            form = StudentForm(request.POST)
            context = {'full_name': full_name, 'form': form, 'prefix': prefix}
            return render(request, STUDENT_INFO_TEMPLATE, context)

        form = StudentForm(instance=alumno)
        context = {'full_name': full_name, 'form': form, 'estados': estados, 'prefix': prefix}
        if alumno:
            form.fields['codigo_postal'].widget.attrs['maxlength'] = '5'
            return render(request, STUDENT_INFO_TEMPLATE, context)
        else:
            return render(request, STUDENT_INFO_TEMPLATE, context)

    if request.method == 'POST':
        usuario = request.user
        full_name = return_full_name(request)
        alumno = Student.objects.filter(matricula=usuario).first()
        estados = Estados.objects.all()
        form = StudentForm(request.POST)
        context = {'full_name': full_name, 'form': form, 'estados': estados, 'prefix': prefix}
        if alumno:
            if form.is_valid():
                alumno.nombre = form.cleaned_data.get('nombre')
                alumno.apellido_paterno = form.cleaned_data.get('apellido_paterno')
                alumno.apellido_materno = form.cleaned_data.get('apellido_materno')
                alumno.sexo = form.cleaned_data.get('sexo')
                alumno.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
                alumno.fecha_ingreso_lic = form.cleaned_data.get('fecha_ingreso_lic')
                alumno.correo = form.cleaned_data.get('correo')
                alumno.correo_uv = form.cleaned_data.get('correo_uv')
                alumno.celular = form.cleaned_data.get('celular')
                alumno.telefono = form.cleaned_data.get('telefono')
                alumno.twitter = form.cleaned_data.get('twitter')
                alumno.facebook = form.cleaned_data.get('facebook')
                alumno.linkedin = form.cleaned_data.get('linkedin')
                alumno.calle = form.cleaned_data.get('calle')
                alumno.colonia = form.cleaned_data.get('colonia')
                alumno.numero_exterior = form.cleaned_data.get('numero_exterior')
                alumno.numero_interior = form.cleaned_data.get('numero_interior')
                alumno.codigo_postal = form.cleaned_data.get('codigo_postal')
                alumno.estado = form.cleaned_data.get('estado')
                alumno.municipio = form.cleaned_data.get('municipio')
                alumno.localidad = form.cleaned_data.get('localidad')
                alumno.nombre_ref_principal = form.cleaned_data.get('nombre_ref_principal')
                alumno.celular_ref_principal = form.cleaned_data.get('celular_ref_principal')
                alumno.nombre_ref_auxiliar = form.cleaned_data.get('nombre_ref_auxiliar')
                alumno.celular_ref_auxiliar = form.cleaned_data.get('celular_ref_auxiliar')
                alumno.pre_egreso_abierto = True
                alumno.save()
                return redirect('student_module:job_during_school')
            else:
                errors = form.errors
                context = {'full_name': full_name, 'form': form, 'errors': errors, 'estados': estados, 'prefix': prefix}
                return render(request, "student_module/student_info.html", context)
        else:
            messages.error(request, 'No se guardaron los cambios.')
            return render(request, "student_module/student_info.html", context)


def signup(request):
    carreras = Carrera.objects.all()
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            # Guardar el usuario
            form.save()
            # Crear el objeto estudiante y asignar el usuario
            alumno = Student(matricula=form.cleaned_data.get('username').upper(),
                             nombre=form.cleaned_data.get('first_name'),
                             apellido_paterno=form.cleaned_data.get('last_name'),
                             apellido_materno=form.cleaned_data.get('apellido_materno'),
                             licenciatura_fei=form.cleaned_data.get('licenciatura_fei'),
                             correo=form.cleaned_data.get('email'))
            alumno.save()
            messages.success(request, 'Usuario registrado con éxito. Ahora puedes iniciar sesión.')
            return redirect('student_module:login')
    else:
        form = SignupUserForm()

    return render(request, 'student_module/signup.html', {'form': form, 'carreras': carreras})


@login_required
def career_selection(request):
    # Si el método es GET, el sistema recupera de la BD el objeto Seleccion Carrera correspondiente y lo usa para
    # llenar la variable form de tipo SeleccionCarreraForm. La cual DEBE recibir una instancia de un objeto tipo
    # SeleccionCarrera(ver models.py -> SeleccionCarrera)
    usuario = request.user
    student = Student.objects.filter(matricula=usuario).first()
    full_name = student.nombre + ' ' + student.apellido_paterno + ' ' + student.apellido_materno
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            career_selected = SeleccionCarrera.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = SeleccionCarreraForm(request.POST)
            context = {'full_name': full_name, 'form': form}
            return render(request, 'student_module/career_selection.html', context)

        form = SeleccionCarreraForm(instance=career_selected)
        context = {'full_name': full_name, 'form': form}
        if career_selected:
            return render(request, 'student_module/career_selection.html', context)
        else:
            return render(request, 'student_module/career_selection.html', context)

    # Si el método es POST, el sistema genera una form vacía que corresponde a la variable 'form' de tipo
    # SeleccionCarreraForm y la llena con los datos entrantes en 'request.POST'. Debido a que en la BD todas
    # las tablas dependen de la tabla Alumno mediante la llave foránea (FK): 'matricula', django necesita
    # una instancia de Alumno que le indique la relación de la FK. Por eso se obtiene un objeto Alumno correspondiente
    # al User actual. Después, se extraen los datos de 'form' para crear el objeto 'seleccion_carrera_obj'
    # de tipo SeleccionCarrera (usando el objeto 'alumno' para la matricula) y se guarda "manualmente" el objeto en
    # la BD.
    if request.method == 'POST':
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        SeleccionCarrera.objects.filter(matricula=alumno).delete()
        form = SeleccionCarreraForm(request.POST)
        context = {'full_name': full_name, 'form': form}
        if form.is_valid():
            matricula = alumno
            primera_eleccion_institucion = form.cleaned_data['primera_eleccion_institucion']
            eleccion_tipo_institucion = form.cleaned_data['eleccion_tipo_institucion']
            primera_opcion_carrera = form.cleaned_data['primera_opcion_carrera']
            primera_eleccion_nombre = form.cleaned_data['primera_eleccion_nombre']
            razon_eleccion_institucion = form.cleaned_data['razon_eleccion_institucion']
            razon_eleccion_carrera = form.cleaned_data['razon_eleccion_carrera']
            seleccion_carrera_obj = SeleccionCarrera(matricula=matricula,
                                                     primera_opcion_carrera=primera_opcion_carrera,
                                                     eleccion_tipo_institucion=eleccion_tipo_institucion,
                                                     primera_eleccion_institucion=primera_eleccion_institucion,
                                                     primera_eleccion_nombre=primera_eleccion_nombre,
                                                     razon_eleccion_institucion=razon_eleccion_institucion,
                                                     razon_eleccion_carrera=razon_eleccion_carrera)
            seleccion_carrera_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, "student_module/career_selection.html", context)


@login_required
def bachelors_degree(request):
    # Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            licenciatura = Licenciatura.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = LicenciaturaForm(request.POST)
            return render(request, "student_module/bachelors_degree.html", {"form": form})

        form = LicenciaturaForm(instance=licenciatura)
        if licenciatura:
            return render(request, 'student_module/bachelors_degree.html', {'form': form})
        else:
            return render(request, 'student_module/bachelors_degree.html', {'form': form})

    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        Licenciatura.objects.filter(matricula=alumno).delete()
        form = LicenciaturaForm(request.POST)
        if form.is_valid():
            matricula = alumno
            nombre_campus = form.cleaned_data['nombre_campus']
            nombre_carrera = form.cleaned_data['nombre_carrera']
            anio_pestudios = form.cleaned_data['anio_pestudios']
            anio_inicio = form.cleaned_data['anio_inicio']
            anio_fin = form.cleaned_data['anio_fin']
            org_ss = form.cleaned_data['org_ss']
            fecha_inicioss = form.cleaned_data['fecha_inicioss']
            fecha_finss = form.cleaned_data['fecha_finss']
            titulado = form.cleaned_data['titulado']
            promedio_final = form.cleaned_data['promedio_final']
            tipo_inscripcion = form.cleaned_data['tipo_inscripcion']
            licenciatura_obj = Licenciatura(matricula=matricula,
                                            nombre_campus=nombre_campus,
                                            nombre_carrera=nombre_carrera,
                                            anio_pestudios=anio_pestudios,
                                            anio_inicio=anio_inicio,
                                            anio_fin=anio_fin,
                                            org_ss=org_ss,
                                            fecha_inicioss=fecha_inicioss,
                                            fecha_finss=fecha_finss,
                                            titulado=titulado,
                                            promedio_final=promedio_final,
                                            tipo_inscripcion=tipo_inscripcion)
            licenciatura_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, 'student_module/bachelors_degree.html', {'form': form})


@login_required
def other_studies(request):
    full_name = return_full_name(request)
    # Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            continuacion = ContinuacionEstudios.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = ContinuacionEstudiosForm(request.POST)
            return render(request, "student_module/other_studies.html", {"form": form})

        form = ContinuacionEstudiosForm(instance=continuacion)
        if continuacion:
            return render(request, "student_module/other_studies.html", {"form": form})
        else:
            return render(request, 'student_module/other_studies.html', {'form': form})
    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        ContinuacionEstudios.objects.filter(matricula=alumno).delete()
        form = ContinuacionEstudiosForm(request.POST)
        if form.is_valid():
            matricula = alumno
            tipo_estudio_continuacion = form.cleaned_data['tipo_estudio_continuacion']
            institucion = form.cleaned_data['institucion']
            nombre_programa = form.cleaned_data['nombre_programa']
            conclusion_estudios = form.cleaned_data['conclusion_estudios']
            obtencion_grado = form.cleaned_data['obtencion_grado']
            duracion_estudios_meses = form.cleaned_data['duracion_estudios_meses']
            continuacion_estudios_obj = ContinuacionEstudios(matricula=matricula,
                                                             tipo_estudio_continuacion=tipo_estudio_continuacion,
                                                             institucion=institucion,
                                                             nombre_programa=nombre_programa,
                                                             conclusion_estudios=conclusion_estudios,
                                                             obtencion_grado=obtencion_grado,
                                                             duracion_estudios_meses=duracion_estudios_meses)
            continuacion_estudios_obj.save()
            messages.success(request, 'Se guardaron los cambios.')
    return render(request, "student_module/other_studies.html", {'full_name': full_name, "form": form})


# Falta mejorar la funcion
def validate_student_form(request):
    usuario = request.user
    alumno = Student.objects.filter(matricula=usuario).first()
    attr_student_list = alumno.__dict__
    cont_attribute_student = 0
    del attr_student_list['_state']
    for attribute in attr_student_list.values():
        if isinstance(attribute, int):
            cont_attribute_student = cont_attribute_student + 1
        else:
            if attribute is not None:
                cont_attribute_student = cont_attribute_student + 1

    return cont_attribute_student > 14


@login_required
def job_during_school(request):
    # Ver comentarios en seleccion_carrera.
    full_name = return_full_name(request)
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user

        try:
            empleo_durante_estudios = EmpleoDuranteEstudios.objects.filter(
                matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = EmpleoDuranteEstudiosForm(request.POST)
            return render(request, "student_module/job_during_school.html", {'full_name': full_name, "form": form})

        form = EmpleoDuranteEstudiosForm(instance=empleo_durante_estudios)
        if empleo_durante_estudios:
            return render(request, "student_module/job_during_school.html", {'full_name': full_name, "form": form})
        else:
            return render(request, 'student_module/job_during_school.html', {'full_name': full_name, 'form': form})

    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        student = Student.objects.filter(matricula=usuario).first()
        EmpleoDuranteEstudios.objects.filter(matricula=student).delete()
        form = EmpleoDuranteEstudiosForm(request.POST)
        if form.is_valid():
            matricula = student
            employee_confirmation = form.cleaned_data['confirmacion_empleo']
            coincidence = form.cleaned_data['coincidencia_estudios_trabajo']
            weekly_worked_hours = form.cleaned_data['horas_laboradas_semanales']
            empleo_durante_estudios_obj = EmpleoDuranteEstudios(matricula=matricula,
                                                                confirmacion_empleo=employee_confirmation,
                                                                coincidencia_estudios_trabajo=coincidence,
                                                                horas_laboradas_semanales=weekly_worked_hours)
            empleo_durante_estudios_obj.save()
            if employee_confirmation is not None:
                student.pre_egreso_terminado = validate_student_form(request)
                if student.pre_egreso_terminado:
                    student.pre_egreso_fecha_fin = datetime.now()
                student.save()
            messages.success(request, 'Se guardaron los cambios.')
    return redirect('student_module:finish')


@login_required
def job_search(request):
    # Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            busqueda_empleo = BusquedaEmpleo.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = BusquedaEmpleoForm(request.POST)
            return render(request, "student_module/job_search.html", {"form": form})

        form = BusquedaEmpleoForm(instance=busqueda_empleo)
        if job_during_school:
            return render(request, "student_module/job_search.html", {"form": form})
        else:
            return render(request, 'student_module/job_search.html', {'form': form})

    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        BusquedaEmpleo.objects.filter(matricula=alumno).delete()
        form = BusquedaEmpleoForm(request.POST)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo_egreso = form.cleaned_data['confirmacion_empleo_egreso']
            confirmacion_busqueda_empleo = form.cleaned_data['confirmacion_busqueda_empleo']
            tiempo_obtencion_empleo = form.cleaned_data['tiempo_obtencion_empleo']
            opinion_demora_empleo = form.cleaned_data['opinion_demora_empleo']
            medio_obtencion_empleo = form.cleaned_data['medio_obtencion_empleo']
            requisito_formal = form.cleaned_data['requisito_formal']
            razon_no_busqueda = form.cleaned_data['razon_no_busqueda']
            busqueda_empleo_obj = BusquedaEmpleo(matricula=matricula,
                                                 confirmacion_empleo_egreso=confirmacion_empleo_egreso,
                                                 confirmacion_busqueda_empleo=confirmacion_busqueda_empleo,
                                                 tiempo_obtencion_empleo=tiempo_obtencion_empleo,
                                                 opinion_demora_empleo=opinion_demora_empleo,
                                                 medio_obtencion_empleo=medio_obtencion_empleo,
                                                 requisito_formal=requisito_formal,
                                                 razon_no_busqueda=razon_no_busqueda)
            busqueda_empleo_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, "student_module/job_search.html", {"form": form})


@login_required
def job_after_grad(request):
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            empleo_inmediato = EmpleoInmediato.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = EmpleoInmediatoForm(request.POST)
            return render(request, "student_module/job_after_grad.html", {"form": form})

        form = EmpleoInmediatoForm(instance=empleo_inmediato)
        if empleo_inmediato:
            return render(request, 'student_module/job_after_grad.html', {'form': form})
        else:
            return render(request, 'student_module/job_after_grad.html', {'form': form})
    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        EmpleoInmediato.objects.filter(matricula=alumno).delete()
        form = EmpleoInmediatoForm(request.POST)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo_inmediato = form.cleaned_data['confirmacion_empleo_inmediato']
            rol_egresado_empleo = form.cleaned_data['rol_egresado_empleo']
            puesto_empleo_inmediato = form.cleaned_data['puesto_empleo_inmediato']
            tamano_empresa_inmediata = form.cleaned_data['tamano_empresa_inmediata']
            nombre_empleo_inmediato = form.cleaned_data['nombre_empleo_inmediato']
            nombre_jefe_supervisor = form.cleaned_data['nombre_jefe_supervisor']
            telefono_empleo_inmediato = form.cleaned_data['telefono_empleo_inmediato']
            correo_empleo_inmediato = form.cleaned_data['correo_empleo_inmediato']
            tipo_contratacion = form.cleaned_data['tipo_contratacion']
            regimen_juridico = form.cleaned_data['regimen_juridico']
            ingreso_mensual_neto_inicio = form.cleaned_data['ingreso_mensual_neto_inicio']
            horas_laboral_semanales = form.cleaned_data['horas_laboral_semanales']
            duracion_trabajo = form.cleaned_data['duracion_trabajo']
            coincidencia_estudios_trabajo = form.cleaned_data['coincidencia_estudios_trabajo']
            sector_economico = form.cleaned_data['sector_economico']
            razon_desempleo = form.cleaned_data['razon_desempleo']
            empleo_inmediato_obj = EmpleoInmediato(matricula=matricula,
                                                   confirmacion_empleo_inmediato=confirmacion_empleo_inmediato,
                                                   rol_egresado_empleo=rol_egresado_empleo,
                                                   puesto_empleo_inmediato=puesto_empleo_inmediato,
                                                   tamano_empresa_inmediata=tamano_empresa_inmediata,
                                                   nombre_empleo_inmediato=nombre_empleo_inmediato,
                                                   nombre_jefe_supervisor=nombre_jefe_supervisor,
                                                   telefono_empleo_inmediato=telefono_empleo_inmediato,
                                                   correo_empleo_inmediato=correo_empleo_inmediato,
                                                   tipo_contratacion=tipo_contratacion,
                                                   regimen_juridico=regimen_juridico,
                                                   ingreso_mensual_neto_inicio=ingreso_mensual_neto_inicio,
                                                   horas_laboral_semanales=horas_laboral_semanales,
                                                   duracion_trabajo=duracion_trabajo,
                                                   coincidencia_estudios_trabajo=coincidencia_estudios_trabajo,
                                                   sector_economico=sector_economico,
                                                   razon_desempleo=razon_desempleo)
            empleo_inmediato_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, 'student_module/job_after_grad.html', {'form': form})


@login_required
def current_job(request):  # Corresponde a model Empresa, form EmpresaForm y en la BD como la tabla 'empresa'

    # Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            empleo_actual = Empresa.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = EmpresaForm(request.POST)
            return render(request, "student_module/current_job.html", {"form": form})

        form = EmpresaForm(instance=empleo_actual)
        if empleo_actual:
            return render(request, 'student_module/current_job.html', {'form': form})
        else:
            return render(request, 'student_module/current_job.html', {'form': form})

    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        Empresa.objects.filter(matricula=alumno).delete()
        form = EmpresaForm(request.POST)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo_empresa = form.cleaned_data['confirmacion_empleo_empresa']
            razon_desempleo_empresa = form.cleaned_data['razon_desempleo_empresa']
            nombre_empresa = form.cleaned_data['nombre_empresa']
            calle_empresa = form.cleaned_data['calle_empresa']
            colonia_empresa = form.cleaned_data['colonia_empresa']
            num_empresa = form.cleaned_data['num_empresa']
            codigo_postal = form.cleaned_data['codigo_postal']
            id_estado = form.cleaned_data['id_estado']
            id_municipio = form.cleaned_data['id_municipio']
            rol_egresado_empresa = form.cleaned_data['rol_egresado_empresa']
            puesto = form.cleaned_data['puesto']
            actividad_egresado_empresa = form.cleaned_data['actividad_egresado_empresa']
            tamanio_empresa = form.cleaned_data['tamanio_empresa']
            tipo_contratacion = form.cleaned_data['tipo_contratacion']
            regimen_juridico = form.cleaned_data['regimen_juridico']
            ingresomensual_neto = form.cleaned_data['ingresomensual_neto']
            horas_laborales = form.cleaned_data['horas_laborales']
            duracion_empresa_meses = form.cleaned_data['duracion_empresa_meses']
            medida_coincidencia_labestudios = form.cleaned_data['medida_coincidencia_labestudios']
            medio_obtencion_empresa = form.cleaned_data['medio_obtencion_empresa']
            sector_economico = form.cleaned_data['sector_economico']
            empresa_obj = Empresa(matricula=matricula,
                                  confirmacion_empleo_empresa=confirmacion_empleo_empresa,
                                  razon_desempleo_empresa=razon_desempleo_empresa,
                                  nombre_empresa=nombre_empresa,
                                  calle_empresa=calle_empresa,
                                  colonia_empresa=colonia_empresa,
                                  num_empresa=num_empresa,
                                  codigo_postal=codigo_postal,
                                  id_estado=id_estado,
                                  id_municipio=id_municipio,
                                  rol_egresado_empresa=rol_egresado_empresa,
                                  puesto=puesto,
                                  actividad_egresado_empresa=actividad_egresado_empresa,
                                  tamanio_empresa=tamanio_empresa,
                                  tipo_contratacion=tipo_contratacion,
                                  regimen_juridico=regimen_juridico,
                                  ingresomensual_neto=ingresomensual_neto,
                                  horas_laborales=horas_laborales,
                                  duracion_empresa_meses=duracion_empresa_meses,
                                  medida_coincidencia_labestudios=medida_coincidencia_labestudios,
                                  medio_obtencion_empresa=medio_obtencion_empresa,
                                  sector_economico=sector_economico)
            empresa_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, 'student_module/current_job.html', {'form': form})


@login_required
def recommendations(request):
    # Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            recomendaciones = DesempenioRecomendaciones.objects.filter(
                matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = DesempenioRecomendacionesForm(request.POST)
            return render(request, "student_module/recommendations.html", {"form": form})

        form = DesempenioRecomendacionesForm(instance=recomendaciones)
        if recomendaciones:
            return render(request, 'student_module/recommendations.html', {'form': form})
        else:
            return render(request, 'student_module/recommendations.html', {'form': form})
    # Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        DesempenioRecomendaciones.objects.filter(matricula=alumno).delete()
        form = DesempenioRecomendacionesForm(request.POST)
        if form.is_valid():
            matricula = alumno
            nivel_satisfaccion = form.cleaned_data['nivel_satisfaccion']
            grado_exigencia = form.cleaned_data['grado_exigencia']
            nivel_formacion = form.cleaned_data['nivel_formacion']
            modificaciones_planest = form.cleaned_data['modificaciones_planest']
            opinion_orgainst = form.cleaned_data['opinion_orgainst']
            desempenio_recomendaciones_obj = DesempenioRecomendaciones(matricula=matricula,
                                                                       nivel_satisfaccion=nivel_satisfaccion,
                                                                       grado_exigencia=grado_exigencia,
                                                                       nivel_formacion=nivel_formacion,
                                                                       modificaciones_planest=modificaciones_planest,
                                                                       opinion_orgainst=opinion_orgainst)
            desempenio_recomendaciones_obj.save()
            messages.success(request, 'Se guardaron los cambios.')
    return render(request, 'student_module/recommendations.html', {'form': form})
