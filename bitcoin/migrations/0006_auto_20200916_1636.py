# Generated by Django 3.1.1 on 2020-09-16 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0005_bitcoin_assert_id_quote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitcoin',
            name='time',
            field=models.CharField(default='', max_length=100),
        ),
    ]
