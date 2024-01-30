from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from student_module.models import Student


class TestStudentViews(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='S18012191', password='beethoven123')
        self.user.save()
        self.client = Client()

    def test_student_info_GET(self):
        is_logged = self.client.login(username='S18012191', password='beethoven123')
        self.assertTrue(is_logged, msg='Succesfully logged in!')

        response = self.client.get(reverse('student_module:student_info'))

        print(response)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'student_module/student_info.html')
