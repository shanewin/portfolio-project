# Generated by Django 2.2 on 2020-04-25 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200123_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='summary',
            field=models.CharField(max_length=10000),
        ),
    ]
