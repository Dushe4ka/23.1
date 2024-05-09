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
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Продукт", help_text="Введите наименование"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание"
    )
    image = models.ImageField(
        upload_to="product/photo",
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию",
        related_name="products",
        null=True,
        blank=True,
        related_query_name="product",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену",
    )
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания",
        help_text="Укажите дату создания",
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения",
        help_text="Укажите дату последнего изменения",
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at"]

    def __str__(self):
        return self.name, self.category, self.price, self.created_at
