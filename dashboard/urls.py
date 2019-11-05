from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='index'),
    path('search', views.search, name ='search'),
    path('manager/', views.manager, name ='manager'),
    path('setting/', views.setting, name ='setting'),
    path('live_crypto_prices/', views.live_crypto_prices, name ='live_crypto_prices'),

]