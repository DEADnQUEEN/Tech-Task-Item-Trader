from django.db import models
from django.contrib.auth.models import User
from tradeApp import constraints
from django.contrib import admin


class AdImages(models.Model):
    image = models.ImageField(
        verbose_name='Изображение'
    )

    @property
    @admin.display(description='Название изображения')
    def image_name(self):
        return self.image.name

    class Meta:
        db_table = 'Images'
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображения"

    def __str__(self):
        return f'Изображение {self.image_name}'


class Categories(models.Model):
    name = models.CharField(
        max_length=constraints.MAX_NAME_SIZE,
        verbose_name='Название категории'
    )

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория {self.name}'


class ItemState(models.Model):
    name = models.CharField(
        max_length=constraints.MAX_NAME_SIZE,
        verbose_name='Состояние'
    )

    class Meta:
        db_table = 'ItemStates'
        verbose_name = 'Состояние предмета'
        verbose_name_plural = 'Состояния предметов'


class TradeStates(models.Model):
    name = models.CharField(
        verbose_name='Статус обмена',
        max_length=constraints.MAX_NAME_SIZE
    )

    class Meta:
        db_table = 'TradeStates'
        verbose_name = 'Состояние обмена'
        verbose_name_plural = 'Состояния обменов'


class Ad(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        related_name='item_user'
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
        verbose_name='Категории',
        on_delete=models.CASCADE,
        related_name='category_item'
    )
    state = models.ForeignKey(
        ItemState,
        verbose_name='Состояние товара',
        on_delete=models.CASCADE,
        related_name='state_item'
    )
    created_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        db_table = 'Ad'
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    @property
    @admin.display(description='Логин пользователя')
    def username(self):
        return self.user.username

    @property
    @admin.display(description='Краткое описание')
    def short_desctiption(self):
        return


class ExchangeProposal(models.Model):
    sender = models.ForeignKey(
        User,
        verbose_name='Отправитель',
        on_delete=models.CASCADE,
        related_name='trade_sender'
    )
    receiver = models.ForeignKey(
        User,
        verbose_name='Получатель',
        on_delete=models.CASCADE,
        related_name='trade_receiver'
    )
    comment = models.CharField(
        max_length=constraints.MAX_DESCRIPTION_LENGTH,
        verbose_name='Комментарий',
        blank=True,
        default=''
    )
    status = models.ForeignKey(
        TradeStates,
        verbose_name='Состояние обмена',
        on_delete=models.CASCADE,
        related_name='trade_state'
    )
    created_at = models.DateField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    @property
    @admin.display(description='Логин отправителя')
    def sender_username(self):
        return self.sender.username

    @property
    @admin.display(description='Логин получателя')
    def receiver_username(self):
        return self.receiver.username

    class Meta:
        db_table = 'Trades'
        verbose_name = 'Обмен'
        verbose_name_plural = "Обмены"
