# Generated by Django 2.0.1 on 2018-04-22 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0009_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='theatre_name',
        ),
    ]
