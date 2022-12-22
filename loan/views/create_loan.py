from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from loan.serializers import LoanSerializer

class CreateLoanAPi(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = LoanSerializer
    
    def post(self, request):
        serializer = LoanSerializer(data=request.data)
        if self.request.user.id == request.data["borrower"]:
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({"status": "error", "data": "Unauthorized Access"}, status=status.HTTP_401_UNAUTHORIZED)