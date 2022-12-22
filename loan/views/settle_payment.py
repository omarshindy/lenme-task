from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from loan.models import LoanPayments
from loan.helpers import LoanPaymentStatusChoices
from accounts.models import Investor, Borrower

class SettlePaymentAPi(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self, request):
        payment = LoanPayments.objects.get(pk = request.data["payment"])
        if payment == None:
            return Response({"status": "error", "data": "You aren't authorized to perform this action"}, status=status.HTTP_400_BAD_REQUEST)

        investor = Investor.objects.get(pk = payment.investor.id)
        borrower = Borrower.objects.get(pk = payment.loan.borrower.id)
        if payment.loan.borrower.id == self.request.user.id:
            payment.status = LoanPaymentStatusChoices.Paid
            investor.balance_amount += payment.amount
            borrower.loan_amount -= payment.amount
            payment.save()
            investor.save()
            borrower.save()
            return Response({"status": "success", "data": "Payment Settled Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "You aren't authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)
    
    