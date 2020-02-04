from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	HyperlinkedRelatedField,
	SerializerMethodField
	)

from routing.models import (Routing,RoutingDetail,RoutingDetailNext,
							RoutingDetailNextSet,RoutingDetailAccept,RoutingDetailAcceptSet,
							RoutingDetailReject,RoutingDetailRejectSet,
							RoutingDetailHook,
							RoutingDetailParameterSet)

from snippet.api.serializers import SnippetUrlSerializer
from parameter.api.serializers import ParameterSerializer
from assembly.api.serializers import AssemblyUsageUrlSerializer

class RoutingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routing
		fields = ['name','title','description',
				'category1','category2','url','status']

class RoutingUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Routing
		fields = ['name','url']

class RoutingDetailSerializer(serializers.ModelSerializer):
	accept_code = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailaccept-detail')
	reject_code = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailreject-detail')
	next_code   = HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailnext-detail')
	parameter   = HyperlinkedRelatedField(many=True,read_only=True,view_name='parameter-detail')
	hooks   	= HyperlinkedRelatedField(many=True,read_only=True,view_name='routingdetailhook-detail')
	# assembly_usages   	= HyperlinkedRelatedField(many=True,read_only=True,
	# 					view_name='assembly_usage-detail',lookup_field='slug')
	assembly_usages = AssemblyUsageUrlSerializer(many=True,read_only=True)
	class Meta:
		model = RoutingDetail
		fields =  ['operation','routing','position','title','description',
				'category1','category2','parameter','next_pass','next_fail',
				'accept_code','reject_code','next_code','hooks','assembly_usages','status','url','slug']



# Next Code Serialize
class RoutingNextSetSerializer(serializers.ModelSerializer):
	# routingnext = RoutingDetailNextSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailNextSet
		fields =  ['title','ordered','operation','status'] #'routingnext',


class RoutingDetailNextSerializer(serializers.ModelSerializer):
	# snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	snippet = SnippetUrlSerializer(many=False, read_only=True)
	nexts   = RoutingNextSetSerializer(many=True,read_only=True)
	class Meta:
		model = RoutingDetailNext
		fields = ['name','title','description','slug','nexts',
				'category1','category2','status','snippet','url']


# ---------------------------

# Accept Serialize
class RoutingDetailAcceptSerializer(serializers.ModelSerializer):
	# snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	snippet = SnippetUrlSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailAccept
		fields = ['name','title','description','slug',
				'category1','category2','status','snippet','url']

class RoutingDetailAcceptSetSerializer(serializers.ModelSerializer):
	routingaccept = RoutingDetailAcceptSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailAcceptSet
		fields =  '__all__'


# Reject Serialize
class RoutingDetailRejectSerializer(serializers.ModelSerializer):
	# snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	snippet = SnippetUrlSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailReject
		fields = ['name','title','description','slug',
				'category1','category2','status','snippet','url']

class RoutingDetailRejectSetSerializer(serializers.ModelSerializer):
	routingreject = RoutingDetailRejectSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailRejectSet
		fields =  '__all__'


# Parameter set
class RoutingDetailParameterSetSerializer(serializers.ModelSerializer):
    # routingnext = RoutingDetailRejectSerializer(many=False, read_only=True)
	# parameter = HyperlinkedIdentityField(view_name='parameter-detail')
	parameter = ParameterSerializer(many=False , read_only=True)
	class Meta:
		model = RoutingDetailParameterSet
		fields =  '__all__'


# Hook Serialize
class RoutingDetailHookSerializer(serializers.ModelSerializer):
	# snippet = HyperlinkedIdentityField(view_name='snippet-detail')
	snippet = SnippetUrlSerializer(many=False, read_only=True)
	class Meta:
		model = RoutingDetailHook
		fields =  ['name','title','description',
					'ordered','event','snippet','category1','category2',
					'status','url']