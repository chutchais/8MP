from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from snippet.models import Snippet



class SnippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ['name','code',
				'title','description','category1','category2',
				'created_date','modified_date','status','slug','url']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

class SnippetUrlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Snippet
		fields = ['name','url']
		lookup_field = 'slug'
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField,
# 	StringRelatedField
# 	)

# from rest_framework import serializers


# from snippet.models import Snippet

# snippet_detail_url=HyperlinkedIdentityField(
# 		view_name='snippet-api:detail',
# 		lookup_field='slug'
# 		)

# highlight_url=HyperlinkedIdentityField(
# 		view_name='snippet:highlight',
# 		lookup_field='slug',
# 		format='html'
# 		)





# class SnippetListSerializer(ModelSerializer):
# 	url 		= snippet_detail_url
# 	user 		= serializers.ReadOnlyField(source='user.username')
# 	highlight 	= highlight_url
	
# 	class Meta:
# 		model = Snippet
# 		# fields ='__all__'
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'category1',
# 			'category2',
# 			'slug',
# 			'user',
# 			'url',
# 			'code', 'linenos', 'language', 'style',
# 			'highlight',
# 			'status'
# 		]

# class SnippetDetailSerializer(ModelSerializer):

# 	class Meta:
# 		model = Snippet
# 		fields ='__all__'
		

# class SnippetCreateSerializer (ModelSerializer):

# 	class Meta:
# 		model = Snippet
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]

# class SnippetUpdateSerializer (ModelSerializer):

# 	class Meta:
# 		model = Snippet
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]



