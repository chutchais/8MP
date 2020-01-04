from django.shortcuts import render

# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.contrib.staticfiles.templatetags.staticfiles import static
# from django.http import HttpResponse
# from django.urls import reverse_lazy
# from django.shortcuts import redirect
# import os.path
# from django.conf import settings


# from django.db.models import Q,F
# from django.shortcuts import get_object_or_404
from .models import Bom
from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

class BomListView(ListView):
	model = Bom

class BomDetailView(DetailView):
	model = Bom
	# template_name = 'crm/bookingfile_detail.html'

	# def get_context_data(self, **kwargs):
	# 	context = super(BookingFileDetailView, self).get_context_data(**kwargs)
	# 	# context['now'] = timezone.now()
	# 	print (kwargs)
	# 	print(self.kwargs.get('slug'))
	# 	return context

