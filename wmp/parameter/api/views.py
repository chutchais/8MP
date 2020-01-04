# from django.db.models import Q

# from rest_framework.generics import (
# 	CreateAPIView,
# 	DestroyAPIView,
# 	ListAPIView,
# 	UpdateAPIView,
# 	RetrieveAPIView,
# 	RetrieveUpdateAPIView,
# 	RetrieveUpdateDestroyAPIView
# 	)

# from rest_framework.filters import (
# 	SearchFilter,
# 	OrderingFilter,
# 	)

# from rest_framework.permissions import (
# 	AllowAny,
# 	IsAuthenticated,
# 	IsAdminUser,
# 	IsAuthenticatedOrReadOnly,
# 	)

# # from .serialize import VoySerializer,VoyDetailSerializer
# # from berth.models import Voy

# from parameter.models import Parameter
# from .serialize import (ParameterListSerializer,
# 						ParameterCreateSerializer,
# 						ParameterDetailSerializer,
# 						ParameterUpdateSerializer)



# class ParameterListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = ParameterListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Parameter.objects.all()
# 		name = self.request.GET.get('q')
# 		if name != None :
# 			queryset_list = Parameter.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class ParameterDetailAPIView(RetrieveAPIView):
# 	queryset= Parameter.objects.all()
# 	serializer_class = ParameterDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class ParameterDeleteAPIView(DestroyAPIView):
# 	queryset= Parameter.objects.all()
# 	serializer_class= ParameterDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class ParameterCreateAPIView(CreateAPIView):
# 	queryset= Parameter.objects.all()
# 	serializer_class= ParameterCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class ParameterUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Parameter.objects.all()
# 	serializer_class=ParameterUpdateSerializer
# 	lookup_field='slug'

