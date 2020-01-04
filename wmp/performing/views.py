from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F
from .models import Performing

class PerformingListView(ListView):
	model = Performing
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Performing.objects.filter(Q(sn__number__icontains=query) ).order_by('sn__number')
		return Performing.objects.all().order_by('-start_time')

class PerformingDetailView(DetailView):
	model = Performing
	slug_field = 'uid'
	slug_url_kwarg = 'uid'