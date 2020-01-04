from django.shortcuts import render
from .models import Operation
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F

from serialnumber.models import SerialNumber

class OperationListView(ListView):
	model = Operation
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Operation.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Operation.objects.all().order_by('-modified_date')

class OperationDetailView(DetailView):
	model = Operation

def onwip(request,slug):
	query = SerialNumber.objects.filter(current_operation__slug = slug)
	print (query)
	return render(request, 'operation/operation_wip.html', {'object_list':query})