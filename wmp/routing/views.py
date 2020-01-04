from django.shortcuts import render
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView
from django.db.models import Q,F

from .models import (Routing,RoutingDetail,
						RoutingDetailNext,
						RoutingDetailAccept,
						RoutingDetailReject,
						RoutingDetailHook)

class RoutingListView(ListView):
	model = Routing
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Routing.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Routing.objects.all().order_by('-modified_date')

class RoutingDetailView(DetailView):
	model = Routing

class RoutingOperationDetailView(DetailView):
	model = RoutingDetail

class RoutingDetailNextView(DetailView):
	model = RoutingDetailNext

class RoutingDetailAcceptView(DetailView):
	model = RoutingDetailAccept

class RoutingDetailRejectView(DetailView):
	model = RoutingDetailReject

class RoutingDetailHookView(DetailView):
	model = RoutingDetailHook