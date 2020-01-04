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

# from item.models import Item
# from .serialize import (ItemListSerializer,
# 						ItemCreateSerializer,
# 						ItemDetailSerializer,
# 						ItemUpdateSerializer)



# class ItemListAPIView(ListAPIView):
# 	queryset = None #Booking.objects.all()
# 	serializer_class = ItemListSerializer
# 	filter_backends = [SearchFilter,OrderingFilter]
# 	search_fields = ['q']
# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Item.objects.all()
# 		name = self.request.GET.get('q')
# 		if name != None :
# 			queryset_list = Item.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class ItemDetailAPIView(RetrieveAPIView):
# 	queryset= Item.objects.all()
# 	serializer_class = ItemDetailSerializer
# 	lookup_field = 'slug'
# 	# print ("vessel details")

# class ItemDeleteAPIView(DestroyAPIView):
# 	queryset= Item.objects.all()
# 	serializer_class= ItemDetailSerializer
# 	lookup_field='slug'
# 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# class ItemCreateAPIView(CreateAPIView):
# 	queryset= Item.objects.all()
# 	serializer_class= ItemCreateSerializer
# 	# permission_classes = [IsAuthenticated]

# # 	def perform_create(self,serializer):
# # 		print ('Voy is %s' % self.kwargs.get('voy'))
# # 		serializer.save()
# class ItemUpdateAPIView(RetrieveUpdateDestroyAPIView):
# 	queryset=Item.objects.all()
# 	serializer_class=ItemUpdateSerializer
# 	lookup_field='slug'

