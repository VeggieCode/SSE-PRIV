# Get user model from settings
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class LoginViewTest(TestCase):
    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='S18012191', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='S18012192', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('student_module:student_info'))
        self.assertRedirects(response, '/sse/login', status_code=302)

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='S18012191', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('student_module:student_info'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
