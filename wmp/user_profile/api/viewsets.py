from rest_framework import viewsets,filters
from rest_framework import status, viewsets
from rest_framework.decorators import action,detail_route
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from user_profile.models import Profile
from user_profile.api.serializers import ProfileSerializer,UserAccessListSerializer


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	filter_backends = (filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend)
	search_fields = ('user__username','department','title','status')
	filter_fields = ('user__username','department','title','status')

	@detail_route()
	def operations(self, request, pk=None):
		profile = self.get_object()
		serializer = UserAccessListSerializer(profile.operations.all(), 
		context={'request': request}, many=True)
		return Response(serializer.data)