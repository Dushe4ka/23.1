# Generated by Django 4.2.2 on 2024-07-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blog_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="price",
            field=models.DecimalField(
                blank="True",
                decimal_places=2,
                help_text="Введите цену",
                max_digits=10,
                null="True",
                verbose_name="Цена за покупку",
            ),
            preserve_default="True",
        ),
    ]
