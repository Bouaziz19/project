# Generated by Django 2.0.9 on 2020-03-14 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200314_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log_res',
            name='star_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 26, 47, 647983)),
        ),
        migrations.AlterField(
            model_name='log_res',
            name='stop_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 14, 17, 26, 47, 648014)),
        ),
    ]
