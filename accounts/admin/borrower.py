from django.contrib import admin
from accounts.models import Borrower

@admin.register(Borrower)
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'loan_amount')

