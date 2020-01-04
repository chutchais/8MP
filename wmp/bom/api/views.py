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


# from bom.models import Bom

# from .serialize import (BomListSerializer,
# 						BomCreateSerializer,
# 						BomDetailSerializer,
# 						BomUpdateSerializer)



# class BomListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = BomListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Bom.objects.all()
# 		name = self.request.GET.get("q")
# 		if name != None :
# 			queryset_list = Bom.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class BomDetailAPIView(RetrieveAPIView):
# 	queryset= Bom.objects.all()
# 	serializer_class = BomDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class BomDeleteAPIView(DestroyAPIView):
# 	queryset= Bom.objects.all()
# 	serializer_class= BomDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class BomCreateAPIView(CreateAPIView):
# 	queryset= Bom.objects.all()
# 	serializer_class= BomCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class BomUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Bom.objects.all()
# 	serializer_class=BomUpdateSerializer
# 	lookup_field='slug'

