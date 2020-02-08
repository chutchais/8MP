from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
from django.db.models import Count,Sum,Value,Min,Max, When,Case,IntegerField,CharField
from .models import WorkOrder
from serialnumber.models import SerialNumber

class WorkOrderListView(ListView):
	model = WorkOrder
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return WorkOrder.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return WorkOrder.objects.all().order_by('-modified_date')

class WorkOrderDetailView(DetailView):
	model = WorkOrder


def onwip(request,slug):
	sn = SerialNumber.objects.filter(workorder__slug = slug)
	query   = sn.values('current_operation').annotate(total_wip=Count('number'))
	print (query)
	return render(request, 'workorder/workorder_wip.html', {'object_list':query})