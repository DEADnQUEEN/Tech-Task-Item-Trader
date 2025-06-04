from django.contrib import admin
from tradeApp import models


@admin.register(models.AdImages)
class AdImagesAdmin(admin.ModelAdmin):
    search_fields = ['image_name']



@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.ItemState)
class ItemStateAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.TradeStates)
class TradeStatesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(models.Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['username', 'category', 'state', 'created_at']
    autocomplete_fields = ['images', 'category', 'state']


@admin.register(models.ExchangeProposal)
class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ['sender_username', 'receiver_username', 'status', 'created_at']
    autocomplete_fields = ['sender', 'receiver', 'status']
