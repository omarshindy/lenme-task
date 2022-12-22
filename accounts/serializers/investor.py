from rest_framework import serializers
from accounts.models import Investor


class InvestorSerializer(serializers.ModelSerializer):
    def to_representation(self, object):
        
        response = super().to_representation(object)
        del response["password"]
        return response
        
    class Meta:
        model = Investor
        fields = ('id', 'username', 'email', 'password')

class RegisterInvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Investor.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user    