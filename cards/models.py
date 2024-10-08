from _decimal import Decimal

from django.db import models
from .utils import CONDITION_CHOICES, CAR_BODY, FUEL, COLOR_CAR, AVAILABILITY, TECHNICAL_CONDITION, TRANSMISSION, STEERING_WHEEL, DRIVE, CUSTOMS_CLEARANCE


class Category(models.Model):
    name = models.CharField('Название категории', max_length=50, default='')
    icon = models.ImageField('Иконка', upload_to='category/icon', default='', blank=True)
    icon_mobile = models.ImageField('Иконка для мобильного', upload_to='category/icon_mobile', default='', blank=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('order',)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField('Заголовок', max_length=255, default='')
    price = models.CharField('Цена', max_length=20, default='')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='items')
    description = models.TextField('Описание', default='')
    is_like = models.BooleanField('Нравится', default=False)
    created_at = models.DateTimeField('Время создания', auto_now_add=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']

    def __str__(self):
        return self.title


class ItemImages(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='item_images')
    image = models.ImageField('Изображение', upload_to='item')
    image_mobile = models.ImageField('Изображение для мобильного', upload_to='item')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Изображение товара'
        verbose_name_plural = 'Изображения товаров'
        ordering = ('order',)

    def __str__(self):
        return f'Изображение - {self.item.title}'


class ItemParameters(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='parameters')
    condition = models.CharField('Состояние', max_length=255, choices=CONDITION_CHOICES, default='')
    mileage = models.IntegerField('Пробег (км)', default=0)
    car_body = models.CharField('Кузов', max_length=255, choices=CAR_BODY, default='')
    fuel = models.CharField('Топливо', max_length=255, choices=FUEL, default='')
    color_car = models.CharField('Цвет', max_length=255, choices=COLOR_CAR, default='')
    availability = models.CharField('Наличие', max_length=255, choices=AVAILABILITY, default='')
    technical_condition = models.CharField('Техническое состояние', max_length=255, choices=TECHNICAL_CONDITION, default='')
    customs_clearance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField('Описание', default='')
    model = models.CharField('Модель', max_length=255, default='')
    year = models.DateField('Год', null=True, blank=True)
    transmission = models.CharField('Коробка передач', max_length=255, choices=TRANSMISSION, default='')
    engine_displacement = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=Decimal(0),)
    steering_wheel = models.CharField('Руль', max_length=255, choices=STEERING_WHEEL, default='')
    drive = models.CharField('Привод', max_length=255, choices=DRIVE, default='')
    vin_code = models.CharField('VIN код', max_length=255, default='')
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        verbose_name = 'Параметр товара'
        verbose_name_plural = 'Параметры товаров'
        ordering = ('order',)

    def __str__(self):
        return f'Параметры товара: {self.item.title}'