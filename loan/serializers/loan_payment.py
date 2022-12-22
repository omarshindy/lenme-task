from rest_framework import serializers
from loan.models import LoanPayments

class LoanPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayments
        fields = ('id' ,'loan', 'investor', 'amount', 'status', 'due_date', 'created_at')