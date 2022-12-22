from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from loan.models import Offers
from loan.helpers import OfferStatusChoices
from loan.serializers import OffersSerializer
from accounts.models import Borrower

class OffersListAPI(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    
    def get(self, request, *args, **kwargs):
        borrower = Borrower.objects.get(pk= self.request.user.id)
        loan = self.kwargs.get("loan")
        if borrower != None:
            offers = Offers.objects.filter(status = OfferStatusChoices.Pending).filter(loan= loan)
            if len(list(offers)) == 0:
                return Response({"status": "error", "data": "Requested Loan has no offers"}, status=status.HTTP_401_UNAUTHORIZED) 
                           
            serializer = OffersSerializer(offers, many = True)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        else:
            return Response({"status": "error", "data": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)