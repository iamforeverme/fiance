from django.db import models
from django.utils import timezone 
import datetime

# Create your models here.
class Currency(models.Model):
	US_DOLLAR = 'USD'
	AUSTRILIAN_DOLLAR = 'AUD'
	CHINA_NATIANAL_YUAN = 'CNY'
	CURRENCY_TYPE_CHOICES = (
	    (US_DOLLAR, 'US Dollar'),
	    (AUSTRILIAN_DOLLAR, 'Austrilian Dollar'),
	    (CHINA_NATIANAL_YUAN, 'China National Yuan'),
	)
	currency_type = models.CharField(
	    max_length=3,
	    primary_key=True,
	    choices=CURRENCY_TYPE_CHOICES,
	    default=CHINA_NATIANAL_YUAN,
	)
	def __str__(self):
		"""
		    show obj in the admin
		"""
		return self.currency_type

class ExchangeRate(models.Model):
	currency_type = models.ForeignKey(Currency, on_delete=models.CASCADE)
	record_date = models.DateTimeField(default=timezone.now)
	exchange_rate = models.FloatField(default=1.0)
	def __str__(self):
		"""
		    show obj in the admin
		"""
		return "{currency_type} vs USD : {rate} @{time}".\
		format(currency_type=self.currency_type,rate = str(self.exchange_rate), time = self.record_date.strftime("%Y-%m-%d %H:%M:%S"))

class Bank(models.Model):
	bank_abbreviation = models.CharField(
	    max_length=10,
	    primary_key=True
	)
	bank_name = models.CharField(
	    max_length=200
	)
	def __str__(self):
		"""
		    show obj in the admin
		"""
		return self.bank_abbreviation

class Asset(models.Model):
	asset_abbreviation = models.CharField(
	    max_length=100,
	    primary_key=True
	)
	asset_name = models.CharField(
	    max_length=200
	)
	def __str__(self):
		"""
		    show obj in the admin
		"""
		return self.asset_abbreviation

class Account(models.Model):
	currency_type = models.ForeignKey(Currency, on_delete=models.CASCADE)
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
	asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
	amount = models.FloatField(default=0.0)
	owner = models.CharField(max_length=200)
	record_date = models.DateTimeField(default=timezone.now)
	is_availible = models.BooleanField(default=True)

	def __str__(self):
		"""
		    show obj in the admin
		"""
		return self.owner
	


