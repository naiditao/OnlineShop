# Generated by Django 5.0.4 on 2024-04-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shirt_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]