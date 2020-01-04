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
		if query :
			return SerialNumber.objects.filter(Q(number__icontains=query) ).order_by('number')
		return SerialNumber.objects.all().order_by('-last_modified_date')

class SerialNumberDetailView(DetailView):
	model = SerialNumber