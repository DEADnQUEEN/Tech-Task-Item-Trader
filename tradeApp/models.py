from django.db import models
from django.contrib.auth.models import User
from tradeApp import constraints
from django.utils import timezone


class AdImages(models.Model):
    image = models.ImageField(
        verbose_name='Изображение'
    )

    class Meta:
        db_table = 'Images'
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"


class Categories(models.Model):
    name = models.CharField(
        max_length=constraints.MAX_NAME_SIZE,
        verbose_name='Название категории'
    )

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class ItemState(models.Model):
    name = models.CharField(
        max_length=constraints.MAX_NAME_SIZE,
        verbose_name='Состояние'
    )

    class Meta:
        db_table = 'States'
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'


class TradeStates(models.Model):
    name = models.CharField(
        verbose_name='Статус обмена',
        max_length=constraints.MAX_NAME_SIZE
    )

    class Meta:
        db_table = 'States'
        verbose_name = 'Состояние обмена'
        verbose_name_plural = 'Состояния'


class Ad(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    title = models.CharField(
        max_length=constraints.MAX_TITLE_LENGTH,
        verbose_name='Заголовок'
    )
    description = models.CharField(
        max_length=constraints.MAX_TITLE_LENGTH,
        verbose_name='Описание'
    )
    images = models.ManyToManyField(
        AdImages,
        verbose_name='Изображения'
    )
    category = models.ForeignKey(
        Categories,
        verbose_name='Категории'
    )
    state = models.ForeignKey(
        ItemState,
        verbose_name='Состояние товара'
    )
    created_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        db_table = 'Ad'
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'


class ExchangeProposal(models.Model):
    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель'
    )
    receiver = models.ForeignKey(
        User,
        verbose_name='Получатель'
    )
    comment = models.CharField(
        max_length=constraints.MAX_DESCRIPTION_LENGTH,
        verbose_name='Комментарий',
        blank=True,
        default=''
    )
    status = models.ForeignKey(
        TradeStates,
        verbose_name='Состояние обмена'
    )
    created_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
