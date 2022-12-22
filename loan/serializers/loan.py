from rest_framework import serializers
from loan.models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ('id' ,'borrower', 'amount', 'period','status','created_at')