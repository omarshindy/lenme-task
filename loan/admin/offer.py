from django.contrib import admin
from loan.models import Offers

    
@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = ('id' ,'loan', 'investor', 'annual_interest', 'status', 'created_at', 'updated_at')