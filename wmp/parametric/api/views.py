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

# from parametric.models import Parametric
# from .serialize import (ParametricListSerializer,
# 						ParametricCreateSerializer,
# 						ParametricDetailSerializer,
# 						ParametricUpdateSerializer)



# class ParametricListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = ParametricListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['name']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Parametric.objects.all()
# 		number = self.request.GET.get("name")
# 		if number != None :
# 			queryset_list = Parametric.objects.filter(
# 					Q(name__icontains = number))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class ParametricDetailAPIView(RetrieveAPIView):
# 	queryset= Parametric.objects.all()
# 	serializer_class = ParametricDetailSerializer
# 	lookup_field = 'pk'
# 	# print ("vessel details")

# class ParametricDeleteAPIView(DestroyAPIView):
# 	queryset= Parametric.objects.all()
# 	serializer_class= ParametricDetailSerializer
# 	lookup_field='pk'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class ParametricCreateAPIView(CreateAPIView):
# 	queryset= Parametric.objects.all()
# 	serializer_class= ParametricCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# 	def perform_create(self,serializer):
# 		serializer.save(user=self.request.user)
			
# class ParametricUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Parametric.objects.all()
# 	serializer_class=ParametricUpdateSerializer
# 	lookup_field='pk'

