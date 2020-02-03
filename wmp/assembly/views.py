from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F

from .models import Assembly

class AssemblyListView(ListView):
	model = Assembly
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Assembly.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(product__name__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Assembly.objects.all().order_by('-modified_date')

class AssemblyDetailView(DetailView):
	model = Assembly
