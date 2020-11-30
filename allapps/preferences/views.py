from django.shortcuts import render
from django.views.generic import FormView
from .forms import PreferenceModelForm
from django.contrib import messages


# Create your views here.
class IndexView(FormView):
    form_class = PreferenceModelForm
    template_name = 'preferences/index.html'

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        messages.add_message(
            self.request,
            messages.INFO,
            'Saved Successfully!'
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        form.add_error(None, 'Oops!...Some error occured!')
        return super().form_invalid(form)
