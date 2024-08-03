from rest_framework import serializers
from .models import User
from .constants  import REGISTER_USER_MESSAGES

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'code' ,'phone_no', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  
        }

    
    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user

    
class TokenResponseSerializer(serializers.Serializer):
    status = serializers.BooleanField(required=True)
    token = serializers.CharField(max_length=255, required=False)
    error = serializers.CharField(max_length=255, required=False)
    message = serializers.CharField(max_length=255, required=False)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['status']:
            data['message'] =  REGISTER_USER_MESSAGES['USER_REGISTERED_MESSAGE']
        else: 
            data['message'] = REGISTER_USER_MESSAGES['USER_REGISTERED_FAILED_MESSAGE']
        return data
    

class LoginResponseSerializer(serializers.Serializer):
    status = serializers.BooleanField(required=True)
    token = serializers.CharField(max_length=255, required=False)
    error = serializers.CharField(max_length=255, required=False)
    message = serializers.CharField(max_length=255, required=False)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if data['status']:
            data['message'] =  REGISTER_USER_MESSAGES['SUCCESSFUL_LOGIN']
        else: 
            data['message'] = REGISTER_USER_MESSAGES['UNSUCCESSFUL_LOGIN']
        return data