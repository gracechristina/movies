# Generated by Django 2.0.1 on 2018-03-20 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0006_theatre_theatre_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='photo',
            field=models.ImageField(default='', upload_to='list'),
            preserve_default=False,
        ),
    ]