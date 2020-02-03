from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F

from .models import Bom,Bom_Detail

class BomListView(ListView):
	model = Bom
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Bom.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(pn__name__icontains=query) |
									Q(fg_pn__name__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Bom.objects.all().order_by('-modified_date')

class BomDetailView(DetailView):
	model = Bom



class BomDetailListView(ListView):
	model = Bom_Detail
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Bom_Detail.objects.filter(Q(rd__icontains=query) |
									Q(title__icontains=query) |
									Q(pn__icontains=query) |
									Q(customer_pn__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Bom_Detail.objects.all().order_by('-modified_date')

class BomDetailDetailView(DetailView):
	model = Bom_Detail