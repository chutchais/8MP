from django.shortcuts import render

from django.views.generic import DetailView,CreateView,UpdateView,DeleteView,ListView

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.db.models import Q,F


from .models import Snippet



@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'users': reverse('user-api:list', request=request, format=format),
		'snippets': reverse('snippet-api:list', request=request, format=format)
	})


class SnippetListView(ListView):
	model = Snippet
	paginate_by = 100
	def get_queryset(self):
		query = self.request.GET.get('q')
		if query :
			return Snippet.objects.filter(Q(name__icontains=query) |
									Q(title__icontains=query) |
									Q(description__icontains=query) ).order_by('-modified_date')
		return Snippet.objects.all().order_by('-modified_date')

class SnippetDetailView(DetailView):
	model = Snippet


class SnippetHighlight(generics.GenericAPIView):
	queryset = Snippet.objects.all()
	renderer_classes = (renderers.StaticHTMLRenderer,)
	lookup_field ='slug'

	def get(self, request, *args, **kwargs):
		snippet = self.get_object()
		return Response(snippet.highlighted)