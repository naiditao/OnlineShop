# Generated by Django 5.0.4 on 2024-04-10 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_brand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shirt',
            name='brand',
        ),
    ]
