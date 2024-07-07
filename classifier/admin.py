from django.contrib import admin
from .models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('text', 'prediction')
    search_fields = ('text', 'prediction')

admin.site.register(Transaction, TransactionAdmin)
