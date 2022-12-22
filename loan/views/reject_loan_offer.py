from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from loan.helpers import LoanStatusChoices, OfferStatusChoices
from loan.models import Loan, Offers
from loan.tasks import schedule_payments
from accounts.models import Borrower, Investor


class RejectLoanOfferAPi(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def post(self, request):
        loan = Loan.objects.filter(id = request.data["loan"]).first()
        offer = Offers.objects.filter(id = request.data["offer"]).first()
        if loan == None or offer == None:
            return Response({"status": "error", "data": "Requested Loan or Offer aren't Valid"}, status=status.HTTP_400_BAD_REQUEST)
        
        if self.request.user.id == loan.borrower.id:
            offer.status = OfferStatusChoices.Rejected
            offer.save()
            return Response({"status": "success", "data": "Offer Rejected Successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": "You aren't authorized to perform this action"}, status=status.HTTP_401_UNAUTHORIZED)