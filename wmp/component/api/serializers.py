from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from component.models import Module,Component
from serialnumber.api.serializers import SerialNumberUrlSerializer


class ModuleSerializer(serializers.ModelSerializer):
	parent 			= SerialNumberUrlSerializer(many=False,read_only=True)
	reserved_for 	= SerialNumberUrlSerializer(many=False,read_only=True)
	class Meta:
		model = Module
		fields = ['number','parent','reserved_for','slug','title','category1','category2',
				'description','pn','rev','datecode','lotcode','supcode',
				'registered_date','last_operation','last_modified_date','status',
				'user','pn_type','url']
		lookup_field = 'number'
		extra_kwargs = {
			'url': {'lookup_field': 'number'}
		}

class ComponentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Component
		fields = ['number','barcode', 'slug','title','category1','category2','description',
				'pn','rev','datecode','lotcode','supcode','qty','carrier',
				'msl','floor_life','shelf_life','met','exp_date','baking_start_date',
				'baking_finish_date','registered_date','last_modified_date','status','user','url']
		# lookup_field = 'slug'
		# extra_kwargs = {
		# 	'url': {'lookup_field': 'slug'}
		# }