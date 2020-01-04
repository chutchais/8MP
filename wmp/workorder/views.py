from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
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
	query = SerialNumber.objects.filter(current_operation__slug = slug)
	return render(request, 'workorder/workorder_wip.html', {'object_list':query})