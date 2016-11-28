from django.conf.urls import url
from .views import CurrencyList, ExchangeRateList, AccountList, BankList, AssetList

urlpatterns = [
    url(r'^currency/$', CurrencyList.as_view()),
    url(r'^exchange_rate/$', ExchangeRateList.as_view()),
    url(r'^account/$', AccountList.as_view()),
    url(r'^bank/$', BankList.as_view()),
    url(r'^asset/$', AssetList.as_view()),
]
