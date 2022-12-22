from rest_framework import serializers
from loan.models import Offers

class OffersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        fields = ('id' ,'loan', 'investor', 'annual_interest', 'status')