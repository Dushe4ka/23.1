from django.db import models

from catalog.models import Category
from users.models import User

NULLABLE = {"blank": "True", "null": "True"}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    # category = models.ForeignKey(
    #     Category,
    #     on_delete=models.SET_NULL,
    #     verbose_name="Категория",
    #     help_text="Выберите категорию",
    #     related_name="products",
    #     null=True,
    #     blank=True,
    #     related_query_name="product",
    # )
    slug = models.CharField(max_length=150, verbose_name="URL", **NULLABLE)
    content = models.TextField(verbose_name="Содержимое", **NULLABLE)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена за покупку",
        help_text="Введите цену",
        **NULLABLE
    )
    preview = models.ImageField(upload_to='media/photo', **NULLABLE)
    created_at = models.DateField(auto_created=True, verbose_name="дата создания", **NULLABLE)
    published = models.BooleanField(default=True, verbose_name='опубликован')
    views = models.IntegerField(default=0, verbose_name='просмотры')
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        null=True,
        blank=True,
        help_text='Укажите владельца продукта',
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Личный кабинет"
        verbose_name_plural = "Личные кабинеты"

class Version(models.Model):
    product = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="versions", verbose_name='Продукт')
    number = models.PositiveIntegerField(verbose_name='Номер версии', default=1)
    name = models.CharField(max_length=100, verbose_name='Название версии', default='V_1')
    is_current = models.BooleanField(default=False, verbose_name='Актуальная')

    class Meta:
        verbose_name = "Версия товара"
        verbose_name_plural = "Версии товара"

    def __str__(self):
        return f'{self.product.name} - {self.number} ({self.name})'
