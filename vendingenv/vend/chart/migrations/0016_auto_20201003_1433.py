# Generated by Django 2.1.5 on 2020-10-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0015_alert_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='check',
            field=models.BooleanField(default=False),
        ),
    ]