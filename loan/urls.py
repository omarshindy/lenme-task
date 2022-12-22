from django.urls import path, include
from knox import views as knox_views
from .views import (LoanListAPI,
        CreateLoanAPi,
        CreateLoanOfferAPi,
        AcceptLoanOfferAPi,
        SettlePaymentAPi,
        RejectLoanOfferAPi,
        OffersListAPI,
        LoanPaymentsListAPI
    )

urlpatterns = [
    path('api/', include('knox.urls')),
    path('api/offer', CreateLoanOfferAPi().as_view(), name='loan_offer'),
    path('api/list', LoanListAPI().as_view(), name='list_loans'),
    path('api/list/<int:loan>/offers', OffersListAPI().as_view(), name='list_loan_offers'),
    path('api/list/<int:loan>/payments', LoanPaymentsListAPI().as_view(), name='list_loans'),    
    path('api/create', CreateLoanAPi().as_view(), name='create_loan'),
    path('api/offer/accept', AcceptLoanOfferAPi().as_view(), name='accept_offer'),
    path('api/offer/reject', RejectLoanOfferAPi().as_view(), name='reject_offer'),
    path('api/payment/settle', SettlePaymentAPi().as_view(), name='settle_payment')
]