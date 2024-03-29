import datetime

from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm, UserCreationForm, PasswordResetForm, User
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.forms.widgets import DateInput, TextInput
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Student, SeleccionCarrera, Carrera, Licenciatura, ContinuacionEstudios, SI_NO_CHOICES_NUMERIC
from .models.empleo import EmpleoDuranteEstudios, RAZON_NO_BUSQUEDA_EMPLEO, BusquedaEmpleo, EmpleoInmediato, Empresa, \
    DesempenioRecomendaciones

NUMBER = '[0-9]'

MATRICULA = 'Matrícula'


class MatriculaInput(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab'}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value[i:i + 1] for i in range(0, 9)]
        return [None, None, None, None, None, None, None, None, None]

    def value_from_datadict(self, data, files, name):
        values = [data.get(name + '_%s' % i, '')[:1] for i in range(0, 9)]
        return ''.join(values)


class SignupUserForm(UserCreationForm):
    matricula_validator = RegexValidator(
        r'[Ss](1[4-9]|[2-9][0-9])\d{6}$',
        'Por favor ingrese una matrícula válida'
    )

    username = forms.CharField(required=True, widget=MatriculaInput(
        attrs={'placeholder': '', 'class': 'form-control', 'autocomplete': 'username'}),
                                      validators=[matricula_validator])
    username.label = ''

    first_name = forms.CharField(max_length=30, required=True,
                                        widget=forms.TextInput(
                                            attrs={'placeholder': '', 'class': 'form-control'}))
    first_name.label = 'Nombre(s):'

    last_name = forms.CharField(max_length=30, required=True,
                                       widget=forms.TextInput(
                                           attrs={'placeholder': '', 'class': 'form-control'}))
    last_name.label = 'Apellido paterno:'

    apellido_materno = forms.CharField(max_length=30, required=True,
                                              widget=forms.TextInput(
                                                  attrs={'placeholder': '', 'class': 'form-control'}))
    apellido_materno.label = 'Apellido materno:'

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'rafaelhernandez@ejemplo.com'}))
    email.label = 'Correo electrónico personal:'
    licenciatura_fei = forms.ChoiceField(
        widget=forms.Select,
        choices=[],
        label='Licenciatura')

    try:
        licenciatura_fei = forms.ChoiceField(
            widget=forms.Select,
            choices=[(carrera.licenciatura, carrera.licenciatura) for carrera in Carrera.objects.all()],
            label='Licenciatura')
    except:
        pass
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}))
    password1.label = 'Contraseña:'

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '', 'class': 'form-control'}))
    password2.label = 'Confirmar contraseña:'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'licenciatura_fei', 'first_name', 'last_name',
                  'apellido_materno']

    def clean_username(self):
        # Get the username value entered by the user
        username = self.cleaned_data.get('username')

        # Convert the username value to uppercase
        username = username.upper()

        # Return the cleaned username value
        return username

    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')
        return matricula

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        if commit:
            user.save()

        return user


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'}),
        error_messages={
            'required': _("Por favor escribe un correo correcto"),
            'invalid': _("Por favor escribe un correo incorrecto"),
        }
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("Nueva contraseña"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=_("Tu contraseña debe tener al menos 8 caracteres"),
        validators=[],
    )
    new_password2 = forms.CharField(
        label=_("Confirmación de nueva contraseña"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    )


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Matrícula:', max_length=254,
                                      widget=forms.TextInput(attrs={'placeholder': '', 'class': 'form-control'}))
    password = forms.CharField(label="Contraseña:",
                                      widget=forms.PasswordInput(
                                          attrs={'placeholder': '', 'class': 'form-control'}))


class CrearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'sexo',
                  'fecha_nacimiento', 'fecha_ingreso_lic', 'correo', 'correo_uv', 'celular', 'telefono', 'twitter',
                  'facebook', 'linkedin', 'calle', 'colonia', 'numero_exterior', 'numero_interior', 'codigo_postal',
                  'estado', 'municipio', 'localidad', 'nombre_ref_principal', 'celular_ref_principal',
                  'nombre_ref_auxiliar', 'celular_ref_auxiliar']

        labels = {
            'matricula': MATRICULA,
            'nombre': 'Nombre*',
            'apellido_paterno': 'Apellido paterno*',
            'apellido_materno': 'Apellido materno*',
            'sexo': 'Sexo*',
            'fecha_nacimiento': 'Fecha de nacimiento*',
            'fecha_ingreso_lic': 'Año de ingreso a la licenciatura',
            'correo': 'Correo electronico*',
            'correo_uv': 'Correo electronico alterno',
            'celular': 'Celular*',
            'telefono': 'Teléfono',
            'twitter': 'Twitter',
            'facebook': 'Facebook',
            'linkedin': 'LinkedIn',
            'calle': 'Calle*',
            'numero_exterior': 'Número exterior*',
            'numero_interior': 'Número interior',
            'colonia': 'Colonia*',
            'numero': 'Número*',
            'codigo_postal': 'Código Postal*',
            'estado': 'Estado',
            'municipio': 'Municipio',
            'localidad': 'Localidad',
            'nombre_ref_principal': 'Nombre completo* ',
            'celular_ref_principal': 'Celular* ',
            'nombre_ref_auxiliar': 'Nombre completo ',
            'celular_ref_auxiliar': 'Celular'
        }

        max_year = datetime.datetime.now().year - 4
        max_born_date = str(datetime.date.today() - datetime.timedelta(days=365 * 20))
        min_born_date = str(datetime.date.today() - datetime.timedelta(days=365 * 40))
        widgets = {
            'estado': forms.Select(choices=[]),
            'municipio': forms.Select(choices=[]),
            'nombre': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'apellido_paterno': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'apellido_materno': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            # 'min':min_born_date ,'max': max_born_date
            'fecha_nacimiento': DateInput(attrs={'class': 'form-control', 'type': 'date', }),
            'fecha_ingreso_lic': TextInput(
                attrs={'type': 'number', 'placeholder': '', 'class': 'form-control', 'min': '2014', 'max': max_year}),
            'correo': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'correo_uv': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'celular': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'telefono': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'facebook': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'twitter': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'linkedin': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'calle': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'numero_exterior': TextInput(
                attrs={'type': 'number', 'placeholder': '', 'class': 'form-control', 'min': '1'}),
            'numero_interior': TextInput(
                attrs={'type': 'number', 'placeholder': '', 'class': 'form-control', 'min': '1'}),
            'colonia': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'codigo_postal': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'localidad': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nombre_ref_principal': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'celular_ref_principal': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nombre_ref_auxiliar': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'celular_ref_auxiliar': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class SeleccionCarreraForm(forms.ModelForm):
    primera_eleccion_institucion = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿La institución en que usted cursó sus estudios de licenciatura fue la primera que eligió?')

    primera_opcion_carrera = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿La carrera que usted cursó fue su primera elección?')

    class Meta:
        model = SeleccionCarrera
        fields = ['primera_eleccion_institucion', 'eleccion_tipo_institucion', 'razon_eleccion_institucion',
                  'primera_opcion_carrera', 'primera_eleccion_nombre',
                  'razon_eleccion_carrera']
        labels = {
            # 'matricula': MATRICULA,
            'primera_eleccion_institucion': '¿La institución en que usted cursó sus estudios de licenciatura fue la '
                                            'primera que eligió?',
            'eleccion_tipo_institucion': 'En caso de haber respondido "No" en la pregunta anterior, ¿Qué tipo de '
                                         'institución que había elegido como primera opción?',
            'primera_opcion_carrera': '¿La carrera que usted cursó fue su primera elección?',
            'primera_eleccion_nombre': 'En caso de haber respondido "No" en la pregunta anterior, ¿Qué carrera había '
                                       'elegido?',
            'razon_eleccion_institucion': '¿Cuál fue para usted la razón más importante en la elección de la '
                                          'institución (en la que cursó sus estudios)?',
            'razon_eleccion_carrera': '¿Cuál fue para usted la razón más importante en la elección de la carrera?',
        }
        widgets = {
            # 'matricula':forms.HiddenInput(),
            'primera_eleccion_nombre': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'razon_eleccion_institucion': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'razon_eleccion_carrera': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class LicenciaturaForm(forms.ModelForm):
    class Meta:
        model = Licenciatura
        fields = ('nombre_campus', 'nombre_carrera', 'anio_pestudios', 'anio_inicio', 'anio_fin', 'org_ss',
                  'fecha_inicioss', 'fecha_finss', 'titulado', 'promedio_final', 'tipo_inscripcion')
        labels = {
            'matricula': MATRICULA,
            'nombre_campus': 'Nombre del campus',
            'nombre_carrera': 'Nombre de la carrera',
            'anio_pestudios': 'Generación',
            'anio_inicio': 'Año de inicio',
            'anio_fin': 'Año de finalización',
            'org_ss': 'Organización donde realizó el servicio social',
            'fecha_inicioss': 'Fecha de inicio del servicio social',
            'fecha_finss': 'Fecha de finalización del servicio social',
            'titulado': '¿Titulado?',
            'promedio_final': 'Promedio final',
            'tipo_inscripcion': 'Durante la mayor parte de su carrera estuvo usted inscrito como alumno de:',
        }
        widgets = {
            'matricula': forms.HiddenInput(),
            'nombre_campus': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'anio_pestudios': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'anio_inicio': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'anio_fin': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'org_ss': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'fecha_inicioss': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_finss': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'promedio_final': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class ContinuacionEstudiosForm(forms.ModelForm):
    conclusion_estudios = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿Concluyó usted estos estudios?')

    obtencion_grado = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿Obtuvo usted el grado o diploma?')

    class Meta:
        model = ContinuacionEstudios
        fields = (
            'tipo_estudio_continuacion', 'institucion', 'nombre_programa', 'conclusion_estudios', 'obtencion_grado',
            'duracion_estudios_meses')
        labels = {
            'matricula': MATRICULA,
            'tipo_estudio_continuacion': '¿Una vez que concluyó su licenciatura optó por otro tipo de estudios? ¿Cuál '
                                         'fue este tipo de estudio?',
            'institucion': 'Tipo de institución',
            'nombre_programa': 'Nombre del programa',
            'conclusion_estudios': '¿Concluyó usted estos estudios?',
            'obtencion_grado': '¿Obtuvo usted el grado o diploma?',
            'duracion_estudios_meses': 'En meses, ¿cuánto duraron los estudios?',
        }
        widgets = {
            'matricula': forms.HiddenInput(),
            'nombre_programa': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'duracion_estudios_meses': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class EmpleoDuranteEstudiosForm(forms.ModelForm):
    confirmacion_empleo = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿Trabajó usted durante el transcurso de sus estudios en la licenciatura?')

    class Meta:
        model = EmpleoDuranteEstudios
        fields = ('confirmacion_empleo', 'coincidencia_estudios_trabajo', 'horas_laboradas_semanales')
        labels = {
            'matricula': MATRICULA,
            'confirmacion_empleo': '¿Trabajó usted durante el transcurso de sus estudios en la licenciatura?',
            'coincidencia_estudios_trabajo': '¿En qué medida coincidía su trabajo con sus estudios de licenciatura?',
            'horas_laboradas_semanales': 'Número de horas en promedio que laboraba a la semana:'
        }
        widgets = {
            'matricula': forms.HiddenInput(),
            'horas_laboradas_semanales': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class BusquedaEmpleoForm(forms.ModelForm):
    confirmacion_empleo_egreso = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿Tenía usted empleo al concluir sus estudios de licenciatura? (Recuerde que por estudios concluidos '
              'entendemos haber cubierto el total de los créditos de cursos).')

    confirmacion_busqueda_empleo = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿Al concluir sus estudios buscó usted activamente trabajo? (Aunque ya estuviera trabajando)')

    razon_no_busqueda = forms.ChoiceField(
        label='¿Cuál es la principal razón por la que no buscó empleo? (Sólo en caso de no haber buscado empleo al '
              'concluir sus estudios de licenciatura)',
        widget=forms.Select,
        choices=RAZON_NO_BUSQUEDA_EMPLEO,
        required=False)

    class Meta:
        model = BusquedaEmpleo
        fields = ('confirmacion_empleo_egreso', 'confirmacion_busqueda_empleo', 'tiempo_obtencion_empleo',
                  'opinion_demora_empleo',
                  'medio_obtencion_empleo', 'requisito_formal', 'razon_no_busqueda')
        labels = {
            'matricula': MATRICULA,
            'confirmacion_empleo_egreso': '¿Tenía usted empleo al concluir sus estudios de licenciatura? (Recuerde '
                                          'que por estudios concluidos entendemos haber cubierto el total de créditos '
                                          'de cursos)',
            'confirmacion_busqueda_empleo': '¿Al concluir sus estudios buscó Ud. activamente trabajo? (Nos interesa '
                                            'su respuesta, aunque ya estuviese trabajando)',
            'tiempo_obtencion_empleo': 'Indique el tiempo que le llevó conseguir  el primer empleo, una vez que '
                                       'concluyó sus estudios de licenciatura. (Nos referimos al empleo cuya duración'
                                       ' mínima fue de tres meses)',
            'opinion_demora_empleo': '¿A qué atribuye la demora y/o dificultades para conseguir empleo al concluir '
                                     'sus estudios? (Solo si tuvo demoras o dificultades)',
            'medio_obtencion_empleo': 'Señale el principal medio a través del cual encontró trabajo al concluir sus '
                                      'estudios',
            'requisito_formal': '¿Cuál fue el requisito formal de mayor peso para conseguir el trabajo, una vez que '
                                'concluyó sus estudios y lo buscó?',
            'razon_no_busqueda:': '¿Cuál es la principal razón por la que no buscó empleo? (Sólo en caso de no haber '
                                  'buscado empleo al concluir sus estudios de licenciatura)',
        }
        widgets = {
            'matricula': forms.HiddenInput(),
        }


class EmpleoInmediatoForm(forms.ModelForm):
    confirmacion_empleo_inmediato = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='De acuerdo a las condiciones antes mencionadas, ¿tuvo usted un trabajo?')

    class Meta:
        model = EmpleoInmediato
        fields = ('confirmacion_empleo_inmediato', 'razon_desempleo', 'rol_egresado_empleo', 'puesto_empleo_inmediato',
                  'tamano_empresa_inmediata',
                  'nombre_empleo_inmediato', 'nombre_jefe_supervisor', 'telefono_empleo_inmediato',
                  'correo_empleo_inmediato', 'tipo_contratacion',
                  'regimen_juridico', 'ingreso_mensual_neto_inicio', 'horas_laboral_semanales', 'duracion_trabajo',
                  'coincidencia_estudios_trabajo',
                  'sector_economico',)
        labels = {
            'matricula': MATRICULA,
            'confirmacion_empleo_inmediato': 'De acuerdo a las condiciones antes mencionadas, ¿tuvo usted un trabajo?',
            'razon_desempleo': 'Si respondió negativamente a la pregunta anterior, señale la razón principal por la '
                               'que no tenía trabajo (Puede omitir las demás preguntas):',
            'rol_egresado_empleo': 'En este trabajo, usted era:',
            'puesto_empleo_inmediato': 'El puesto inicial que ocupó era',
            'tamano_empresa_inmediata': 'El tamaño de la empresa/institución era',
            'nombre_empleo_inmediato': 'Favor de proporcionar el nombre de la empresa/institución:',
            'nombre_jefe_supervisor': 'Favor de propocionar el nombre del jefe/supervisor inmediato superior:',
            'telefono_empleo_inmediato': 'Favor de proporcionar un número telefónico de contacto de la '
                                         'empresa/institución:',
            'correo_empleo_inmediato': 'Favor de proporcionar un correo electrónico de contacto de la '
                                       'empresa/institución:',
            'tipo_contratacion': 'Señale el tipo de contratación que usted tenía:',
            'regimen_juridico': 'El régimen jurídico de la empresa/institución en que trabajaba era',
            'ingreso_mensual_neto_inicio': 'Indique su ingreso mensual neto al inicio (incluyendo bonos y prestaciones)',
            'horas_laboral_semanales': 'Número de horas en promedio que laboraba a la semana',
            'duracion_trabajo': 'Su duración en el trabajo (en meses) fue',
            'coincidencia_estudios_trabajo': '¿En qué medida coincidía su actividad laboral con los estudios de '
                                             'licenciatura?',
            'sector_economico': 'El sector económico de la empresa o institución en que trabajaba era (vea NOTA):',

        }
        widgets = {
            'matricula': forms.HiddenInput(),
            'ingreso_mensual_neto_inicio': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'horas_laboral_semanales': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'duracion_trabajo': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nombre_empleo_inmediato': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'nombre_jefe_supervisor': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'telefono_empleo_inmediato': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'correo_empleo_inmediato': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class EmpresaForm(forms.ModelForm):
    confirmacion_empleo_empresa = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=SI_NO_CHOICES_NUMERIC,
        label='¿Trabaja usted actualmente? (En caso de responder negativamente, sólo conteste la siguiente pregunta y '
              'omita el resto)')

    razon_desempleo_empresa = forms.ChoiceField(
        label='Señale la razón que usted considere más importante por la cual no se encuentra trabajando actualmente:',
        widget=forms.Select,
        choices=RAZON_NO_BUSQUEDA_EMPLEO,
        required=False)

    class Meta:
        model = Empresa
        fields = (
            'confirmacion_empleo_empresa', 'razon_desempleo_empresa', 'nombre_empresa', 'calle_empresa',
            'colonia_empresa',
            'num_empresa', 'codigo_postal',
            'id_estado', 'id_municipio', 'rol_egresado_empresa', 'actividad_egresado_empresa', 'puesto',
            'tamanio_empresa',
            'tipo_contratacion', 'regimen_juridico',
            'ingresomensual_neto', 'horas_laborales', 'duracion_empresa_meses', 'medida_coincidencia_labestudios',
            'medio_obtencion_empresa',
            'sector_economico')
        labels = {
            'matricula': MATRICULA,
            'razon_desempleo_empresa': 'Señale la razón que usted considere más importante por la cual no se '
                                       'encuentra trabajando actualmente:',
            'nombre_empresa': 'Nombre de la empresa/institución en que trabaja:',
            'calle_empresa': 'Calle:',
            'colonia_empresa': 'Colonia:',
            'num_empresa': 'Número:',
            'codigo_postal': 'CP:',
            'id_estado': 'Estado:',
            'id_municipio': 'Municipio:',
            'rol_egresado_empresa': 'En este trabajo usted es:',
            'actividad_egresado_empresa': 'Señale la principal actividad que usted desempeña:',
            'puesto': 'El puesto que ocupa actualmente es:',
            'tamanio_empresa': 'El tamaño de la empresa/institución donde labora actualmente es:',
            'tipo_contratacion': 'Señale el tipo de contratación que usted tiene:',
            'regimen_juridico': 'Señale el régimen jurídico de la empresa/institución en que trabaja:',
            'ingresomensual_neto': 'Indique su ingreso mensual neto actual (incluyendo bonos y prestaciones):',
            'horas_laborales': 'Número de horas en promedio que labora a la semana:',
            'duracion_empresa_meses': 'Su duración en este trabajo ha sido (en meses):',
            'medida_coincidencia_labestudios': '¿En qué medida coincide su actividad laboral con los estudios de '
                                               'licenciatura?',
            'medio_obtencion_empresa': 'Señale el principal medio a través del cual encontró su trabajo actual:',
            'sector_economico': 'Señale el sector económico de la empresa o institución en que trabaja (vea NOTA):',
        }
        widgets = {
            'matricula': forms.HiddenInput(),
            'nombre_empresa': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'calle_empresa': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'colonia_empresa': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'num_empresa': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'codigo_postal': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'ingresomensual_neto': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'horas_laborales': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'duracion_empresa_meses': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }


class DesempenioRecomendacionesForm(forms.ModelForm):
    class Meta:
        model = DesempenioRecomendaciones
        fields = ('nivel_satisfaccion', 'grado_exigencia', 'nivel_formacion', 'modificaciones_planest',
                  'opinion_orgainst')
        labels = {
            'matricula': MATRICULA,
            'nivel_satisfaccion': '¿Qué tan satisfecho está usted con los conocimientos adquiridos durante sus '
                                  'estudios de licenciatura?',
            'grado_exigencia': 'De acuerdo con su experiencia laboral actual y la(s) actividad (es) que desarrolla, '
                               'indíquenos, por favor, cuál es el grado de exigencia que enfrenta en aspectos como: '
                               'Conocimientos generales de la disciplina, Conocimiento de lenguas extranjeras, etc',
            'nivel_formacion': '¿En qué medida la formación de licenciatura lo preparó para el campo laboral?',
            'modificaciones_planest': '¿Qué modificaciones sugeriría al plan de estudios que usted cursó?',
            'opinion_orgainst': '¿Cuál sería su opinión acerca de la organización institucional en donde curso la '
                                'licenciatura?',
        }
        widgets = {
            'matricula': forms.HiddenInput(),
            'modificaciones_planest': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
            'opinion_orgainst': TextInput(attrs={'placeholder': '', 'class': 'form-control'}),
        }
