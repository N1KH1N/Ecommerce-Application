# Generated by Django 4.1.4 on 2023-02-06 07:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='expected_deliverydate',
            field=models.DateField(default=datetime.date(2023, 2, 11)),
        ),
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(max_length=1200),
        ),
    ]