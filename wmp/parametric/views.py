from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Parametric

class ParametricListView(ListView):
	model = Parametric

class ParametricDetailView(DetailView):
	model = Parametric