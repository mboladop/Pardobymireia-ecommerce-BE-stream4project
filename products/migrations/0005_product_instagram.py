# Generated by Django 2.0.6 on 2018-08-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20180820_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='instagram',
            field=models.TextField(default=''),
        ),
    ]
