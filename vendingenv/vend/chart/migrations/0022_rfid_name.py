# Generated by Django 2.1.5 on 2021-03-03 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0021_rfid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rfid',
            name='name',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
