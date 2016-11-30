from .models import Currency, ExchangeRate, Account, Bank, Asset
from rest_framework import serializers



# Create your models here.
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('currency_type',)

class ExchangeRateSerializer(serializers.ModelSerializer):
	class Meta:
		model = ExchangeRate
		fields = ('id', 'currency_type','record_date','exchange_rate')

class BankSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank
		fields = ('bank_abbreviation','bank_name')


class AssetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Asset
		fields = ('asset_abbreviation','asset_name')

class AccountSerializer(serializers.ModelSerializer):
	class Meta:
		model = Account
		fields = ('id','currency_type','bank','asset','amount','owner','record_date','interest_rate','mature_date')