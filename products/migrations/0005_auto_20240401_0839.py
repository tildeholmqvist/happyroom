# Generated by Django 3.2.25 on 2024-04-01 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_subcategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Sub categories'},
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='products.SubCategory'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, related_name='products', to='products.Category'),
        ),
    ]
