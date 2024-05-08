from django.db import models

# Product
# Наименование
# Описание
# Изображение (превью)
# Категория
# Цена за покупку
# Дата создания (записи в БД)
# Дата последнего изменения (записи в БД)
# Category
# Наименование
# Описание


class Category(models.Model):
    pass


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Продукт', help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание', help_text='Введите описание')
    image = models.ImageField(upload_to='product/photo', blank=True, null=True, verbose_name='Изображение', help_text='Загрузите изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', help_text='Выберите категорию')

