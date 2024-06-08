from django.db import models, connection

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
        verbose_name="Описание",
        help_text="Введите описание",
        blank=True,
        null=True,
        default=None,
        unique=True,
        db_index=True,
    )

    @classmethod
    def truncate_table_restart_id(cls):
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

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
        blank=True,
        null=True,
        default=None,
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
        null=True,
        blank=True,

        auto_now_add=True,
        verbose_name="Дата создания",
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
        verbose_name="Дата последнего изменения",
    )
    views = models.IntegerField(
        default=0,
        verbose_name='просмотры',
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price", "created_at"]

    def __str__(self):
        return f'{self.name}, {self.category}, {self.price}, {self.created_at}'


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='versions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Продукт',

    )
    version_number = models.PositiveIntegerField(
        default=1,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
        unique=True,

    )
    version_name = models.CharField(
        max_length=255,
        verbose_name="Наименование версии",
        help_text="Введите наименование версии",
    )
    is_current_version = models.BooleanField(
        default=False,
        verbose_name="Аквтивная версия",
    )

    class Meta:
        verbose_name = "Версия товара"
        verbose_name_plural = "Версии товара"

    def __str__(self):
        return f'{self.product.name} - {self.version_number} ({self.version_name})'



