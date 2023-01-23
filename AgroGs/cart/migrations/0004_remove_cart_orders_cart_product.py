# Generated by Django 4.1.2 on 2023-01-23 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_products_cart'),
        ('cart', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='orders',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products', verbose_name='Product'),
        ),
    ]
