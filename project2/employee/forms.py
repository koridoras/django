from django import forms
from .models import Status, Department


class SearchForm(forms.Form):
    status = forms.ModelChoiceField(
        queryset=Status.objects, label='雇用形態', required=False)

    department = forms.ModelChoiceField(
        queryset=Department.objects, label='配属', required=False)