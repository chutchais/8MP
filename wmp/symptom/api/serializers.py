from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from symptom.models import (Symptom,
							SymptomCode)



class SymptomCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = SymptomCode
		fields = ['name',
				'title','description','symptom_type','category1','category2',
				'created_date','status','slug','url']

class SymptomCodeUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = SymptomCode
		fields = ['name','url']



class SymptomSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields = ['performing','symptomcode','note','cnd',
					'created_date','user','url']

class SymptomUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Symptom
		fields = ['performing','url']

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField
# 	)


# from symptom_code.models import SymptomCode


# symptom_code_url = HyperlinkedIdentityField(
# 		view_name='symptomcode-api:detail',
# 		lookup_field='slug'
# 		)

# class SymptomCodeListSerializer(ModelSerializer):
# 	url = symptom_code_url
# 	# routing 	= RoutingListSerializer(read_only=True)
# 	class Meta:
# 		model = SymptomCode
# 		# fields ='__all__'
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'url',
# 			'slug'
# 		]

# class SymptomCodeDetailSerializer(ModelSerializer):

# 	class Meta:
# 		model = SymptomCode
# 		fields ='__all__'


# class SymptomCodeCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = SymptomCode
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2'
# 		]

# class SymptomCodeUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = SymptomCode
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2'
# 		]



