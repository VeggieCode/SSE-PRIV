from django.conf import settings
from django.core import mail
from django.test import TestCase

# subject, message, from_email and recipient_list son parametros REQUERIDOS.
personal_emails = [
    'alexisao@hotmail.com',
]

mockMailData = {
    'to': ['test@example.com'],
    'from': 'admin@django.com',
    'subject': 'Subject Mock Data',
    'body': 'Body Mock Data',
}

settingsMailData = {
    'to': personal_emails,
    'from': settings.DEFAULT_FROM_EMAIL,
    'subject': 'Subject Test Data',
    'body': 'Body Test Data',
}


class SendMailTestCase(TestCase):
    to = []
    from_email: str
    subject: str
    body: str

    def setUp(self):
        self.dummy_email_setup()
        self.backend_email_setup()

    def test_mail_params(self):
        email_params = mockMailData
        self.assertEqual(self.dummy_email_message.subject, email_params['subject'])
        self.assertEqual(self.dummy_email_message.body, email_params['body'])
        self.assertEqual(self.dummy_email_message.from_email, email_params['from'])
        self.assertEqual(self.dummy_email_message.to, email_params['to'])

    def test_send_email_without_backend(self):
        self.dummy_email_message.send()
        actual_outbox = mail.outbox
        self.assertIn(self.dummy_email_message, actual_outbox, 'is not in outbox')

    def test_send_email_backend(self):
        result = self.backend_email_message.send()
        assert result == -1

    def dummy_email_setup(self):
        self.dummy_email_message = mail.EmailMessage(
            mockMailData.get('subject'),
            mockMailData.get('body'),
            mockMailData.get('from'),
            mockMailData.get('to')
        )

    def backend_email_setup(self):
        backend_connection = mail.get_connection(backend='django.core.mail.backends.smtp.EmailBackend')
        self.backend_email_message = mail.EmailMessage(
            settingsMailData.get('subject'),
            settingsMailData.get('body'),
            settingsMailData.get('from'),
            settingsMailData.get('to'),
            connection=backend_connection
        )
