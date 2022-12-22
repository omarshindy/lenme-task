from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from loan.serializers import OffersSerializer
from loan.models import Loan
from accounts.models import Investor

class CreateLoanOfferAPi(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = OffersSerializer
    
    def post(self, request):
        serializer = OffersSerializer(data=request.data)
        if self.request.user.id == request.data["investor"]:
            investor = Investor.objects.filter(id = request.data["investor"]).first()
            loan = Loan.objects.filter(id = request.data["loan"]).first()
            if loan == None:
                return Response({"status": "error", "data": "Requested Loan not available"}, status=status.HTTP_400_BAD_REQUEST)
            if investor.balance_amount >= loan.amount + loan.lenme_fee:
                if serializer.is_valid():
                    serializer.save()
                    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
                else:
                    return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else: 
                return Response({"status": "error", "data": "Unsufficient Balance"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "error", "error": "UnAuthorized Action"}, status=status.HTTP_401_UNAUTHORIZED)