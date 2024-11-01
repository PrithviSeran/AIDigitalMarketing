from rest_framework import serializers
from . models import *
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCampaign
        fields = ['name', 'use', 'user_info', 'purpose', 'target_audience', 'created_at', 'user']

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'])
		user_obj.username = clean_data['username']
		user_obj.save()
		return user_obj


class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(username=clean_data['username'], password=clean_data['password'])
		if not user:
			return False
		return user


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ['username', 'password']


class NewCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewCampaign
        fields = ['id', 'name', 'use', 'user_info', 'purpose', 'target_audience', 'created_at', 'user']

class DomainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessDomains
        fields = ['name', 'domain', 'url', 'content']