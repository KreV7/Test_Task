from django.contrib import admin

from employees.models import Position, Subdivision, Employee, AdvUser

admin.site.register(AdvUser)
admin.site.register(Position)
admin.site.register(Subdivision)
admin.site.register(Employee)
