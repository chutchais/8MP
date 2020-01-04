from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from parametric.models import Parametric


class ParametricSerializer(serializers.ModelSerializer):
	# item = ItemSerializer(read_only=True)
	class Meta:
		model = Parametric
		fields = ['performing','item','value','created_date']

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)


# from parametric.models import Parametric


# parametric_detail_url=HyperlinkedIdentityField(
# 		view_name='parametric-api:detail',
# 		lookup_field='pk'
# 		)





# class ParametricListSerializer(ModelSerializer):
# 	url = parametric_detail_url
# 	class Meta:
# 		model = Parametric
# 		fields ='__all__'
		

# class ParametricDetailSerializer(ModelSerializer):
# 	# url = booking_detail_url
# 	class Meta:
# 		model = Parametric
# 		fields = '__all__'


# class ParametricCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Parametric
# 		# fields = '__all__'
# 		fields =[
# 			'performing',
# 			'name',
# 			'value',
# 			'id'
# 		]

# class ParametricUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Parametric
# 		# fields = '__all__'
# 		fields =[
# 			'value'
# 		]



