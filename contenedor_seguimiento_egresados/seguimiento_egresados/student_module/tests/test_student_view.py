from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

LOGIN_VIEWNAME: str = 'student_module:login'


class TestStudentViews(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='S18012191', password='beethoven123')
        self.user.save()
        self.client = Client()

    def test_login_view_GET(self):
        response = self.client.get(reverse(LOGIN_VIEWNAME))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response=response, template_name='student_module/login.html')

    def test_success_student_login(self):
        credentials = {
            'username': 'S18012191',
            'password': 'beethoven123'
        }
        response = self.client.post(reverse('student_module:login'), credentials, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_student_info_GET(self):
        self.client.login(username='S18012192', password='beethoven123')
        response = self.client.get(reverse('student_module:student_info'))
        print(response.__dict__)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_module/student_info.html')
