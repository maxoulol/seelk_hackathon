# Generated by Django 3.1.1 on 2020-09-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcoin', '0003_remove_bitcoin_assert_id_quote'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitcoin',
            name='assert_id_base',
            field=models.CharField(default='', max_length=100),
        ),
    ]
