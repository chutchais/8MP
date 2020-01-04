from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
from .models import Parameter

class ParameterListView(ListView):
	model = Parameter
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Parameter.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Parameter.objects.all().order_by('-modified_date')

class ParameterDetailView(DetailView):
	model = Parameter