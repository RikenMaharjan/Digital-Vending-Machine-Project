# Generated by Django 2.1.5 on 2020-10-03 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0016_auto_20201003_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alert',
            name='check',
        ),
    ]