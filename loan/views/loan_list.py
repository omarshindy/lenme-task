from rest_framework import generics, permissions, status
from rest_framework.response import Response
from loan.models import Loan
from loan.helpers import LoanStatusChoices
from loan.serializers import LoanSerializer
from accounts.models import Investor

class LoanListAPI(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = LoanSerializer
    
    def get_queryset(self):
        investor = Investor.objects.get(pk= self.request.user.id)
        
        if investor != None:
            return Loan.objects.filter(status = LoanStatusChoices.Pending)
        else:
            return Response({"status": "error", "data": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)