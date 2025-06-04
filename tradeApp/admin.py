from django.contrib import admin
from tradeApp import models, constraints


@admin.register(models.AdImages)
class AdImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.ItemState)
class ItemStateAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.TradeStates)
class TradeStatesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(models.Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['username', 'category', 'state', 'created_at']


@admin.register(models.ExchangeProposal)
class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ['sender_username', 'receiver_username', 'status', 'created_at']
