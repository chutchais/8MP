from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
from .models import Parametric

class ParametricListView(ListView):
	model = Parametric
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Parametric.objects.filter(Q(item__name__icontains=query) |
									Q(performing__sn__number__icontains=query) ).order_by('-created_date')
		return Parametric.objects.all().order_by('-created_date')

class ParametricDetailView(DetailView):
	model = Parametric