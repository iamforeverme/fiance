"""
A script to run periodical to fetch exchange rate and put them in the database
"""
import requests
import json
import os
from time import sleep
# 
# export DJANGO_SETTINGS_MODULE=backend.settings
# 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
EXCHANGE_RATE_URL = r"http://free.currencyconverterapi.com/api/v3/convert?"
TIME_INTERVAL = 60*10
import django
django.setup()
from fetch_finacial_data.models import Currency, ExchangeRate

while True:
	currency_set = Currency.objects.all()
	for currency in currency_set:
		currency_type = currency.currency_type
		if currency_type == 'USD':
			continue
		exchange_key = "{}_USD".format(currency_type)
		param = {'q':exchange_key,"compact":'y'}
		response = requests.get(EXCHANGE_RATE_URL,param)
		response_json = json.loads(response.text)
		rate = float(response_json[exchange_key]['val'])
		exchange_rate = ExchangeRate(currency_type = currency, exchange_rate=rate)
		exchange_rate.save()
	sleep(TIME_INTERVAL)