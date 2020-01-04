from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import DefectCode

class DefectCodeListView(ListView):
	model = DefectCode

class DefectCodeDetailView(DetailView):
	model = DefectCode