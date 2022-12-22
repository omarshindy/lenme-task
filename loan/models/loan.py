from django.db import models
from loan.helpers import LoanStatusChoices 
from accounts.models import Borrower

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete= models.CASCADE )
    amount = models.IntegerField(null= False, blank= False)
    return_amount = models.IntegerField(null= True, blank= True)
    period = models.IntegerField(null= False, blank= False)
    processed_installments = models.IntegerField(default= 0)
    lenme_fee = models.IntegerField(default= 3)
    status = models.IntegerField(
        choices=LoanStatusChoices.choices,
        default= LoanStatusChoices.Pending
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = 'Loan'
        verbose_name_plural = 'Loans' 