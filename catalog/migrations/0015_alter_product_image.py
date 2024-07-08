# Generated by Django 4.2.2 on 2024-07-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0014_product_release_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True,
                default=None,
                help_text="Загрузите изображение",
                null=True,
                upload_to="product/",
                verbose_name="Изображение",
            ),
        ),
    ]