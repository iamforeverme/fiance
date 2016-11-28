from django.contrib import admin
from .models import Currency, ExchangeRate, Account, Bank, Asset


admin.site.register(Currency)
admin.site.register(Bank)
admin.site.register(Asset)
admin.site.register(ExchangeRate)
admin.site.register(Account)
