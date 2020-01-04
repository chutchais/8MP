from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from operation.models import Operation



class OperationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Operation
		fields = ['name','operation_type','customer_name',
				'title','description','category1','category2',
				'created_date','modified_date','status','slug','url']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

class OperationUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Operation
		fields = ['name','url']




# Older Serializer




# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)







# operation_detail_url=HyperlinkedIdentityField(
# 		view_name='operation-api:detail',
# 		lookup_field='slug'
# 		)

# class OperationListSerializer(ModelSerializer):
# 	url = operation_detail_url
# 	class Meta:
# 		model = Operation
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'slug'
# 		]

# class OperationDetailSerializer(ModelSerializer):
# 	class Meta:
# 		model = Operation
# 		fields ='__all__'

# class OperationCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Operation
# 		fields =[
# 			'name',
# 			'title',
# 			'url',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]

# class OperationUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Operation
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2',
# 			'user'
# 		]



