from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from parameter.models import Parameter,ParameterDetail
from item.api.serializers import ItemSerializer

class ParameterDetailSerializer(serializers.ModelSerializer):
	item = ItemSerializer(read_only=True)
	class Meta:
		model = ParameterDetail
		fields = ['item','ordered','required','status']


class ParameterSerializer(serializers.ModelSerializer):
	# items = ParameterDetailSerializer(read_only=True, many=True)
	items = HyperlinkedIdentityField(view_name='item-detail',read_only=True, many=True,lookup_field='slug')
	class Meta:
		model = Parameter
		fields = ['name','items',
				'title','description','category1','category2',
				'created_date','modified_date','status','slug','url']

		# extra_kwargs = {
		# 	'url': {'lookup_field': 'slug'}
		# }




# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField,
# 	HyperlinkedModelSerializer,
# 	ReadOnlyField
# 	)


# from parameter.models import Parameter,ParameterSet
# from item.api.serialize import ItemListSerializer
# # from vessel.api.serialize import VesselSerializer

# parameter_detail_url=HyperlinkedIdentityField(
# 		view_name='parameter-api:detail',
# 		lookup_field='slug'
# 		)





# class ParameterListSerializer(ModelSerializer):
# 	url = parameter_detail_url
# 	# shipper = ShipperSerializer(allow_null=True)
# 	# vessel = VesselSerializer()
# 	class Meta:
# 		model = Parameter
# 		fields =[
# 			'name',
# 			'title',
# 			'item_count',
# 			'description',
# 			'url',
# 			'slug'
# 		]

# # class ParameterSetSerializer(HyperlinkedModelSerializer):
# #     # name = ReadOnlyField(source='Parameter.name')
# #     # x = ItemListSerializer(read_only=True, many=True)
# #     class Meta:
# #         model = ParameterSet
# #         fields = ('ordered', )

# class ParameterSetSerializer(HyperlinkedModelSerializer ):
# 	name = ReadOnlyField(source='item.name')
# 	title = ReadOnlyField(source='item.title')
# 	description = ReadOnlyField(source='item.description')
# 	input_type = ReadOnlyField(source='item.input_type')
# 	default_value = ReadOnlyField(source='item.default_value')
# 	regexp = ReadOnlyField(source='item.regexp')

# 	# 'url',
# 	slug = ReadOnlyField(source='item.slug')
# 	status = ReadOnlyField(source='item.status')
# 	class Meta:
# 		model = ParameterSet
# 		fields = ['name','title','description','input_type','default_value','regexp','ordered','status','slug','required']

# class ParameterDetailSerializer(ModelSerializer):
# 	# items = ItemListSerializer(read_only=True, many=True)
# 	items = ParameterSetSerializer(source='parametersets', many=True)
# 	class Meta:
# 		model = Parameter
# 		fields ='__all__'
# 		# # depth = 1
# 		# fields =[
# 		# 	'name',
# 		# 	'title',
# 		# 	'items',
# 		# 	'description',
# 		# 	'items',
# 		# 	'user'
# 		# ]

# class ParameterCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Parameter
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]

# class ParameterUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Parameter
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]



