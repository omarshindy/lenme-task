from django.db import models
from loan.helpers import LoanPaymentStatusChoices
from accounts.models import Investor
from .loan import Loan

class LoanPayments(models.Model):
    loan = models.ForeignKey(Loan, on_delete = models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete = models.CASCADE)
    amount = models.IntegerField(null= True, blank= True)
    status = models.IntegerField(
        choices=LoanPaymentStatusChoices.choices,
        default= LoanPaymentStatusChoices.Scheduled
    )
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'LoanPayment'
        verbose_name_plural = 'LoanPayments'  