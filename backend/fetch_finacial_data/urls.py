from django.conf.urls import url
from .views import CurrencyList, ExchangeRateList, AccountList, BankList, AssetList, current_exchange_rate

urlpatterns = [
    url(r'^currency/$', CurrencyList.as_view()),
    url(r'^exchange_rate/$', ExchangeRateList.as_view()),
    url(r'^account/$', AccountList.as_view()),
    url(r'^bank/$', BankList.as_view()),
    url(r'^asset/$', AssetList.as_view()),
    url(r'^current_exchange_rate/(?P<currency_type>[A-Z]+)/$',current_exchange_rate)
]
