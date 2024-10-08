# Generated by Django 5.1.1 on 2024-10-05 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название категории')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Название категории')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Название категории')),
                ('name_ky', models.CharField(max_length=50, null=True, verbose_name='Название категории')),
                ('icon', models.ImageField(upload_to='category/icon', verbose_name='Иконка')),
                ('icon_mobile', models.ImageField(upload_to='category/icon_mobile', verbose_name='Иконка')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Заголовок')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('is_like', models.BooleanField(default=False, verbose_name='Нравится')),
                ('created_at', models.DateTimeField(verbose_name='Время создания')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='item', to='cards.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ItemImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='item', verbose_name='Изображение')),
                ('image_mobile', models.ImageField(upload_to='item', verbose_name='Изображение')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_images', to='cards.item')),
            ],
            options={
                'verbose_name': 'Изображение товара',
                'verbose_name_plural': 'Изображения товаров',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='ItemParametrs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(choices=[('Новый', 'new'), ('Бу', 'used')], max_length=255, verbose_name='Состояние : ')),
                ('mileage', models.IntegerField(verbose_name='Пробег (км.) : ')),
                ('car_body', models.CharField(choices=[('Седан', 'sedan'), ('Хэтчбек', 'hatchback'), ('Универсал', 'wagon'), ('Купе', 'coupe'), ('Кабриолет', 'convertible'), ('Кроссовер', 'crossover'), ('Внедорожник', 'suv'), ('Минивэн', 'minivan'), ('Пикап', 'pickup'), ('Лифтбек', 'liftback')], max_length=255, null=True, verbose_name='Кузов: ')),
                ('fuel', models.CharField(choices=[('Бензин', 'Gasoline'), ('Дизель', 'Diesel'), ('Электрический', 'Electric'), ('Гибридные', 'Hybrid')], max_length=255, verbose_name='Топливо: ')),
                ('color_car', models.CharField(choices=[('Белый', 'White'), ('Черный', 'Black'), ('Серый', 'Gray'), ('Серебристый', 'Silver'), ('Синий', 'Blue'), ('Красный', 'Красный'), ('Коричневый', 'Brown'), ('Бронзовый', 'Bronze'), ('Зеленый', 'Green'), ('Желтый', 'Yellow'), ('Оранжевый', 'Orange')], max_length=255, verbose_name='Цвет: ')),
                ('availability', models.CharField(choices=[('В наличии', 'In stock'), ('Нет', 'No')], default='Available', max_length=255, verbose_name='Наличие: ')),
                ('technical_condition', models.CharField(max_length=100, null=True)),
                ('model', models.TextField(verbose_name='Модель: ')),
                ('year', models.DateField(verbose_name='Год: ')),
                ('transmission', models.CharField(choices=[('Механическая', 'Manual'), ('Автоматическая', 'Automatic'), ('Роботизированная', 'Robotized'), ('Роботизированная с двумя сцеплениями', 'Dual-Clutch'), ('Вариатор', 'Continuously Variable')], max_length=255, verbose_name='Коробка передач: ')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parametrs', to='cards.category')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='cards.item')),
            ],
            options={
                'verbose_name': 'Параметр товара',
                'verbose_name_plural': 'Параметры товаров',
                'ordering': ('order',),
            },
        ),
    ]
