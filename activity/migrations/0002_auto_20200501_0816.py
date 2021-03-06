# Generated by Django 3.0.5 on 2020-05-01 08:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='participants',
            field=models.IntegerField(db_index=True, validators=[django.core.validators.MinValueValidator]),
        ),
        migrations.AlterField(
            model_name='activity',
            name='type',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
