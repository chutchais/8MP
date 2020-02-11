from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
from .models import SerialNumber
from operation.models import Operation


class SerialNumberListView(ListView):
	model = SerialNumber
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		workorder = self.request.GET.get('workorder')
		operation = self.request.GET.get('operation')
		product = self.request.GET.get('product')
		if query :
			return SerialNumber.objects.filter(Q(number__icontains=query) ).order_by('number')
		if workorder and operation :
			return SerialNumber.objects.filter(
				workorder=workorder,current_operation=operation ).order_by('-last_modified_date')
		if product and operation :
			return SerialNumber.objects.filter(
				workorder__product=product,current_operation=operation ).order_by('-last_modified_date')
		return SerialNumber.objects.all().order_by('-last_modified_date')

class SerialNumberDetailView(DetailView):
	model = SerialNumber