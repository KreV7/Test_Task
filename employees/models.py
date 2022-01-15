from django.db import models
from django.contrib.auth.models import AbstractUser


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
        ('Foreman', 'Производители работ'),
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


class AdvUser(AbstractUser):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)

    class Meta(AbstractUser.Meta):
        pass
