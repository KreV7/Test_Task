from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from employees.models import Subdivision, Position
from employees.forms import PositionForm, SubdivisionForm


class EmplLoginView(LoginView):
    template_name = 'registration/login.html'


def main_page(request):
    subdivisions = Subdivision.objects.all()

    context = {
        'subdivisions': subdivisions
    }

    return render(request, 'main.html', context)


class SubdivisionList(ListView):
    template_name = 'subdivisions/subdivisions.html'
    context_object_name = 'subdivisions'

    def get_queryset(self):
        return Subdivision.objects.all().order_by('title')


class SubdivisionCreate(CreateView):
    template_name = 'subdivisions/subdivision_create.html'
    form_class = SubdivisionForm
    model = Subdivision
    success_url = '/subdivisions/'


class SubdivisionUpdate(UpdateView):
    template_name = 'subdivisions/subdivision_update.html'
    form_class = SubdivisionForm
    model = Subdivision
    success_url = '/subdivisions/'


class SubdivisionDelete(DeleteView):
    template_name = 'subdivisions/subdivision_delete.html'
    model = Subdivision
    success_url = '/subdivisions/'


class PositionList(ListView):
    template_name = 'positions/positions.html'
    context_object_name = 'positions'

    def get_queryset(self):
        return Position.objects.all().order_by('title')


class PositionCreate(CreateView):
    template_name = 'positions/position_create.html'
    form_class = PositionForm
    model = Position
    success_url = '/positions/'


class PositionUpdate(UpdateView):
    template_name = 'positions/position_update.html'
    model = Position
    form_class = PositionForm
    success_url = '/positions/'


class PositionDelete(DeleteView):
    template_name = 'positions/position_delete.html'
    model = Position
    success_url = '/positions/'
