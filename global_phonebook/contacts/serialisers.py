from rest_framework import serializers
from .models import Contacts


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class ContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name', 'phone_no', 'code', 'is_spam']



