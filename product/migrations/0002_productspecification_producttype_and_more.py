# Generated by Django 5.1.1 on 2025-03-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='product',
            name='vendor',
        ),
        migrations.RemoveField(
            model_name='productvariant',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.CharField(choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=20),
        ),
    ]
