from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)


from failure.models import Failure


failure_url=HyperlinkedIdentityField(
		view_name='failure-api:detail',
		lookup_field='pk'
		)





class FailureListSerializer(ModelSerializer):
	url = failure_url
	class Meta:
		model = Failure
		fields ='__all__'
		

class FailureDetailSerializer(ModelSerializer):
	# url = booking_detail_url
	class Meta:
		model = Failure
		fields = '__all__'


class FailureCreateSerializer (ModelSerializer):
	class Meta:
		model = Failure
		# fields = '__all__'
		fields =[
			'performing',
			'symptomcode',
			'remark',
			'id'
		]

class FailureUpdateSerializer (ModelSerializer):
	class Meta:
		model = Failure
		# fields = '__all__'
		fields =[
			'remark'
		]



