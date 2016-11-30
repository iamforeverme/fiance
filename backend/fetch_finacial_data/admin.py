from django.contrib import admin
from .models import Currency, ExchangeRate, Account, Bank, Asset


admin.site.register(Currency)
admin.site.register(Bank)
admin.site.register(Asset)
admin.site.register(ExchangeRate)



class AccountAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if change:
			super(AccountAdmin,self).save_model(request, obj, form, change)
		else:
			try:
				account = Account.objects.get(bank = obj.bank,
									   asset = obj.asset,
									   owner = obj.owner,
									   currency_type = obj.currency_type,
									   mature_date = obj.mature_date,
									   interest_rate = obj.interest_rate,
									   is_availible = True)
				account.is_availible = False
				account.save()
			except Account.DoesNotExist:
				pass
			obj.save()

admin.site.register(Account,AccountAdmin)