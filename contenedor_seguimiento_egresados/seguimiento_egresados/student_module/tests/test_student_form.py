from student_module.forms import SignupUserForm
from django.test import TestCase


class TestSignUpUserForm(TestCase):
    def test_signup_render(self):
        signup_fields = dict(username='S18012193', first_name='Alexis Alvarez')
        signup_form = SignupUserForm(signup_fields)

        self.assertEqual(signup_form.is_valid(), False)
        print(signup_form.errors.as_json())
        self.assertEqual(signup_form.cleaned_data, signup_fields)

    def test_signup_is_valid(self):
        signup_form = SignupUserForm()
        print(signup_form.fields)
