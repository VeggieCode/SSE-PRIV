# Generated by Django 4.1.7 on 2023-03-29 18:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
                ('correo_uv', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
            ],
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_municipio', models.CharField(max_length=100)),
                ('id_estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=45, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('', 'Seleccione sexo'), ('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Prefiero no decirlo')], max_length=10, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('fecha_ingreso_lic', models.DateField(blank=True, null=True)),
                ('licenciatura_fei', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Estadística', 'Estadística'), ('Ingeniería de Software', 'Ingeniería de Software'), ('Tecnologías Computacionales ', 'Tecnologías Computacionales'), ('Redes y Servicios de Cómputo ', 'Redes y Servicios de Cómputo')], max_length=100, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
                ('correo_uv', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
                ('celular', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Sólo se permiten números de teléfono de 10 dígitos.')])),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Sólo se permiten números de teléfono de 10 dígitos.')])),
                ('twitter', models.CharField(blank=True, max_length=45, null=True)),
                ('facebook', models.CharField(blank=True, max_length=45, null=True)),
                ('linkedin', models.CharField(blank=True, default='', max_length=45)),
                ('calle', models.CharField(blank=True, max_length=45, null=True)),
                ('colonia', models.CharField(blank=True, max_length=45, null=True)),
                ('numero', models.CharField(blank=True, max_length=10, null=True)),
                ('codigo_postal', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator('^\\d{5}$', 'Sólo se permiten códigos postales válidos.')])),
                ('pre_egreso_abierto', models.BooleanField(default=False)),
                ('estado', models.CharField(blank=True, max_length=50, null=True)),
                ('municipio', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeleccionCarrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primera_opcion_carrera', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('eleccion_tipo_institucion', models.CharField(blank=True, choices=[('', 'Seleccione el tipo de institución'), ('Universidad Pública', 'Universidad Pública'), ('Universidad Privada', 'Universidad Privada'), ('Instituto Tecnológico y/o Politécnico Público', 'Instituto Tecnológico y/o Politécnico Público'), ('Instituto Tecnológico Privado', 'Instituto Tecnológico Privado'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('primera_eleccion_institucion', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('primera_eleccion_nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('razon_eleccion_institucion', models.CharField(blank=True, max_length=45, null=True)),
                ('razon_eleccion_carrera', models.CharField(blank=True, max_length=45, null=True)),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='Licenciatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campus', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]*$')])),
                ('nombre_carrera', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Estadística', 'Estadística'), ('Ingeniería de Software', 'Ingeniería de Software'), ('Tecnologías Computacionales ', 'Tecnologías Computacionales'), ('Redes y Servicios de Cómputo ', 'Redes y Servicios de Cómputo')], max_length=60)),
                ('anio_pestudios', models.CharField(blank=True, max_length=45, null=True)),
                ('anio_inicio', models.CharField(blank=True, max_length=25, null=True)),
                ('anio_fin', models.CharField(blank=True, max_length=25, null=True)),
                ('org_ss', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha_inicioss', models.DateField(blank=True, null=True)),
                ('fecha_finss', models.DateField(blank=True, null=True)),
                ('titulado', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Sí', 'Titulado'), ('No', 'No titulado'), ('En proceso', 'En proceso')], max_length=10, null=True)),
                ('promedio_final', models.FloatField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+(\\.[0-9]{1,4})?$', 'Sólo se permiten números con el formato: X.XX')])),
                ('tipo_inscripcion', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Tiempo completo', 'Tiempo completo'), ('Tiempo parcial', 'Tiempo parcial')], max_length=25, null=True)),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmacion_empleo_empresa', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('razon_desempleo_empresa', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('No tengo trabajo porque no encontré, pero sigo buscando', 'No tengo trabajo porque no encontré, pero sigo buscando'), ('No tengo trabajo porque no encontré y ya no busco', 'No tengo trabajo porque no encontré y ya no busco'), ('Estoy por incorporarme a un trabajo', 'Estoy por incorporarme a un trabajo'), ('No tengo trabajo, porque decidí continuar estudiando', 'No tengo trabajo, porque decidí continuar estudiando'), ('No necesito trabajar', 'No necesito trabajar'), ('No tengo trabajo por razones de salud', 'No tengo trabajo por razones de salud'), ('No tengo trabajo porque aún no lo he buscado', 'No tengo trabajo porque aún no lo he buscado')], max_length=55, null=True)),
                ('nombre_empresa', models.CharField(blank=True, max_length=45, null=True)),
                ('calle_empresa', models.CharField(blank=True, max_length=45, null=True)),
                ('colonia_empresa', models.CharField(blank=True, max_length=45, null=True)),
                ('num_empresa', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
                ('codigo_postal', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^\\d{5}$', 'Sólo se permiten códigos postales válidos.')])),
                ('rol_egresado_empresa', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Propietario', 'Propietario'), ('Trabajador Independiente', 'Trabajador Independiente'), ('Empleado', 'Empleado')], max_length=45, null=True)),
                ('puesto', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Director general', 'Director general'), ('Dueño o socio de empresa, despacho, rancho', 'Dueño o socio de empresa, despacho, rancho'), ('Profesional independiente', 'Profesional independiente'), ('Gerente/Director de área', 'Gerente/Director de área'), ('Subgerente/Subdirector de área', 'Subgerente/Subdirector de área'), ('Jefe de departamento', 'Jefe de departamento'), ('Ejecutivo de Cuenta', 'Ejecutivo de Cuenta'), ('Jefe de oficina/sección/área', 'Jefe de oficina/sección/área'), ('Empleado profesional', 'Empleado profesional'), ('Supervisor', 'Supervisor'), ('Analista especializado/técnico', 'Analista especializado/técnico'), ('Profesional independiente', 'Profesional independiente'), ('Gerente/Director de área', 'Gerente/Director de área'), ('Subgerente/Subdirector de área', 'Subgerente/Subdirector de área'), ('Jefe de departamento', 'Jefe de departamento'), ('Ejecutivo de Cuenta', 'Ejecutivo de Cuenta'), ('Jefe de oficina/sección/área', 'Jefe de oficina/sección/área'), ('Empleado profesional', 'Empleado profesional'), ('Supervisor', 'Supervisor'), ('Analista especializado/técnico', 'Analista especializado/técnico'), ('Vendedor en establecimiento', 'Vendedor en establecimiento'), ('Asistente', 'Asistente'), ('Ayudante', 'Ayudante'), ('Por cuenta propia no profesional', 'Por cuenta propia no profesional'), ('Empleado no profesional', 'Empleado no profesional'), ('Auxiliar', 'Auxiliar'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('actividad_egresado_empresa', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Dirección', 'Dirección'), ('Coordinación', 'Coordinación'), ('Dirección de proyectos', 'Dirección de proyectos'), ('Coordinación de Proyectos', 'Coordinación de Proyectos'), ('Dirección de Obras', 'Dirección de Obras'), ('Coordinación de Obras', 'Coordinación de Obras'), ('Análisis de Sistemas', 'Análisis de Sistemas'), ('Planeación', 'Planeación'), ('Programación', 'Programación'), ('Evaluación', 'Evaluación'), ('Supervisión', 'Supervisión'), ('Mantenimiento', 'Mantenimiento'), ('Diagnóstico', 'Diagnóstico'), ('Investigación', 'Investigación'), ('Análisis Financiero', 'Análisis Financiero'), ('Capacitación', 'Capacitación'), ('Asesoría Especializada', 'Asesoría Especializada'), ('Consultoría', 'Consultoría'), ('Asesoría Técnica', 'Asesoría Técnica'), ('Comercialización', 'Comercialización'), ('Ventas', 'Ventas'), ('Desarrollo de Productos', 'Desarrollo de Productos'), ('Control de Calidad', 'Control de Calidad'), ('Atención a Pacientes', 'Atención a Pacientes'), ('Atención Psicológica', 'Atención Psicológica'), ('Trabajo Editorial', 'Trabajo Editorial'), ('Actividades de Organización', 'Actividades de Organización'), ('Actividades Administrativas', 'Actividades Administrativas'), ('Publicidad', 'Publicidad'), ('Atención a Clientes', 'Atención a Clientes'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('tamanio_empresa', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Hasta 15 empleados (Micro)', 'Hasta 15 empleados (Micro)'), ('Entre 16 y 100 empleados (Pequeña)', 'Entre 16 y 100 empleados (Pequeña)'), ('Entre 101 y 250 empleados (Mediana)', 'Entre 101 y 250 empleados (Mediana)'), ('Más de 251 empleados (Grande)', 'Más de 251 empleados (Grande)')], max_length=45, null=True)),
                ('tipo_contratacion', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Por tiempo determinado', 'Por tiempo determinado'), ('Por obra determinada', 'Por obra determinada'), ('Por tiempo indeterminado', 'Por tiempo indeterminado'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('regimen_juridico', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Público', 'Público'), ('Privado', 'Privado')], max_length=45, null=True)),
                ('ingresomensual_neto', models.CharField(blank=True, max_length=45, null=True)),
                ('horas_laborales', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Sólo se permiten números.')])),
                ('duracion_empresa_meses', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Sólo se permiten números.')])),
                ('medida_coincidencia_labestudios', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Nula coincidencia', 'Nula coincidencia'), ('Baja coincidencia', 'Baja coincidencia'), ('Mediana coincidencia', 'Mediana coincidencia'), ('Alta coincidencia', 'Alta coincidencia')], max_length=45, null=True)),
                ('sector_economico', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Agrícola-ganadero, silvícola,etc', 'Agrícola-ganadero, silvícola,etc'), ('Industria extractiva', 'Industria extractiva'), ('Industria de la transformación', 'Industria de la transformación'), ('Industria de la construcción', 'Industria de la construcción'), ('Comercio', 'Comercio'), ('Servicios bancarios, financieros y seguros', 'Servicios bancarios, financieros y seguros'), ('Transporte/comunicaciones', 'Transporte/comunicaciones'), ('Educación', 'Educación'), ('Servicios Profesionales y Técnicos', 'Servicios Profesionales y Técnicos'), ('Servicios de Salud', 'Servicios de Salud'), ('Servicios de Gobierno', 'Servicios de Gobierno'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('medio_obtencion_empresa', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Bolsa de trabajo', 'Bolsa de trabajo'), ('Anuncio en el periódico', 'Anuncio en el periódico'), ('Invitación expresa de una empresa', 'Invitación expresa de una empresa'), ('Recomendación de amigos de la licenciatura', 'Recomendación de amigos de la licenciatura'), ('Recomendación de un profesor', 'Recomendación de un profesor'), ('Recomendación de un amigo o familiar', 'Recomendación de un amigo o familiar'), ('Relaciones hechas en empleos anteriores', 'Relaciones hechas en empleos anteriores'), ('Creación de un negocio de empresa, propios', 'Creación de empresa, propios'), ('Integración a un negocio familiar', 'Integración a un negocio familiar'), ('Servicio social', 'Servicio social'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('id_estado', models.ForeignKey(blank=True, db_column='id_estado', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.estados')),
                ('id_municipio', models.ForeignKey(blank=True, db_column='id_municipio', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.municipios')),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='EmpleoInmediato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmacion_empleo_inmediato', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('rol_egresado_empleo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Propietario', 'Propietario'), ('Trabajador Independiente', 'Trabajador Independiente'), ('Empleado', 'Empleado')], max_length=45, null=True)),
                ('puesto_empleo_inmediato', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Director general', 'Director general'), ('Dueño o socio de empresa, despacho, rancho', 'Dueño o socio de empresa, despacho, rancho'), ('Profesional independiente', 'Profesional independiente'), ('Gerente/Director de área', 'Gerente/Director de área'), ('Subgerente/Subdirector de área', 'Subgerente/Subdirector de área'), ('Jefe de departamento', 'Jefe de departamento'), ('Ejecutivo de Cuenta', 'Ejecutivo de Cuenta'), ('Jefe de oficina/sección/área', 'Jefe de oficina/sección/área'), ('Empleado profesional', 'Empleado profesional'), ('Supervisor', 'Supervisor'), ('Analista especializado/técnico', 'Analista especializado/técnico'), ('Profesional independiente', 'Profesional independiente'), ('Gerente/Director de área', 'Gerente/Director de área'), ('Subgerente/Subdirector de área', 'Subgerente/Subdirector de área'), ('Jefe de departamento', 'Jefe de departamento'), ('Ejecutivo de Cuenta', 'Ejecutivo de Cuenta'), ('Jefe de oficina/sección/área', 'Jefe de oficina/sección/área'), ('Empleado profesional', 'Empleado profesional'), ('Supervisor', 'Supervisor'), ('Analista especializado/técnico', 'Analista especializado/técnico'), ('Vendedor en establecimiento', 'Vendedor en establecimiento'), ('Asistente', 'Asistente'), ('Ayudante', 'Ayudante'), ('Por cuenta propia no profesional', 'Por cuenta propia no profesional'), ('Empleado no profesional', 'Empleado no profesional'), ('Auxiliar', 'Auxiliar'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('tamano_empresa_inmediata', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Hasta 15 empleados (Micro)', 'Hasta 15 empleados (Micro)'), ('Entre 16 y 100 empleados (Pequeña)', 'Entre 16 y 100 empleados (Pequeña)'), ('Entre 101 y 250 empleados (Mediana)', 'Entre 101 y 250 empleados (Mediana)'), ('Más de 251 empleados (Grande)', 'Más de 251 empleados (Grande)')], max_length=45, null=True)),
                ('nombre_empleo_inmediato', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre_jefe_supervisor', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono_empleo_inmediato', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator('^\\d{10}$', 'Sólo se permiten números de teléfono de 10 dígitos.')])),
                ('correo_empleo_inmediato', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^([a-zA-Z0-9_\\-\\.]+)@([a-zA-Z0-9_\\-\\.]+)\\.([a-zA-Z]{2,5})$', 'Sólo se permiten direcciones de e-mail válidas.')])),
                ('tipo_contratacion', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Por tiempo determinado', 'Por tiempo determinado'), ('Por obra determinada', 'Por obra determinada'), ('Por tiempo indeterminado', 'Por tiempo indeterminado'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('regimen_juridico', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Público', 'Público'), ('Privado', 'Privado')], max_length=45, null=True)),
                ('ingreso_mensual_neto_inicio', models.CharField(blank=True, db_column='ingreso_mensual_neto_Inicio', max_length=45, null=True)),
                ('horas_laboral_semanales', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Sólo se permiten números.')])),
                ('duracion_trabajo', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Sólo se permiten números.')])),
                ('coincidencia_estudios_trabajo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Nula coincidencia', 'Nula coincidencia'), ('Baja coincidencia', 'Baja coincidencia'), ('Mediana coincidencia', 'Mediana coincidencia'), ('Alta coincidencia', 'Alta coincidencia')], max_length=45, null=True)),
                ('sector_economico', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Agrícola-ganadero, silvícola,etc', 'Agrícola-ganadero, silvícola,etc'), ('Industria extractiva', 'Industria extractiva'), ('Industria de la transformación', 'Industria de la transformación'), ('Industria de la construcción', 'Industria de la construcción'), ('Comercio', 'Comercio'), ('Servicios bancarios, financieros y seguros', 'Servicios bancarios, financieros y seguros'), ('Transporte/comunicaciones', 'Transporte/comunicaciones'), ('Educación', 'Educación'), ('Servicios Profesionales y Técnicos', 'Servicios Profesionales y Técnicos'), ('Servicios de Salud', 'Servicios de Salud'), ('Servicios de Gobierno', 'Servicios de Gobierno'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('razon_desempleo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('No tengo trabajo porque no encontré, pero sigo buscando', 'No tengo trabajo porque no encontré, pero sigo buscando'), ('No tengo trabajo porque no encontré y ya no busco', 'No tengo trabajo porque no encontré y ya no busco'), ('Estoy por incorporarme a un trabajo', 'Estoy por incorporarme a un trabajo'), ('No tengo trabajo, porque decidí continuar estudiando', 'No tengo trabajo, porque decidí continuar estudiando'), ('No necesito trabajar', 'No necesito trabajar'), ('No tengo trabajo por razones de salud', 'No tengo trabajo por razones de salud'), ('No tengo trabajo porque aún no lo he buscado', 'No tengo trabajo porque aún no lo he buscado')], max_length=55, null=True)),
                ('matricula', models.ForeignKey(blank=True, db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='EmpleoDuranteEstudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmacion_empleo', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('coincidencia_estudios_trabajo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Nula coincidencia', 'Nula coincidencia'), ('Baja coincidencia', 'Baja coincidencia'), ('Mediana coincidencia', 'Mediana coincidencia'), ('Alta coincidencia', 'Alta coincidencia')], max_length=45, null=True)),
                ('horas_laboradas_semanales', models.CharField(blank=True, max_length=45, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Sólo se permiten números.')])),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='DesempenioRecomendaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_satisfaccion', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Poco satisfecho', 'Poco satisfecho'), ('Satisfecho', 'Satisfecho'), ('Muy satisfecho', 'Muy satisfecho'), ('Totalmente satisfecho', 'Totalmente satisfecho')], max_length=45, null=True)),
                ('grado_exigencia', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Ninguna exigencia', 'Ninguna exigencia '), ('Poca exigencia', 'Poca exigencia'), ('Moderada exigencia', 'Moderada exigencia'), ('Mucha exigencia', 'Mucha exigencia')], max_length=45, null=True)),
                ('nivel_formacion', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Nada', 'Nada'), ('Poco', 'Poco'), ('En parte', 'En parte'), ('Mucho', 'Mucho')], max_length=45, null=True)),
                ('modificaciones_planest', models.CharField(blank=True, max_length=45, null=True)),
                ('opinion_orgainst', models.CharField(blank=True, max_length=45, null=True)),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='ContinuacionEstudios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_estudio_continuacion', models.CharField(blank=True, choices=[('', 'Seleccione el tipo de continuación de estudios...'), ('Cursos cortos ', 'Cursos cortos'), ('Diplomado ', 'Diplomado'), ('Especialización', 'Especialización'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('institucion', models.CharField(blank=True, choices=[('', 'Seleccione el tipo de institución'), ('Pública ', 'Pública'), ('Privada', 'Privada'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('nombre_programa', models.CharField(blank=True, max_length=45, null=True)),
                ('conclusion_estudios', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('obtencion_grado', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('duracion_estudios_meses', models.IntegerField(blank=True, null=True, validators=[django.core.validators.RegexValidator('^\\d+$', 'Sólo se permiten números.')])),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
        migrations.CreateModel(
            name='BusquedaEmpleo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirmacion_empleo_egreso', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('confirmacion_busqueda_empleo', models.IntegerField(blank=True, choices=[(1, 'Sí'), (0, 'No')], null=True)),
                ('tiempo_obtencion_empleo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Menos de seis meses', 'Menos de seis meses'), ('De seis meses a un año', 'De seis meses a un año'), ('De 1 año 1 día a 2 años', 'De 1 año 1 día a 2 años'), ('Más de 2 años', 'Más de 2 años'), ('No encontré y seguí en el mismo empleo', 'No encontré y seguí en el mismo empleo'), ('No encontré empleo, quedé desocupado', 'No encontré empleo, quedé desocupado'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('opinion_demora_empleo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Escasa experiencia laboral', 'Escasa experiencia laboral'), ('La carrera es poco conocida', 'La carrera es poco conocida'), ('Su situación personal se lo dificultó', 'Su situación personal se lo dificultó'), ('Tenía ofertas de trabajo poco atractivas', 'Tenía ofertas de trabajo poco atractivas'), ('Otro ', 'Otro')], max_length=45, null=True)),
                ('medio_obtencion_empleo', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Bolsa de trabajo', 'Bolsa de trabajo'), ('Anuncio en el periódico', 'Anuncio en el periódico'), ('Invitación expresa de una empresa', 'Invitación expresa de una empresa'), ('Recomendación de amigos de la licenciatura', 'Recomendación de amigos de la licenciatura'), ('Recomendación de un profesor', 'Recomendación de un profesor'), ('Recomendación de un amigo o familiar', 'Recomendación de un amigo o familiar'), ('Relaciones hechas en empleos anteriores', 'Relaciones hechas en empleos anteriores'), ('Creación de un negocio de empresa, propios', 'Creación de empresa, propios'), ('Integración a un negocio familiar', 'Integración a un negocio familiar'), ('Servicio social', 'Servicio social'), ('Otro', 'Otro')], max_length=45, null=True)),
                ('requisito_formal', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Tener título de licenciatura', 'Tener título de licenciatura'), ('Aprobar los exámenes de selección', 'Aprobar los exámenes de selección'), ('Pasar una entrevista formal', 'Pasar una entrevista formal')], max_length=45, null=True)),
                ('razon_no_busqueda', models.CharField(blank=True, choices=[('', 'Seleccione...'), ('Ya tenía un trabajo', 'Ya tenía un trabajo'), ('Decidí continuar estudiando', 'Decidí continuar estudiando'), ('Por razones personales', 'Por razones personales')], max_length=45, null=True)),
                ('matricula', models.ForeignKey(db_column='matricula', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='student_module.student', validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')])),
            ],
        ),
    ]
