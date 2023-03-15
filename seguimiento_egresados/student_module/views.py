from django.shortcuts import render
from student_module.forms import SignupUserForm
from .forms import CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
import re
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.http import HttpResponse, request
from .forms import *
from django.contrib import messages

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm

def privacy_notice(request):
    return render(request, 'student_module/privacy_notice.html')

@login_required
def home(request):
        student = Student.objects.filter(matricula=request.user).first()
        name = student.nombre
        context = {'name': name}
        full_name = student.nombre + ' ' + student.apellido_paterno + ' ' + student.apellido_materno
        context = {'full_name': full_name, 'name': name}
        return render(request, 'student_module/home.html', context)

def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def student_info(request):
    user = request.user
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            alumno = Student.objects.filter(matricula=usuario).first()
        except Student.ObjectDoesNotExist:
            form = StudentForm(request.POST)
            contexto = {'form':form}
            return render(request, 'student_module/student_info.html', contexto)

        form = StudentForm(instance=alumno)
        contexto = {'form':form}
        if alumno:
            form.fields['codigo_postal'].widget.attrs['maxlength'] = '5'
            return render(request, 'student_module/student_info.html', contexto)
        else:
            return render(request, 'student_module/student_info.html', contexto)
    
    if request.method == 'POST':
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        form = StudentForm(request.POST)
        contexto = {'form':form}
        try:
            if alumno:
                print("usuario ya existe, actualizar")
                if form.is_valid():
                    print("actualizando...")
                    alumno.nombre = form.cleaned_data.get('nombre')
                    alumno.apellido_paterno = form.cleaned_data.get('apellido_paterno')
                    alumno.apellido_materno = form.cleaned_data.get('apellido_materno')
                    alumno.sexo = form.cleaned_data.get('sexo')
                    alumno.fecha_nacimiento = form.cleaned_data.get('fecha_nacimiento')
                    alumno.fecha_ingreso_lic = form.cleaned_data.get('fecha_ingreso_lic')
                    alumno.correo =  form.cleaned_data.get('correo')
                    alumno.celular = form.cleaned_data.get('celular')
                    alumno.telefono = form.cleaned_data.get('telefono')
                    alumno.twitter = form.cleaned_data.get('twitter')
                    alumno.facebook = form.cleaned_data.get('facebook')
                    alumno.linkedin = form.cleaned_data.get('linkedin')
                    alumno.calle = form.cleaned_data.get('calle')
                    alumno.colonia = form.cleaned_data.get('colonia')
                    alumno.numero = form.cleaned_data.get('numero')
                    alumno.codigo_postal = form.cleaned_data.get('codigo_postal')
                    alumno.id_estado = form.cleaned_data.get('id_estado')
                    alumno.id_municipio = form.cleaned_data.get('id_municipio')
                    alumno.save(update_fields=["nombre", "apellido_paterno", "apellido_materno", "genero", "fecha_nacimiento",
                                                "fecha_ingreso_lic", "correo", "correo_uv", "celular", "telefono", "twitter", "facebook", "calle",
                                                "colonia", "numero", "codigo_postal", "id_estado", "id_municipio"])
                    return render(request, "student_module/student_info.html", contexto)
                else:
                    print("Formulario no válido")
                    print(form.errors)
                    return render(request, "student_module/student_info.html", contexto)           
        except:
            messages.error(request, f'No se guardaron los cambios.')
    return render(request, "student_module/student_info.html", contexto)

def signup(request):
    if request.method == 'POST':
        form = SignupUserForm(request.POST)
        if form.is_valid():
            # Guardar el usuario
            user = form.save()
            # Crear el objeto estudiante y asignar el usuario
            alumno = Student(matricula=form.cleaned_data.get('username'),
                              nombre=form.cleaned_data.get('first_name'),
                              apellido_paterno=form.cleaned_data.get('last_name'),
                              apellido_materno=form.cleaned_data.get('apellido_materno'))
            alumno.save()

            messages.success(request, f'Usuario registrado con éxito. Ahora puedes iniciar sesión.')
            return redirect('student_module:login')
    else:
        form = SignupUserForm()
    
    return render(request, 'student_module/signup.html', {'form': form})

@login_required
def career_selection(request):
    #Si el método es GET, el sistema recupera de la BD el objeto Seleccion Carrera correspondiente y lo usa para
    #llenar la variable form de tipo SeleccionCarreraForm. La cual DEBE recibir una instancia de un objeto tipo
    #SeleccionCarrera(ver models.py -> SeleccionCarrera)
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            career_selection = SeleccionCarrera.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = SeleccionCarreraForm(request.POST)
            return render(request, 'student_module/career_selection.html', {'form':form})

        form = SeleccionCarreraForm(instance=career_selection)
        if career_selection:
            return render(request, 'student_module/career_selection.html', {'form':form})
        else:
            return render(request, 'student_module/career_selection.html', {'form':form})

    #Si el método es POST, el sistema genera una form vacía que corresponde a la variable 'form' de tipo
    #SeleccionCarreraForm y la llena con los datos entrantes en 'request.POST'. Debido a que en la BD todas 
    #las tablas dependen de la tabla Alumno mediante la llave foránea (FK): 'matricula', django necesita 
    #una instancia de Alumno que le indique la relación de la FK. Por eso se obtiene un objeto Alumno correspondiente
    #al User actual. Después, se extraen los datos de 'form' para crear el objeto 'seleccion_carrera_obj'  
    # de tipo SeleccionCarrera (usando el objeto 'alumno' para la matricula) y se guarda "manualmente" el objeto en la BD.

    if request.method == 'POST':
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        SeleccionCarrera.objects.filter(matricula=alumno).delete()
        form = SeleccionCarreraForm(request.POST)
        
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
    return render(request, "student_module/career_selection.html", {"form":form})

@login_required
def bachelors_degree(request):
    #Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            licenciatura = Licenciatura.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:             
            form = LicenciaturaForm(request.POST)
            return render(request, "student_module/bachelors_degree.html", {"form":form})
        
        form = LicenciaturaForm(instance=licenciatura)
        if licenciatura:
            return render(request, 'student_module/bachelors_degree.html', {'form':form})
        else:
            return render(request, 'student_module/bachelors_degree.html', {'form':form})

    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        Licenciatura.objects.filter(matricula=alumno).delete()
        form = LicenciaturaForm(request.POST)
        #print(form.is_valid())
        #print(form.errors)
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
    return render(request, 'student_module/bachelors_degree.html', {'form':form})
    
@login_required
def other_studies(request):
    #Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            continuacion = ContinuacionEstudios.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:  
            form = ContinuacionEstudiosForm(request.POST)
            return render(request, "student_module/other_studies.html", {"form":form})

        form = ContinuacionEstudiosForm(instance=continuacion)
        if continuacion:
            return render(request, "student_module/other_studies.html", {"form":form})
        else:
            return render(request, 'student_module/other_studies.html', {'form':form})
    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        ContinuacionEstudios.objects.filter(matricula=alumno).delete()
        form = ContinuacionEstudiosForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            matricula = alumno
            tipo_estudio_continuacion = form.cleaned_data['tipo_estudio_continuacion']
            institucion = form.cleaned_data['institucion']
            nombre_programa = form.cleaned_data['nombre_programa']
            conclusion_estudios = form.cleaned_data['conclusion_estudios']
            obtencion_grado =form.cleaned_data['obtencion_grado']
            duracion_estudios_meses = form.cleaned_data['duracion_estudios_meses']
            continuacion_estudios_obj = ContinuacionEstudios(matricula= matricula,
                tipo_estudio_continuacion=tipo_estudio_continuacion,
                institucion=institucion,
                nombre_programa=nombre_programa,
                conclusion_estudios =conclusion_estudios,
                obtencion_grado =obtencion_grado,
                duracion_estudios_meses = duracion_estudios_meses)
            continuacion_estudios_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, "student_module/other_studies.html", {"form":form})

@login_required
def job_during_school(request):
    #Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            empleo_durante_estudios = EmpleoDuranteEstudios.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = EmpleoDuranteEstudiosForm(request.POST)
            return render(request, "student_module/job_during_school.html", {"form":form})

        form = EmpleoDuranteEstudiosForm(instance=empleo_durante_estudios)
        if empleo_durante_estudios:
            return render(request, "student_module/job_during_school.html", {"form":form})
        else:
            return render(request, 'student_module/job_during_school.html', {'form':form})
    
    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        EmpleoDuranteEstudios.objects.filter(matricula=alumno).delete()
        form = EmpleoDuranteEstudiosForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo = form.cleaned_data['confirmacion_empleo']
            coincidencia_estudios_trabajo = form.cleaned_data['coincidencia_estudios_trabajo']
            horas_laboradas_semanales = form.cleaned_data['horas_laboradas_semanales']
            empleo_durante_estudios_obj = EmpleoDuranteEstudios(matricula= matricula,
                confirmacion_empleo=confirmacion_empleo,
                coincidencia_estudios_trabajo=coincidencia_estudios_trabajo,
                horas_laboradas_semanales=horas_laboradas_semanales)
            empleo_durante_estudios_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, "student_module/job_during_school.html", {"form":form})

@login_required
def job_search(request):
    #Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            busqueda_empleo = BusquedaEmpleo.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:  
            form = BusquedaEmpleoForm(request.POST)
            return render(request, "student_module/job_search.html", {"form":form})

        form = BusquedaEmpleoForm(instance=busqueda_empleo)
        if job_during_school:
            return render(request, "student_module/job_search.html", {"form":form})
        else:
            return render(request, 'student_module/job_search.html', {'form':form})
    
    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        BusquedaEmpleo.objects.filter(matricula=alumno).delete()
        form = BusquedaEmpleoForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo_egreso = form.cleaned_data['confirmacion_empleo_egreso']
            confirmacion_busqueda_empleo = form.cleaned_data['confirmacion_busqueda_empleo']
            tiempo_obtencion_empleo = form.cleaned_data['tiempo_obtencion_empleo']
            opinion_demora_empleo = form.cleaned_data['opinion_demora_empleo']
            medio_obtencion_empleo = form.cleaned_data['medio_obtencion_empleo']
            requisito_formal = form.cleaned_data['requisito_formal']
            razon_no_busqueda = form.cleaned_data['razon_no_busqueda']
            busqueda_empleo_obj = BusquedaEmpleo(matricula= matricula,
                confirmacion_empleo_egreso=confirmacion_empleo_egreso,
                confirmacion_busqueda_empleo=confirmacion_busqueda_empleo,
                tiempo_obtencion_empleo=tiempo_obtencion_empleo,
                opinion_demora_empleo=opinion_demora_empleo,
                medio_obtencion_empleo=medio_obtencion_empleo,
                requisito_formal=requisito_formal,
                razon_no_busqueda=razon_no_busqueda)
            busqueda_empleo_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, "student_module/job_search.html", {"form":form})

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
            return render(request, "student_module/job_after_grad.html", {"form":form})

        form = EmpleoInmediatoForm(instance=empleo_inmediato)
        if empleo_inmediato:
            return render(request, 'student_module/job_after_grad.html', {'form':form})
        else:
            return render(request, 'student_module/job_after_grad.html', {'form':form})
    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        EmpleoInmediato.objects.filter(matricula=alumno).delete()
        form = EmpleoInmediatoForm(request.POST)
        #print(form.is_valid())
        #print(form.errors)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo_inmediato=form.cleaned_data['confirmacion_empleo_inmediato']
            rol_egresado_empleo=form.cleaned_data['rol_egresado_empleo']
            puesto_empleo_inmediato = form.cleaned_data['puesto_empleo_inmediato']
            tamano_empresa_inmediata = form.cleaned_data['tamano_empresa_inmediata']
            nombre_empleo_inmediato = form.cleaned_data['nombre_empleo_inmediato']
            nombre_jefe_supervisor = form.cleaned_data['nombre_jefe_supervisor']
            telefono_empleo_inmediato = form.cleaned_data['telefono_empleo_inmediato']
            correo_empleo_inmediato = form.cleaned_data['correo_empleo_inmediato']
            tipo_contratacion=form.cleaned_data['tipo_contratacion']
            regimen_juridico = form.cleaned_data['regimen_juridico']
            ingreso_mensual_neto_inicio = form.cleaned_data['ingreso_mensual_neto_inicio']
            horas_laboral_semanales = form.cleaned_data['horas_laboral_semanales']
            duracion_trabajo = form.cleaned_data['duracion_trabajo']
            coincidencia_estudios_trabajo=form.cleaned_data['coincidencia_estudios_trabajo']
            sector_economico = form.cleaned_data['sector_economico']
            razon_desempleo = form.cleaned_data['razon_desempleo']
            empleo_inmediato_obj= EmpleoInmediato(matricula=matricula,
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
    return render(request, 'student_module/job_after_grad.html', {'form':form})

@login_required
def current_job(request): #Corresponde a model Empresa, form EmpresaForm y en la BD como la tabla 'empresa'

    #Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            empleo_actual = Empresa.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = EmpresaForm(request.POST)
            return render(request, "student_module/current_job.html", {"form":form})

        form = EmpresaForm(instance=empleo_actual)
        if empleo_actual:
            return render(request, 'student_module/current_job.html', {'form':form})
        else:
            return render(request, 'student_module/current_job.html', {'form':form})         

    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        Empresa.objects.filter(matricula=alumno).delete()
        form = EmpresaForm(request.POST)
        #print(form.is_valid())
        #print(form.errors)
        if form.is_valid():
            matricula = alumno
            confirmacion_empleo_empresa= form.cleaned_data['confirmacion_empleo_empresa']
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
                razon_desempleo_empresa= razon_desempleo_empresa,
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
    return render(request, 'student_module/current_job.html', {'form':form})

@login_required
def recommendations(request):
    #Ver comentarios en seleccion_carrera.
    if request.method == 'GET':
        storage = messages.get_messages(request)
        storage.used = True
        usuario = request.user
        try:
            recomendaciones = DesempenioRecomendaciones.objects.filter(matricula=Student.objects.get(matricula=usuario)).first()
        except Student.DoesNotExist:
            form = DesempenioRecomendacionesForm(request.POST)
            return render(request, "student_module/recommendations.html", {"form":form})

        form = DesempenioRecomendacionesForm(instance=recomendaciones)
        if recomendaciones:
            return render(request, 'student_module/recommendations.html', {'form':form})
        else:
            return render(request, 'student_module/recommendations.html', {'form':form})
    #Ver comentarios en seleccion_carrera.
    if request.method == "POST":
        usuario = request.user
        alumno = Student.objects.filter(matricula=usuario).first()
        DesempenioRecomendaciones.objects.filter(matricula=alumno).delete()
        form = DesempenioRecomendacionesForm(request.POST)
        #print(form.is_valid())
        #print(form.errors)
        if form.is_valid():
            matricula = alumno
            nivel_satisfaccion = form.cleaned_data['nivel_satisfaccion']
            grado_exigencia = form.cleaned_data['grado_exigencia']
            nivel_formacion = form.cleaned_data['nivel_formacion']
            modificaciones_planest = form.cleaned_data['modificaciones_planest']
            opinion_orgainst = form.cleaned_data['opinion_orgainst']
            desempenio_recomendaciones_obj = DesempenioRecomendaciones(matricula=matricula,
                nivel_satisfaccion=nivel_satisfaccion,
                grado_exigencia= grado_exigencia,
                nivel_formacion=nivel_formacion,
                modificaciones_planest=modificaciones_planest,
                opinion_orgainst=opinion_orgainst)
            desempenio_recomendaciones_obj.save()
            messages.success(request, f'Se guardaron los cambios.')
    return render(request, 'student_module/recommendations.html', {'form':form})