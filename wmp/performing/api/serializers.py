from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from performing.models import Performing
from serialnumber.api.serializers import SerialNumberUrlSerializer


class PerformingSerializer(serializers.ModelSerializer):
	# sn = SerialNumberUrlSerializer(many=False,read_only=True)
	class Meta:
		model = Performing
		fields = ['uid','sn','operation','resource_name','interval',
				'start_time','stop_time','result','remark','created_date','url','user']

class PerformingUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Performing
		fields = ['uid','url']

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)


# from performing.models import Performing
# # from shipper.api.serialize import ShipperSerializer
# # from vessel.api.serialize import VesselSerializer

# performing_detail_url=HyperlinkedIdentityField(
# 		view_name='performing-api:detail',
# 		lookup_field='pk'
# 		)





# class PerformingListSerializer(ModelSerializer):
# 	url = performing_detail_url
# 	# shipper = ShipperSerializer(allow_null=True)
# 	# vessel = VesselSerializer()
# 	class Meta:
# 		model = Performing
# 		# fields ='__all__'
# 		fields =[
# 			'id',
# 			'sn',
# 			'operation',
# 			'url',
# 			'start_time',
# 			'stop_time',
# 			'result',
# 			'resource_name',
# 			'remark',
# 			'user'
# 		]

# class PerformingDetailSerializer(ModelSerializer):
# 	# url = booking_detail_url
# 	class Meta:
# 		model = Performing
# 		fields = '__all__'
# 		# fields =[
# 		# 	'sn',
# 		# 	'operation',
# 		# 	'start_time',
# 		# 	'stop_time',
# 		# 	'result',
# 		# 	'remark',
# 		# 	'user'
# 		# ]

# class PerformingCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Performing
# 		fields =[
# 			'sn',
# 			'operation',
# 			'start_time',
# 			'stop_time',
# 			'result',
# 			'resource_name',
# 			'remark',
# 			'id'
# 		]

# class PerformingUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Performing
# 		fields =[
# 			'sn',
# 			'operation',
# 			'start_time',
# 			'stop_time',
# 			'result',
# 			'resource_name',
# 			'remark',
# 			'user'
# 		]



