# Generated by Django 3.0 on 2020-12-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myp1', '0002_auto_20201202_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='new1',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
