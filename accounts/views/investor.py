from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from accounts.serializers import InvestorSerializer, RegisterInvestorSerializer, LoginSerializer


class RegisterInvestorAPI(generics.GenericAPIView):
    serializer_class = RegisterInvestorSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": InvestorSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })



class InvestorSignInAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": InvestorSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })