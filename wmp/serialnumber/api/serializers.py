from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from serialnumber.models import SerialNumber



class SerialNumberSerializer(serializers.ModelSerializer):
	class Meta:
		model = SerialNumber
		fields = ['id','number','workorder','description','category1','category2',
				'registered_date','routing','current_operation','last_operation',
				'last_modified_date','last_result','finished_date','wip',
				'perform_start_date','perform_operation','perform_resource','status','slug','url',
				'parent','unit_type','user']

		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

	# def create(self, request, *args, **kwargs):
	# 	# serializer = ProfileSerializer(data=request.data)
	# 	# serializer.is_valid(raise_exception=True)
	# 	# serializer.save()
	# 	return Response(request.dataserializer.data)
	# def create(self, request, *args, **kwargs):
	# 	serializer = self.get_serializer(data=request.data)
	# 	serializer.is_valid(raise_exception=True)
	# 	self.perform_create(serializer)
	# 	headers = self.get_success_headers(serializer.data)
	# 	return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class SerialNumberUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = SerialNumber
		fields = ['number','workorder','url']

		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)


# from serialnumber.models import SerialNumber

# from workorder.api.serialize import WorkOrderListSerializer
# from routing.api.serialize import RoutingListSerializer

# serialnumber_detail_url=HyperlinkedIdentityField(
# 		view_name='serialnumber-api:detail',
# 		lookup_field='slug'
# 		)


# class SerialNumberListSerializer(ModelSerializer):
# 	url 		= serialnumber_detail_url
	
# 	# routing = HyperlinkedIdentityField(view_name='routing-api:detail',lookup_field='slug')
# 	class Meta:
# 		model = SerialNumber
# 		fields =[
# 			'number',
# 			'slug',
# 			'workorder',
# 			'url',
# 			'wip',
# 			'current_operation',
# 			'last_operation'
# 		]
# 		# depth =1

# class SerialNumberDetailSerializer(ModelSerializer):
# 	# Full Information
# 	# workorder  	= WorkOrderListSerializer(read_only=True)
# 	# routing 	= RoutingListSerializer(read_only=True)

# 	routing 	= SerializerMethodField() #Slug field
# 	workorder 	= SerializerMethodField()  #Slug field
# 	class Meta:
# 		model = SerialNumber
# 		fields ='__all__'

# 	def get_routing(self,obj):
# 		return None if obj.routing == None else obj.routing.slug

# 	def get_workorder(self,obj):
# 		return obj.workorder.slug


# class SerialNumberCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = SerialNumber
# 		fields =[
# 			'number',
# 			'workorder',
# 			'description',
# 			'category1',
# 			'category2',
# 			'routing',
# 			'current_operation',
# 			'user',
# 			'id',
# 			'slug'
# 		]

# class SerialNumberUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = SerialNumber
# 		fields =[
# 			'number',
# 			'workorder',
# 			'description',
# 			'category1',
# 			'category2',
# 			'routing',
# 			'current_operation',
# 			'last_operation',
# 			'last_result',
# 			'finished_date',
# 			'wip',
# 			'perform_start_date',
# 			'perform_operation'

# 		]



