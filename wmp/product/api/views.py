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

# from product.models import Product
# from .serialize import (ProductListSerializer,
# 						ProductCreateSerializer,
# 						ProductDetailSerializer,
# 						ProductUpdateSerializer)



# class ProductListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = ProductListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list =Product.objects.all()
# 		name = self.request.GET.get('q')
# 		if name != None :
# 			queryset_list = Product.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class ProductDetailAPIView(RetrieveAPIView):
# 	queryset= Product.objects.all()
# 	serializer_class = ProductDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class ProductDeleteAPIView(DestroyAPIView):
# 	queryset= Product.objects.all()
# 	serializer_class= ProductDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class ProductCreateAPIView(CreateAPIView):
# 	queryset= Product.objects.all()
# 	serializer_class= ProductCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class ProductUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Product.objects.all()
# 	serializer_class=ProductUpdateSerializer
# 	lookup_field='slug'

