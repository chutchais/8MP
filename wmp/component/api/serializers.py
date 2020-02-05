from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from component.models import Component,Part



class ComponentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Component
		fields = '__all__'
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

class PartSerializer(serializers.ModelSerializer):
	class Meta:
		model = Part
		fields = '__all__'
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}