# Generated by Django 5.0.4 on 2024-04-20 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_category_alter_product_brand_delete_shirt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
