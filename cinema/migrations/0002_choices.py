# Generated by Django 2.0.1 on 2018-02-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_choice', models.CharField(choices=[('M1', 'Hello'), ('M2', 'Hey'), ('M3', 'Hi')], default='M1', max_length=10)),
            ],
        ),
    ]