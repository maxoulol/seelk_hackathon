# Generated by Django 3.1.1 on 2020-09-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('assert_id_base', models.CharField(max_length=100)),
                ('assert_id_quote', models.CharField(max_length=100)),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
