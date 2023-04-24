# Generated by Django 4.1.1 on 2022-10-07 02:30

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(default=0, validators=[main.models.distinct_one_hundred_percent]),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(validators=[main.models.greater_than_zero]),
        ),
    ]
