# Generated by Django 2.1.5 on 2020-10-03 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chart', '0018_auto_20201003_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sold1',
            options={'ordering': ('tagid',), 'verbose_name_plural': 'sold1'},
        ),
        migrations.AlterModelOptions(
            name='vend1',
            options={'ordering': ('tagid',), 'verbose_name_plural': 'vend1'},
        ),
        migrations.AlterModelOptions(
            name='vend2',
            options={'ordering': ('tagid',), 'verbose_name_plural': 'vend2'},
        ),
    ]