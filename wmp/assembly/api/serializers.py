from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	HyperlinkedRelatedField,
	SerializerMethodField
	)

from assembly.models import Assembly,Assembly_Detail,Assembly_Usage

class AssemblySerializer(serializers.ModelSerializer):
	class Meta:
		model = Assembly
		fields = ['name','product','title','slug','description',
				'category1','category2','status','url']


class AssemblyDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Assembly_Detail
		fields = ['ordered','assembly','part',
		'title','slug','description',
		'category1','category2','status','url','critical','datecode_regexp','lotcode_regexp',
		'supplycode_regexp','sn_regexp']

class AssemblyUsageSerializer(serializers.ModelSerializer):
	assembly   = HyperlinkedRelatedField(many=False,read_only=True,view_name='assembly-detail')
	class Meta:
		model = Assembly_Usage
		fields = ['ordered','assembly','routingdetail',
		'title','description',
		'category1','category2','status','url']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}