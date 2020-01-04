from rest_framework import serializers
from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField
	)

from item.models import Item,ItemList
from snippet.api.serializers import SnippetUrlSerializer


class ItemSerializer(serializers.ModelSerializer):
	# snippet = serializers.HyperlinkedIdentityField(view_name='snippet-detail',
	# 										lookup_field ='pk',
	# 										many=False, read_only=False)
	lists = serializers.HyperlinkedIdentityField(view_name='itemlist-detail',
											many=True, read_only=False)
	snippet = SnippetUrlSerializer(many=False)
	absolute_url = serializers.URLField(source='get_absolute_url', read_only=True)

	class Meta:
		model = Item
		fields = ['id','name','help_text','input_type','default_value','regexp',
				'expected_return','snippet','lists',
				'title','description','category1','category2','required',
				'created_date','modified_date','status','slug','url','absolute_url']
		extra_kwargs = {
			'url': {'lookup_field': 'slug'}
		}

class ItemListSerializer(serializers.ModelSerializer):
	class Meta:
		model = ItemList
		fields = ['ordered','name','item','value','default',
				'title','description','category1','category2',
				'created_date','modified_date','status','slug','url']

# from rest_framework.serializers import (
# 	ModelSerializer,
# 	HyperlinkedIdentityField,
# 	SerializerMethodField,
# 	StringRelatedField,
# 	SlugRelatedField,
# 	HyperlinkedModelSerializer,
# 	ReadOnlyField
# 	)
# # from rest_framework.serializers import (
# # 	ModelSerializer,
# # 	HyperlinkedIdentityField,
# # 	SerializerMethodField,
# # 	HyperlinkedModelSerializer,
# # 	ReadOnlyField
# # 	)


# from item.models import Item
# from item_list.api.serialize import ItemListListSerializer
# # from vessel.api.serialize import VesselSerializer

# item_detail_url=HyperlinkedIdentityField(
# 		view_name='item-api:detail',
# 		lookup_field='slug'
# 		)





# class ItemListSerializer(ModelSerializer):
# 	url = item_detail_url
# 	# shipper = ShipperSerializer(allow_null=True)
# 	# lists = ItemListListSerializer(many=True, read_only=True)
# 	# lists = StringRelatedField(many=True)


# 	class Meta:
# 		model = Item
# 		# fields ='__all__'
# 		fields =[
# 			'name',
# 			'title',
# 			'slug',
# 			'product',
# 			'description',
# 			'input_type',
# 			'default_value',
# 			'regexp',
# 			'url',
# 			'status'
# 		]

# class ItemDetailSerializer(ModelSerializer):
# 	lists = ItemListListSerializer(many=True, read_only=True)
# 	snippet 	 = SlugRelatedField (many=False,read_only=True,slug_field='slug')
# 	url = item_detail_url
# 	class Meta:
# 		model = Item
# 		fields ='__all__'
# 		# fields =[
# 		# 	'name',
# 		# 	'title',
# 		# 	'product',
# 		# 	'description',
# 		# 	'input_type',
# 		# 	'lists',
# 		# 	'default_value',
# 		# 	'regexp',
# 		# 	'user',
# 		# 	'snippet',
# 		# 	'expected_return',
# 		# 	'url'
# 		# ]

# class ItemCreateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Item
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]

# class ItemUpdateSerializer (ModelSerializer):
# 	class Meta:
# 		model = Item
# 		fields =[
# 			'name',
# 			'title',
# 			'description',
# 			'user'
# 		]



