from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from loan.models import LoanPayments
from loan.serializers import LoanPaymentSerializer
from accounts.models import Borrower

class LoanPaymentsListAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def get(self, request, *args, **kwargs):
        borrower = Borrower.objects.get(pk= self.request.user.id)
        loan = self.kwargs.get("loan")
        if borrower != None:
            loan_payments = LoanPayments.objects.filter(loan= loan)
            if len(list(loan_payments)) == 0:
                return Response({"status": "error", "data": "Requested Loan has no payments"}, status=status.HTTP_401_UNAUTHORIZED) 
                           
            serializer = LoanPaymentSerializer(loan_payments, many = True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({"status": "error", "data": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)