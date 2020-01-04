from rest_framework.serializers import (
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	StringRelatedField
	)

from rest_framework import serializers


from user_profile.models import Profile,AccessOperation
# from snippet.models import Snippet

from operation.api.serializers import  OperationSerializer

# userprofile_detail_url = HyperlinkedIdentityField(
#     view_name='profile-api:detail',
#     lookup_field = 'pk'
#     )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','department','title','url','status']



class UserAccessListSerializer(serializers.ModelSerializer):
    operation = OperationSerializer(many=False,read_only=True)
    class Meta:
        model = AccessOperation
        fields = ['profile','operation']







# class UserDetailSerializer(serializers.ModelSerializer):
#     accessoperation_set = UserAccessListSerializer(many=True, read_only=True)
#     class Meta:
#         model = Profile
#         fields = ('user','department','title','accessoperation_set')

# class ProfileListSerializer(serializers.ModelSerializer):
#     # url         = userprofile_detail_url
#     class Meta:
#         model = Profile
#         fields = ('user','department','title')

