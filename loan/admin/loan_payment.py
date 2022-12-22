from django.contrib import admin
from loan.models import LoanPayments
    
@admin.register(LoanPayments)
class LoanPaymentsAdmin(admin.ModelAdmin):
    def status(self, object):
        return object.get_status_display()
    list_display = ('id' ,'loan', 'investor', 'amount', 'status', 'due_date', 'created_at', 'updated_at')
    