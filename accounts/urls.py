from django.urls import path, include
from knox import views as knox_views
from .views import RegisterBorrowerAPI, RegisterInvestorAPI, BorrowerSignInAPI, InvestorSignInAPI

urlpatterns = [
    path('api/register/borrower', RegisterBorrowerAPI.as_view(), name='register_borrower'),
    path('api/register/investor', RegisterInvestorAPI.as_view(), name='register_investor'),
    path('api/auth/borrower/login/', BorrowerSignInAPI.as_view(), name = "login_borrower"),
    path('api/auth/investor/login/', InvestorSignInAPI.as_view(), name = "login_investor"),

]