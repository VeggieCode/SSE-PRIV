from django.test import TestCase
from student_module.models.student import Student


# Create your tests here.
class StudentModelTest(TestCase):
    def test_student_register(self):
        new_student = Student.objects.create(matricula="S18012191", nombre="Alexis")
        new_student.save()

        searchedStudent = Student.objects.get(matricula="S18012191")
        self.assertEquals(searchedStudent.matricula, "S18012191")

