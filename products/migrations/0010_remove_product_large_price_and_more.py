# Generated by Django 4.2.11 on 2024-04-15 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_large_price_alter_product_medium_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='large_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='medium_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='small_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='xlarge_price',
        ),
    ]
