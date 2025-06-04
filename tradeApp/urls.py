from django.urls import path
from tradeApp import views

urlpatterns = [
    path('show-offers/', views.show_items, name='show_offers'),
    path('show-offers/<int:page>/', views.show_items, name='show_offers')
]
