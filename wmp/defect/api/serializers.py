from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from defect.models import DefectCode,Defect



class DefectCodeSerializer(serializers.ModelSerializer):
	class Meta:
		model = DefectCode
		fields = ['name',
				'title','description','category1','category2',
				'created_date','status','slug','url']

class DefectCodeUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = DefectCode
		fields = ['name','url']



class DefectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Defect
		fields = ['symptom','defectcode','note','ndf',
					'created_date','user','url']

class DefectUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Defect
		fields = ['sysmptom','url']
