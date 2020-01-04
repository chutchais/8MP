from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from .models import Failure

class FailureListView(ListView):
	model = Failure

class FailureDetailView(DetailView):
	model = Failure