from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import SymptomCode

class SymptomCodeListView(ListView):
	model = SymptomCode

class SymptomCodeDetailView(DetailView):
	model = SymptomCode