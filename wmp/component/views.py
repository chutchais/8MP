from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F

from .models import Module,Component

class ModuleListView(ListView):
	model = Module
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Module.objects.filter(Q(number__icontains=query) |
									Q(pn__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-last_modified_date')
		return Module.objects.all().order_by('-last_modified_date')

class ModuleDetailView(DetailView):
	model = Module




class ComponentDetailView(DetailView):
	model = Component



class ComponentListView(ListView):
	model = Component
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Component.objects.filter(Q(number__icontains=query) |
									Q(pn__icontains=query) |
									Q(barcode__icontains=query) |
									Q(datecode__icontains=query) |
									Q(lotcode__icontains=query) |
									Q(supcode__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-last_modified_date')
		return Component.objects.all().order_by('-last_modified_date')