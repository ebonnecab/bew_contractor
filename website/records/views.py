from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Record

class RecordsListView(ListView):
    """ Renders a list of all Pages. """
    model = Record

    def get(self, request):
        """ GET a list of Pages. """
        records = self.get_queryset().all()
        return render(request, 'records/list.html', {
          'records': records
        })
