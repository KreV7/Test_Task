from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from employees.models import Subdivision, Position, Employee, AdvUser
from employees.forms import PositionForm, SubdivisionForm, EmployeeForm, RegisterUserForm


class EmplLoginView(LoginView):
    pass


class EmplLogoutView(LogoutView):
    pass


@login_required
def main_page(request):
    subdivisions = Subdivision.objects.all()

    context = {
        'subdivisions': subdivisions
    }

    return render(request, 'main.html', context)


class SubdivisionList(LoginRequiredMixin, ListView):
    template_name = 'subdivisions/subdivisions.html'
    context_object_name = 'subdivisions'

    def get_queryset(self):
        return Subdivision.objects.all().order_by('title')


class SubdivisionCreate(LoginRequiredMixin, CreateView):
    template_name = 'subdivisions/subdivision_create.html'
    form_class = SubdivisionForm
    model = Subdivision
    success_url = '/subdivisions/'


class SubdivisionUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'subdivisions/subdivision_update.html'
    form_class = SubdivisionForm
    model = Subdivision
    success_url = '/subdivisions/'


class SubdivisionDelete(LoginRequiredMixin, DeleteView):
    template_name = 'subdivisions/subdivision_delete.html'
    model = Subdivision
    success_url = '/subdivisions/'


class PositionList(LoginRequiredMixin, ListView):
    template_name = 'positions/positions.html'
    context_object_name = 'positions'

    def get_queryset(self):
        return Position.objects.all().order_by('title')


class PositionCreate(LoginRequiredMixin, CreateView):
    template_name = 'positions/position_create.html'
    form_class = PositionForm
    model = Position
    success_url = '/positions/'


class PositionUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'positions/position_update.html'
    model = Position
    form_class = PositionForm
    success_url = '/positions/'


class PositionDelete(LoginRequiredMixin, DeleteView):
    template_name = 'positions/position_delete.html'
    model = Position
    success_url = '/positions/'


class UsersList(LoginRequiredMixin, ListView):
    template_name = 'users/users.html'
    context_object_name = 'users'

    def get_queryset(self):
        return AdvUser.objects.filter(is_superuser=False)


class UserCreate(LoginRequiredMixin, CreateView):
    template_name = 'registration/register_user.html'
    form_class = RegisterUserForm
    success_url = '/users/'


class EmployeeList(LoginRequiredMixin, ListView):
    template_name = 'employees/employees.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        return Employee.objects.all().order_by('l_name')


class EmployeeCreate(LoginRequiredMixin, CreateView):
    template_name = 'employees/employee_create.html'
    form_class = EmployeeForm
    model = Employee
    success_url = '/employees/'


class EmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee


class EmployeeUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'employees/employee_update.html'
    model = Employee
    form_class = EmployeeForm
    success_url = '/employees/'


class EmployeeDelete(LoginRequiredMixin, DeleteView):
    template_name = 'employees/employee_delete.html'
    model = Employee
    success_url = '/employees/'
