# Generated by Django 3.2.5 on 2021-08-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='abv',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='bottle',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
