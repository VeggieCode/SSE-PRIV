from django.test import TestCase
from student_module.models.student import Student


class StudentModelTest(TestCase):
    def test_correct_create(self):
        s = Student(matricula='S18012191', correo=123)
        s.save()
        s_saved = Student.objects.get(matricula="S18012191")
        self.assertEqual(s, s_saved)
