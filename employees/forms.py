from django import forms
from django.contrib.auth import password_validation

from employees.models import Position, Subdivision, Employee, AdvUser


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = (
            'title',
        )
        labels = {'title': 'Название должности'}


class SubdivisionForm(forms.ModelForm):
    class Meta:
        model = Subdivision
        fields = (
            'title',
            'address',
            'note'
        )
        labels = {'title': 'Наименование подразделения',
                  'address': 'Адрес',
                  'note': 'Примечание'}


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
            'f_name',
            'l_name',
            'subdivision',
            'department',
            'position',
            'employment_date'
        )
        labels = {'f_name': 'Имя',
                  'l_name': 'Фамилия',
                  'subdivision': 'Подразделение',
                  'department': 'Отдел',
                  'position': 'Должность',
                  'employment_date': 'Дата трудоустройства'
                  }
        widgets = {'employment_date': forms.widgets.DateInput(attrs={'type': 'date'})}


class RegisterUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,
                               help_text=password_validation.password_validators_help_text_html())

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            password_validation.validate_password(password)
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser
        fields = (
            'employee',
            'username',
            'email',
            'password',
        )
        labels = {
            'employee': 'Сотрудник',
            'username': 'Логин',
            'email': 'Электронная почта',
            'password1': 'Пароль',
            'password2': 'Пароль (повторно)',
        }
