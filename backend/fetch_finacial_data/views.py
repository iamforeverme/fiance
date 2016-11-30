from django.shortcuts import render

from rest_framework import generics
from .serializers import CurrencySerializer, ExchangeRateSerializer, BankSerializer, AssetSerializer, AccountSerializer
from .models import Currency, ExchangeRate, Account, Bank, Asset

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import json
from django.conf import settings
from django.utils import timezone 

class CurrencyList(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class ExchangeRateList(generics.ListCreateAPIView):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    def get_queryset(self):
	    return super(AccountList, self).get_queryset().filter(is_availible=True)

class BankList(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class AssetList(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

def fetch_exchange_rate(currency):
	currency_type = currency.currency_type
	if currency_type == 'USD':
    	# 
		return 1.0
	last_exchange_rate = ExchangeRate.objects.filter(currency_type = currency).order_by('-record_date')[0]
	timedelta =  timezone.now() - last_exchange_rate.record_date
	if timedelta.seconds < 24*60*60:
		return last_exchange_rate.exchange_rate
	else:
		exchange_key = "{}_USD".format(currency_type)
		param = {'q':exchange_key,"compact":'y'}
		response = requests.get(settings.EXCHANGE_RATE_URL,param)
		response_json = json.loads(response.text)
		rate = float(response_json[exchange_key]['val'])
		exchange_rate = ExchangeRate(currency_type = currency, exchange_rate=rate)
		exchange_rate.save()
		return rate

@api_view(['GET'])
def current_exchange_rate(request,currency_type):
	"""
	fetch the current exachange rate, save it into database, and reply to frontend
	"""
	result_list = []
	if currency_type == "ALL":
		currency_set = Currency.objects.all()
		exchange_rate = 1.0
		for currency in currency_set:
			exchange_rate = fetch_exchange_rate(currency)
			result_list.append({currency.currency_type:exchange_rate})
	else:
		currency = Currency.objects.get(currency_type = currency_type)
		exchange_rate = fetch_exchange_rate(currency)
		result_list.append({currency.currency_type:exchange_rate})
	return Response(result_list)
# 	for currency in currency_set:
# 		currency_type = currency.currency_type
# 		if currency_type == 'USD':
# 			continue
# 		exchange_key = "{}_USD".format(currency_type)
# 		param = {'q':exchange_key,"compact":'y'}
# 		try:
# 			response = requests.get(EXCHANGE_RATE_URL,param)
# 		response_json = json.loads(response.text)
# 		rate = float(response_json[exchange_key]['val'])
# 		exchange_rate = ExchangeRate(currency_type = currency, exchange_rate=rate)
# 		exchange_rate.save()

#    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)