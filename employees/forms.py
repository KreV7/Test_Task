from django import forms

from employees.models import Position, Subdivision


class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = (
            'title',
        )


class SubdivisionForm(forms.ModelForm):
    class Meta:
        model = Subdivision
        fields = (
            'title',
            'address',
            'note'
        )
