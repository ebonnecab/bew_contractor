from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Record
from .forms import RecordForm

class RecordsListView(ListView):
    """ Renders a list of all Pages. """
    model = Record

    def get(self, request):
        """ GET a list of Pages. """
        records = self.get_queryset().all()
        return render(request, 'records/list.html', {
          'records': records
        })

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