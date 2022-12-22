from rest_framework import serializers
from accounts.models import Borrower

# Borrower Serializer
class BorrowerSerializer(serializers.ModelSerializer):
    def to_representation(self, object):
        
        response = super().to_representation(object)
        del response["password"]
        return response
    
    class Meta:
        model = Borrower
        fields = ('id', 'username', 'email', 'password')
        
    
class RegisterBorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Borrower.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user