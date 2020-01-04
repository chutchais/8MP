# from django.db.models import Q

# from rest_framework import generics

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

# from rest_framework import permissions


# from snippet.models import Snippet
# from .serialize import (SnippetListSerializer,
# 						SnippetCreateSerializer,
# 						SnippetDetailSerializer,
# 						SnippetUpdateSerializer)

# from .permissions import IsOwnerOrReadOnly



# class SnippetList(generics.ListCreateAPIView):
# 	queryset 			= Snippet.objects.none()
# 	serializer_class 	= SnippetListSerializer
# 	filter_backends 	= [SearchFilter,OrderingFilter]
# 	search_fields 		= ['name']
# 	# permission_classes 	= (IsAuthenticatedOrReadOnly,
# 	# 					IsOwnerOrReadOnly)

# 	def perform_create(self, serializer):
# 		serializer.save(user=self.request.user),

# 	def get_queryset(self,*args,**kwargs):
# 		queryset_list = Snippet.objects.all()
# 		name = self.request.GET.get("name")
# 		if name != None :
# 			queryset_list = Snippet.objects.filter(
# 					Q(name__icontains = name))
# 		return queryset_list
# 	# pagination_class = PostPageNumberPagination

# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset 			= Snippet.objects.all()
#     lookup_field 		= 'slug'
#     serializer_class 	= SnippetDetailSerializer
#     # permission_classes 	= (IsAuthenticatedOrReadOnly,
#     # 					IsOwnerOrReadOnly,)


# # class SnippetDetailAPIView(RetrieveAPIView):
# # 	queryset= Snippet.objects.all()
# # 	serializer_class = SnippetDetailSerializer
# # 	lookup_field = 'slug'
# # 	# print ("vessel details")

# # class SnippetDeleteAPIView(DestroyAPIView):
# # 	queryset= Snippet.objects.all()
# # 	serializer_class= SnippetDetailSerializer
# # 	lookup_field='slug'
# # 	# permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


# # class SnippetCreateAPIView(CreateAPIView):
# # 	queryset= Snippet.objects.all()
# # 	serializer_class= SnippetCreateSerializer
# # 	# permission_classes = [IsAuthenticated]

# # class SnippetUpdateAPIView(RetrieveUpdateDestroyAPIView):
# # 	queryset=Snippet.objects.all()
# # 	serializer_class=SnippetUpdateSerializer
# # 	lookup_field='slug'

