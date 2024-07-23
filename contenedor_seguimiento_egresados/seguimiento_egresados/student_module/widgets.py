from django import forms

from student_module.validators import NUMBER


class MatriculaInput(forms.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab'}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
            forms.TextInput(attrs={'maxlength': '1', 'class': 'autotab', 'pattern': NUMBER}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value[i:i + 1] for i in range(0, 9)]
        return [None, None, None, None, None, None, None, None, None]

    def value_from_datadict(self, data, files, name):
        values = [data.get(name + '_%s' % i, '')[:1] for i in range(0, 9)]
        return ''.join(values)
