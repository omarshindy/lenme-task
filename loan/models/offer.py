from django.db import models
from loan.helpers import OfferStatusChoices
from accounts.models import Investor
from .loan import Loan

class Offers(models.Model):
    loan = models.ForeignKey(Loan, on_delete= models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete= models.CASCADE)
    annual_interest = models.IntegerField(null= False, blank= False)
    status = models.IntegerField(
        choices=OfferStatusChoices.choices,
        default= OfferStatusChoices.Pending
    )    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'