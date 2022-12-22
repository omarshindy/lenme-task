from django.db import models
from .user import User
    
class Investor(User):
    balance_amount = models.IntegerField(default= 50000)
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Investor'
        verbose_name_plural = 'Investors' 
        