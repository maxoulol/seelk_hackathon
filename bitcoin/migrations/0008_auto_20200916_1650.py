# Generated by Django 3.1.1 on 2020-09-16 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0007_auto_20200916_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitcoin',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='bitcoin',
            name='time',
        ),
    ]