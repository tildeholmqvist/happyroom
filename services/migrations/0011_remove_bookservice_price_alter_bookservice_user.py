# Generated by Django 4.2.11 on 2024-04-11 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('services', '0010_bookservice_price_alter_bookservice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookservice',
            name='price',
        ),
        migrations.AlterField(
            model_name='bookservice',
            name='user',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]