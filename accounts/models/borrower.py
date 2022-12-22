from django.db import models
from .user import User

class Borrower(User):
    
    loan_amount = models.IntegerField(default= 0)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Borrower'
        verbose_name_plural = 'Borrowers' 