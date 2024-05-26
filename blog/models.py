from django.db import models

NULLABLE = {"blank": "True", "null": "True"}


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.CharField(max_length=150, verbose_name="URL", **NULLABLE)
    content = models.TextField(verbose_name="Содержимое", **NULLABLE)
    preview = models.ImageField(upload_to='media/photo', **NULLABLE)
    created_at = models.DateField(auto_created=True, verbose_name="дата создания")
    published = models.BooleanField(default=True, verbose_name='опубликован')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

