from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Record, Patient, Doctor
from .forms import RecordForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class RecordsListView(ListView):
    """ Renders a list of all Pages. """
    model = Record

    def get(self, request):
        """ GET a list of Pages. """
        records = self.get_queryset().all()
        return render(request, 'records/records_list.html', {
          'records': records
        })


class PatientsListView(ListView):
    """ Renders a list of all Pages. """
    model = Patient

    def get(self, request):
        """ GET a list of Pages. """
        patients = self.get_queryset().all()
        return render(request, 'records/patients_list.html', {
          'patients': patients
        })

class PatientsDetailView(DetailView):
    """ Renders a specific page based on it's pk."""
    model = Patient

    fields= '__all__'



class RecordsDetailView(DetailView):
    """ Renders a specific page based on it's pk."""
    model = Record


class RecordsCreateView(CreateView):

    def get(self, request, *args, **kwargs):
      context = {'form': RecordForm()}
      return render(request, 'records/new.html', context)

    def post(self, request, *args, **kwargs):
      form = RecordForm(request.POST)
      if form.is_valid():
        page = form.save()
        return HttpResponseRedirect(reverse_lazy('index'))
      return render(request, 'new.html', {'form': form})


class RecordsUpdateView(UpdateView):
    model = Record
    fields = '__all__'
    template_name_suffix = '_update_form'
    def get_success_url(self):
      return reverse_lazy('index')

class RecordsDeleteView(DeleteView):
    model = Record
    template_name = 'records/records_delete.html'
    success_url = reverse_lazy('index')
    