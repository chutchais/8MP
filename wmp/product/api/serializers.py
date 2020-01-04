from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from product.models import Product
from routing.api.serializers import RoutingUrlSerializer



class ProductSerializer(serializers.ModelSerializer):
	routing = RoutingUrlSerializer(many=False,read_only=True)
	class Meta:
		model = Product
		fields = ['name','pn','rev','routing',
				'regexp','fg_pn','fg_rev',
				'title','description','category1','category2',
				'created_date','modified_date','status','slug','url']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

class ProductUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['name','url']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)

# from routing.api.serialize import RoutingListSerializer
# from product.models import Product
# # from shipper.api.serialize import ShipperSerializer
# # from vessel.api.serialize import VesselSerializer

# product_detail_url=HyperlinkedIdentityField(
# 		view_name='product-api:detail',
# 		lookup_field='slug'
# 		)





# class ProductListSerializer(ModelSerializer):
# 	url = product_detail_url
# 	# shipper = ShipperSerializer(allow_null=True)
# 	# vessel = VesselSerializer()
# 	class Meta:
# 		model = Product
# 		# fields ='__all__'
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]

# class ProductDetailSerializer(ModelSerializer):
# 	routing 	= RoutingListSerializer(read_only=True)
# 	class Meta:
# 		model = Product
# 		fields ='__all__'

# class ProductCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Product
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]
		
# 		# def perform_create(self, serializer):
#   #   serializer.save(owner=self.request.user)


# class ProductUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Product
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]



