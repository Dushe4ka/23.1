# Generated by Django 4.2.2 on 2024-07-03 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0005_alter_blog_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите владельца продукта",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
