from django.shortcuts import render
from django.views.generic import FormView
from .forms import PreferenceModelForm


# Create your views here.
class IndexView(FormView):
    form_class = PreferenceModelForm
    template_name = 'preferences/index.html'
