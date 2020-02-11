from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
from .models import Performing

class PerformingListView(ListView):
	model = Performing
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		workorder = self.request.GET.get('workorder')
		operation = self.request.GET.get('operation')
		product = self.request.GET.get('product')
		interval = self.request.GET.get('interval')
		result = self.request.GET.get('result')

		if query :
			return Performing.objects.filter(Q(sn__number__icontains=query) ).order_by('sn__number')

		# Product Set
		# First pass & fail
		if product and operation and interval and result :
			result = True if result=='true' else False
			print('First pass & fail')
			return Performing.objects.filter(sn__workorder__product=product,
										operation=operation,interval=1 ,
										result = result ).order_by('sn__number')
		# First all
		if product and operation and interval :
			print('First tested')
			return Performing.objects.filter(sn__workorder__product=product,
										operation=operation,interval=1  ).order_by('sn__number')
		# All passed & fail
		if product and operation and result :
			result = True if result=='true' else False
			print('All pass or fail')
			return Performing.objects.filter(sn__workorder__product=product,
										operation=operation ,
										result = result ).order_by('sn__number')
		# All
		if product and operation :
			print('All tested')
			return Performing.objects.filter(sn__workorder__product=product,
										operation=operation  ).order_by('sn__number')

		# Workorder Set
		# First pass & fail
		if workorder and operation and interval and result :
			result = True if result=='true' else False
			print('First pass & fail')
			return Performing.objects.filter(sn__workorder=workorder,
										operation=operation,interval=1 ,
										result = result ).order_by('sn__number')
		# First all
		if workorder and operation and interval :
			print('First tested')
			return Performing.objects.filter(sn__workorder=workorder,
										operation=operation,interval=1  ).order_by('sn__number')
		# All passed & fail
		if workorder and operation and result :
			result = True if result=='true' else False
			print('All pass or fail')
			return Performing.objects.filter(sn__workorder=workorder,
										operation=operation ,
										result = result ).order_by('sn__number')
		# All
		if workorder and operation :
			print('All tested')
			return Performing.objects.filter(sn__workorder=workorder,
										operation=operation  ).order_by('sn__number')
		
		return Performing.objects.all().order_by('-start_time')

class PerformingDetailView(DetailView):
	model = Performing
	slug_field = 'uid'
	slug_url_kwarg = 'uid'