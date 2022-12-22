from django.contrib import admin
from accounts.models import Investor


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'balance_amount')
