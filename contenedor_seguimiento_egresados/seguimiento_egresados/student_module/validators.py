import datetime
import re

from django.core.validators import RegexValidator

born_date_validate = RegexValidator(regex=r'^(1\d|[2-3]\d|4[0-5])-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$',
                                    message='La fecha de nacimiento debe ser entre 20 - 40 años.')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Sólo se permiten caracteres alfanuméricos.')
just_number = RegexValidator(r'^\d+$', 'Sólo se permiten números.')
only_decimals = RegexValidator(r'^[0-9]+(\.[0-9]{1,4})?$', 'Sólo se permiten números con el formato: X.XX')
just_letters = RegexValidator(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ]+(?: [a-zA-ZñÑáéíóúÁÉÍÓÚ]+)*$', 'Sólo se permiten letras')
just_letters_blank = RegexValidator(regex=re.compile(r'^[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+(?: [a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+)*$'),
                                    message='El nombre solo debe contener letras y un espacio entre palabras')
just_letters_numbers = RegexValidator(
    regex=re.compile(r'^[a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]+( [a-zA-ZñÑáéíóúÁÉÍÓÚ0-9]+)*$'),
    message='El nombre solo debe contener letras, números y un espacio entre palabras'
)
only_email = RegexValidator(r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$',
                            'Sólo se permiten direcciones de e-mail válidas.')
only_postal_code_mx = RegexValidator(r'^\d{5}$', 'Sólo se permiten códigos postales válidos.')
only_phone_number_mx = RegexValidator(r'^\d{10}$', 'Sólo se permiten números de teléfono de 10 dígitos.')
MAX_YEAR = datetime.date.today().year - 4
