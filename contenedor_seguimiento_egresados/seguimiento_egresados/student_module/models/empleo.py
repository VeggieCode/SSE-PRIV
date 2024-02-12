from django.db import models
from django.db.models import DO_NOTHING
from student_module.validators import just_number, alphanumeric, only_phone_number_mx, only_email, only_postal_code_mx

SI_NO_CHOICES_NUMERIC = ((1, "Sí"), (0, "No"),)
MEDIDA_COINCIDENCIA_ESTUDIOS = (
    ('', 'Seleccione...'), ('Nula coincidencia', 'Nula coincidencia'), ('Baja coincidencia', 'Baja coincidencia'),
    ('Mediana coincidencia', 'Mediana coincidencia'), ('Alta coincidencia', 'Alta coincidencia'))
TIEMPO_CONSEGUIR_EMPLEO = (('', 'Seleccione...'), ('Menos de seis meses', 'Menos de seis meses'),
                           ('De seis meses a un año', 'De seis meses a un año'),
                           ('De 1 año 1 día a 2 años', 'De 1 año 1 día a 2 años'), ('Más de 2 años', 'Más de 2 años'),
                           ('No encontré y seguí en el mismo empleo', 'No encontré y seguí en el mismo empleo'),
                           ('No encontré empleo, quedé desocupado', 'No encontré empleo, quedé desocupado'),
                           ('Otro', 'Otro'))
DEMORA_EMPLEO = (('', 'Seleccione...'), ('Escasa experiencia laboral', 'Escasa experiencia laboral'),
                 ('La carrera es poco conocida', 'La carrera es poco conocida'),
                 ('Su situación personal se lo dificultó', 'Su situación personal se lo dificultó'),
                 ('Tenía ofertas de trabajo poco atractivas', 'Tenía ofertas de trabajo poco atractivas'),
                 ('Otro ', 'Otro'))
MEDIO_EMPLEO = (('', 'Seleccione...'), ('Bolsa de trabajo', 'Bolsa de trabajo'),
                ('Anuncio en el periódico', 'Anuncio en el periódico'),
                ('Invitación expresa de una empresa', 'Invitación expresa de una empresa'),  # O institucion
                ('Recomendación de amigos de la licenciatura', 'Recomendación de amigos de la licenciatura'),
                ('Recomendación de un profesor', 'Recomendación de un profesor'),
                ('Recomendación de un amigo o familiar', 'Recomendación de un amigo o familiar'),
                ('Relaciones hechas en empleos anteriores', 'Relaciones hechas en empleos anteriores'),
                ('Creación de un negocio de empresa, propios', 'Creación de empresa, propios'),
                # checar en cuestionario preg 53
                ('Integración a un negocio familiar', 'Integración a un negocio familiar'),
                ('Servicio social', 'Servicio social'), ('Otro', 'Otro'))
REQUISITO_FORMAL_EMPLEO = (('', 'Seleccione...'), ('Tener título de licenciatura', 'Tener título de licenciatura'),
                           ('Aprobar los exámenes de selección', 'Aprobar los exámenes de selección'),
                           ('Pasar una entrevista formal', 'Pasar una entrevista formal'))
RAZON_NO_BUSQUEDA_EMPLEO = (('', 'Seleccione...'), ('Ya tenía un trabajo', 'Ya tenía un trabajo'),
                            ('Decidí continuar estudiando', 'Decidí continuar estudiando'),
                            ('Por razones personales', 'Por razones personales'))
RAZON_DESEMPLEO = (('', 'Seleccione...'), (
    'No tengo trabajo porque no encontré, pero sigo buscando',
    'No tengo trabajo porque no encontré, pero sigo buscando'), (
                       'No tengo trabajo porque no encontré y ya no busco',
                       'No tengo trabajo porque no encontré y ya no busco'),
                   ('Estoy por incorporarme a un trabajo', 'Estoy por incorporarme a un trabajo'), (
                       'No tengo trabajo, porque decidí continuar estudiando',
                       'No tengo trabajo, porque decidí continuar estudiando'),
                   ('No necesito trabajar', 'No necesito trabajar'),
                   ('No tengo trabajo por razones de salud', 'No tengo trabajo por razones de salud'),
                   ('No tengo trabajo porque aún no lo he buscado', 'No tengo trabajo porque aún no lo he buscado'),)
ROL_EGRESADO_EMPLEO = (
    ('', 'Seleccione...'), ('Propietario', 'Propietario'), ('Trabajador Independiente', 'Trabajador Independiente'),
    ('Empleado', 'Empleado'),)
PUESTO_INICIAL = (('', 'Seleccione...'), ('Director general', 'Director general'),
                  ('Dueño o socio de empresa, despacho, rancho', 'Dueño o socio de empresa, despacho, rancho'),
                  ('Profesional independiente', 'Profesional independiente'),
                  ('Gerente/Director de área', 'Gerente/Director de área'),
                  ('Subgerente/Subdirector de área', 'Subgerente/Subdirector de área'),
                  ('Jefe de departamento', 'Jefe de departamento'), ('Ejecutivo de Cuenta', 'Ejecutivo de Cuenta'),
                  ('Jefe de oficina/sección/área', 'Jefe de oficina/sección/área'),
                  ('Empleado profesional', 'Empleado profesional'), ('Supervisor', 'Supervisor'),
                  ('Analista especializado/técnico', 'Analista especializado/técnico'),
                  ('Profesional independiente', 'Profesional independiente'),
                  ('Gerente/Director de área', 'Gerente/Director de área'),
                  ('Subgerente/Subdirector de área', 'Subgerente/Subdirector de área'),
                  ('Jefe de departamento', 'Jefe de departamento'), ('Ejecutivo de Cuenta', 'Ejecutivo de Cuenta'),
                  ('Jefe de oficina/sección/área', 'Jefe de oficina/sección/área'),
                  ('Empleado profesional', 'Empleado profesional'), ('Supervisor', 'Supervisor'),
                  ('Analista especializado/técnico', 'Analista especializado/técnico'),
                  ('Vendedor en establecimiento', 'Vendedor en establecimiento'), ('Asistente', 'Asistente'),
                  ('Ayudante', 'Ayudante'), ('Por cuenta propia no profesional', 'Por cuenta propia no profesional'),
                  ('Empleado no profesional', 'Empleado no profesional'), ('Auxiliar', 'Auxiliar'), ('Otro', 'Otro'))
TAMANIO_EMPRESA = (('', 'Seleccione...'), ('Hasta 15 empleados (Micro)', 'Hasta 15 empleados (Micro)'),
                   ('Entre 16 y 100 empleados (Pequeña)', 'Entre 16 y 100 empleados (Pequeña)'),
                   ('Entre 101 y 250 empleados (Mediana)', 'Entre 101 y 250 empleados (Mediana)'),
                   ('Más de 251 empleados (Grande)', 'Más de 251 empleados (Grande)'))
REGIMEN_JURIDICO = (('', 'Seleccione...'), ('Público', 'Público'), ('Privado', 'Privado'))
SECTOR_ECONOMICO = (('', 'Seleccione...'), ('Agrícola-ganadero, silvícola,etc', 'Agrícola-ganadero, silvícola,etc'),
                    ('Industria extractiva', 'Industria extractiva'),
                    ('Industria de la transformación', 'Industria de la transformación'),
                    ('Industria de la construcción', 'Industria de la construcción'), ('Comercio', 'Comercio'),
                    ('Servicios bancarios, financieros y seguros', 'Servicios bancarios, financieros y seguros'),
                    ('Transporte/comunicaciones', 'Transporte/comunicaciones'), ('Educación', 'Educación'),
                    ('Servicios Profesionales y Técnicos', 'Servicios Profesionales y Técnicos'),
                    ('Servicios de Salud', 'Servicios de Salud'), ('Servicios de Gobierno', 'Servicios de Gobierno'),
                    ('Otro', 'Otro'))
DEPARTAMENTOS = (('', 'Seleccione...'), ('Dirección', 'Dirección'), ('Coordinación', 'Coordinación'),
                 ('Dirección de proyectos', 'Dirección de proyectos'),
                 ('Coordinación de Proyectos', 'Coordinación de Proyectos'),
                 ('Dirección de Obras', 'Dirección de Obras'), ('Coordinación de Obras', 'Coordinación de Obras'),
                 ('Análisis de Sistemas', 'Análisis de Sistemas'), ('Planeación', 'Planeación'),
                 ('Programación', 'Programación'), ('Evaluación', 'Evaluación'), ('Supervisión', 'Supervisión'),
                 ('Mantenimiento', 'Mantenimiento'), ('Diagnóstico', 'Diagnóstico'), ('Investigación', 'Investigación'),
                 ('Análisis Financiero', 'Análisis Financiero'), ('Capacitación', 'Capacitación'),
                 ('Asesoría Especializada', 'Asesoría Especializada'), ('Consultoría', 'Consultoría'),
                 ('Asesoría Técnica', 'Asesoría Técnica'), ('Comercialización', 'Comercialización'),
                 ('Ventas', 'Ventas'), ('Desarrollo de Productos', 'Desarrollo de Productos'),
                 ('Control de Calidad', 'Control de Calidad'), ('Atención a Pacientes', 'Atención a Pacientes'),
                 ('Atención Psicológica', 'Atención Psicológica'), ('Trabajo Editorial', 'Trabajo Editorial'),
                 ('Actividades de Organización', 'Actividades de Organización'),
                 ('Actividades Administrativas', 'Actividades Administrativas'), ('Publicidad', 'Publicidad'),
                 ('Atención a Clientes', 'Atención a Clientes'), ('Otro', 'Otro'))
TIPO_CONTRATACION = (('', 'Seleccione...'), ('Por tiempo determinado', 'Por tiempo determinado'),
                     ('Por obra determinada', 'Por obra determinada'),
                     ('Por tiempo indeterminado', 'Por tiempo indeterminado'), ('Otro', 'Otro'))
NIVEL_SATISFACCION = (('', 'Seleccione...'), ('Poco satisfecho', 'Poco satisfecho'), ('Satisfecho', 'Satisfecho'),
                      ('Muy satisfecho', 'Muy satisfecho'), ('Totalmente satisfecho', 'Totalmente satisfecho'))
GRADO_EXIGENCIA = (
    ('', 'Seleccione...'), ('Ninguna exigencia', 'Ninguna exigencia '), ('Poca exigencia', 'Poca exigencia'),
    ('Moderada exigencia', 'Moderada exigencia'), ('Mucha exigencia', 'Mucha exigencia'))
NIVEL_FORMACION = (
    ('', 'Seleccione...'), ('Nada', 'Nada'), ('Poco', 'Poco'), ('En parte', 'En parte'), ('Mucho', 'Mucho'))


class EmpleoDuranteEstudios(models.Model):
    # id_empleo_durante_estudios = models.IntegerField(primary_key=True)
    confirmacion_empleo = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    coincidencia_estudios_trabajo = models.CharField(max_length=45, choices=MEDIDA_COINCIDENCIA_ESTUDIOS, null=True,
                                                     blank=True)
    horas_laboradas_semanales = models.CharField(max_length=45, blank=True, null=True, validators=[just_number])
    matricula = models.ForeignKey('Student', on_delete=DO_NOTHING, db_column='matricula', validators=[alphanumeric],
                                  null=True)


class BusquedaEmpleo(models.Model):
    # id_busqueda_empleo = models.IntegerField(primary_key=True)
    confirmacion_empleo_egreso = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    confirmacion_busqueda_empleo = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    tiempo_obtencion_empleo = models.CharField(max_length=45, blank=True, null=True, choices=TIEMPO_CONSEGUIR_EMPLEO)
    opinion_demora_empleo = models.CharField(max_length=45, blank=True, null=True, choices=DEMORA_EMPLEO)
    medio_obtencion_empleo = models.CharField(max_length=45, blank=True, null=True, choices=MEDIO_EMPLEO)
    requisito_formal = models.CharField(max_length=45, blank=True, null=True, choices=REQUISITO_FORMAL_EMPLEO)
    razon_no_busqueda = models.CharField(max_length=45, blank=True, null=True, choices=RAZON_NO_BUSQUEDA_EMPLEO)
    matricula = models.ForeignKey('Student', on_delete=DO_NOTHING, db_column='matricula', validators=[alphanumeric],
                                  null=True)


class EmpleoInmediato(models.Model):
    # id_empleo_inmediato = models.IntegerField(primary_key=True)
    confirmacion_empleo_inmediato = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    rol_egresado_empleo = models.CharField(max_length=45, blank=True, null=True, choices=ROL_EGRESADO_EMPLEO)
    puesto_empleo_inmediato = models.CharField(max_length=45, choices=PUESTO_INICIAL, blank=True, null=True)
    tamano_empresa_inmediata = models.CharField(max_length=45, choices=TAMANIO_EMPRESA, null=True, blank=True)
    nombre_empleo_inmediato = models.CharField(max_length=45, blank=True, null=True)
    nombre_jefe_supervisor = models.CharField(max_length=45, blank=True, null=True)
    telefono_empleo_inmediato = models.CharField(max_length=10, blank=True, null=True,
                                                 validators=[only_phone_number_mx])
    correo_empleo_inmediato = models.CharField(max_length=45, blank=True, null=True, validators=[only_email])
    tipo_contratacion = models.CharField(max_length=45, blank=True, null=True, choices=TIPO_CONTRATACION)
    regimen_juridico = models.CharField(max_length=45, choices=REGIMEN_JURIDICO, null=True, blank=True)
    ingreso_mensual_neto_inicio = models.CharField(db_column='ingreso_mensual_neto_Inicio', max_length=45, blank=True,
                                                   null=True)  # Field name made lowercase.
    horas_laboral_semanales = models.CharField(max_length=45, blank=True, null=True, validators=[just_number])
    duracion_trabajo = models.IntegerField(blank=True, null=True, validators=[just_number])
    coincidencia_estudios_trabajo = models.CharField(max_length=45, blank=True, null=True,
                                                     choices=MEDIDA_COINCIDENCIA_ESTUDIOS)
    sector_economico = models.CharField(max_length=45, choices=SECTOR_ECONOMICO, null=True, blank=True)
    razon_desempleo = models.CharField(max_length=55, choices=RAZON_DESEMPLEO, null=True, blank=True)
    matricula = models.ForeignKey('Student', on_delete=DO_NOTHING, db_column='matricula', validators=[alphanumeric],
                                  blank=True, null=True)


# Model Empresa y derivados (EmpresaForm y empresa en BD) hacen corresponden a la sección de Empleo Actual.
# (no tengo idea por qué razón decidieron nombrarla Empresa)
class Empresa(models.Model):
    # id_empresa = models.IntegerField(primary_key=True)
    confirmacion_empleo_empresa = models.IntegerField(blank=True, null=True, choices=SI_NO_CHOICES_NUMERIC)
    razon_desempleo_empresa = models.CharField(max_length=55, choices=RAZON_DESEMPLEO, null=True, blank=True)
    nombre_empresa = models.CharField(max_length=45, blank=True, null=True)
    calle_empresa = models.CharField(max_length=45, blank=True, null=True)
    colonia_empresa = models.CharField(max_length=45, blank=True, null=True)
    num_empresa = models.CharField(max_length=45, blank=True, null=True, validators=[alphanumeric])
    codigo_postal = models.CharField(max_length=45, blank=True, null=True, validators=[only_postal_code_mx])
    id_estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='id_estado', blank=True, null=True)
    id_municipio = models.ForeignKey('Municipios', models.DO_NOTHING, db_column='id_municipio', blank=True, null=True)
    rol_egresado_empresa = models.CharField(max_length=45, blank=True, null=True, choices=ROL_EGRESADO_EMPLEO)
    puesto = models.CharField(max_length=45, choices=PUESTO_INICIAL, null=True, blank=True)
    actividad_egresado_empresa = models.CharField(max_length=45, choices=DEPARTAMENTOS, null=True, blank=True)
    tamanio_empresa = models.CharField(max_length=45, choices=TAMANIO_EMPRESA, null=True, blank=True)
    tipo_contratacion = models.CharField(max_length=45, choices=TIPO_CONTRATACION, null=True, blank=True)
    regimen_juridico = models.CharField(max_length=45, choices=REGIMEN_JURIDICO, null=True, blank=True)
    ingresomensual_neto = models.CharField(max_length=45, blank=True, null=True)
    horas_laborales = models.CharField(max_length=45, blank=True, null=True, validators=[just_number])
    duracion_empresa_meses = models.IntegerField(blank=True, null=True, validators=[just_number])
    medida_coincidencia_labestudios = models.CharField(max_length=45, choices=MEDIDA_COINCIDENCIA_ESTUDIOS, null=True,
                                                       blank=True)
    sector_economico = models.CharField(max_length=45, choices=SECTOR_ECONOMICO, null=True, blank=True)
    medio_obtencion_empresa = models.CharField(max_length=45, blank=True, null=True, choices=MEDIO_EMPLEO)
    matricula = models.ForeignKey('Student', on_delete=DO_NOTHING, db_column='matricula', validators=[alphanumeric],
                                  null=True)


class DesempenioRecomendaciones(models.Model):
    # id_desempenio_recomendaciones = models.IntegerField(primary_key=True)
    nivel_satisfaccion = models.CharField(max_length=45, choices=NIVEL_SATISFACCION, null=True, blank=True)
    grado_exigencia = models.CharField(max_length=45, choices=GRADO_EXIGENCIA, null=True, blank=True)
    nivel_formacion = models.CharField(max_length=45, choices=NIVEL_FORMACION, null=True, blank=True)
    modificaciones_planest = models.CharField(max_length=45, blank=True, null=True)
    opinion_orgainst = models.CharField(max_length=45, blank=True, null=True)
    matricula = models.ForeignKey('Student', on_delete=DO_NOTHING, db_column='matricula',
                                  validators=[alphanumeric], null=True)
