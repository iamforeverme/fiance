from django.contrib import admin
from .models import Currency, ExchangeRate, Account, Bank, Asset


admin.site.register(Currency)
admin.site.register(Bank)
admin.site.register(Asset)
admin.site.register(ExchangeRate)



class AccountAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if change:
			self.super(self,AccountAdmin).save_model(request, obj, form, change)
		else:
			account = Account.objects.get(bank = obj.bank,
								   asset = obj.asset,
								   owner = obj.owner,
								   currency_type = obj.currency_type,
								   is_availible = True)
			if account:
				account.is_availible = False
				account.save()
			obj.save()

admin.site.register(Account,AccountAdmin)