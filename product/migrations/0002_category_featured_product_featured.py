# Generated by Django 5.1.7 on 2025-03-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
