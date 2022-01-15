import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class Subdivision(models.Model):
    title = models.CharField(max_length=250)
    address = models.CharField(max_length=250, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Position(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title


class Employee(models.Model):
    DEPARTMENTS = (
        ('Human Resources Department', 'Отдел кадров'),
        ('Accounting', 'Бухгалтерия'),
        ('Purchase department', 'Отдел снабжения'),
        ('Management', 'Руководство'),
        ('Production and technical department', 'Производственно-технический отдел'),
        ('Foremen', 'Производители работ'),
    )

    f_name = models.CharField(max_length=64)
    l_name = models.CharField(max_length=64)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.CASCADE)
    department = models.CharField(max_length=128, choices=DEPARTMENTS)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employment_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.l_name} {self.f_name}'

    def work_experience(self):
        today = datetime.date.today()
        exp = today - self.employment_date

        if exp.days < 31:
            return f'{exp.days} дней'
        elif 31 <= exp.days < 365:
            return f'{exp.days // 31} месяцев и {exp.days % 31} дней'
        elif exp.days > 365:
            return f'{exp.days // 365} лет {(exp.days % 365) // 31} месяцев'

    def get_absolute_url(self):
        return reverse('employee:employee_detail', args=[self.pk])


class AdvUser(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        pass
