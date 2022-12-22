from django.contrib import admin
from loan.models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id' ,'borrower', 'amount', 'return_amount', 'lenme_fee', 'period', 'processed_installments', 'status', 'created_at', 'updated_at')