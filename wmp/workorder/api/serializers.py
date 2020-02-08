from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from workorder.models import WorkOrder
from product.api.serializers import ProductUrlSerializer
from routing.api.serializers import RoutingUrlSerializer



class WorkorderSerializer(serializers.ModelSerializer):
	routing = RoutingUrlSerializer(many=False,read_only=True)
	product = ProductUrlSerializer(many=False)
	class Meta:
		model = WorkOrder
		fields = ['name','product','routing','qty','regexp',
				'title','description','category1','category2',
				'created_date','modified_date','status','slug','url','registered','build_type']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)


# from workorder.models import WorkOrder
# from routing.api.serialize import RoutingListSerializer

# workorder_detail_url=HyperlinkedIdentityField(
# 		view_name='workorder-api:detail',
# 		lookup_field='slug'
# 		)

# class WorkOrderListSerializer(ModelSerializer):
# 	url = workorder_detail_url
# 	# routing 	= RoutingListSerializer(read_only=True)
# 	class Meta:
# 		model = WorkOrder
# 		# fields ='__all__'
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'product',
# 			'routing',
# 			'slug'
# 		]

# class WorkOrderDetailSerializer(ModelSerializer):
# 	routing 	= RoutingListSerializer(read_only=True)
# 	product 	= SerializerMethodField()  #Slug field
# 	class Meta:
# 		model = WorkOrder
# 		fields ='__all__'
# 	def get_product(self,obj):
# 		return obj.product.slug

# class WorkOrderCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = WorkOrder
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'description',
# 			'product',
# 			'routing'
# 			'category1',
# 			'category2',
# 			'user'
# 		]

# class WorkOrderUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = WorkOrder
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'product',
# 			'routing',
# 			'category1',
# 			'category2',
# 			'user'
# 		]



