from django.db import models

class LoanStatusChoices(models.IntegerChoices):
    Pending = 1, 'Pending'
    Funded = 2, 'Funded'
    Completed = 3, 'Completed'
    Default = 4, "Default"
    
    
class OfferStatusChoices(models.IntegerChoices):
    Pending = 1, 'Pending'
    Accepted = 2, 'Accepted'
    Rejected = 3, 'Rejected'

class LoanPaymentStatusChoices(models.IntegerChoices):
    Paid = 1, 'Paid'
    Scheduled = 2, 'Scheduled'
    Default = 3, 'Default'