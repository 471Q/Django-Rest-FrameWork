# Generated by Django 3.2.5 on 2021-07-16 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='slug',
        ),
    ]