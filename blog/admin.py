from django.contrib import admin

from blog.models import Blog, Version


# Для моделей категории и продукта настройте отображение в административной панели.
# Для категорий выведите id и наименование в список отображения,
# а для продуктов выведите в список id, название, цену и категорию.
#
# При этом интерфейс вывода продуктов настройте так,
# чтобы можно было результат отображения фильтровать по категории,
# а также осуществлять поиск по названию и полю описания.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "owner", "price")
    list_filter = ("title", "owner", "price")
    search_fields = ("title", "content",)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "number", "name", "is_current")