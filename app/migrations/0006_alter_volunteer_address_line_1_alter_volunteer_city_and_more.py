# Generated by Django 5.1.1 on 2024-10-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_address_county_remove_volunteer_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='address_line_1',
            field=models.CharField(default='PLACEHOLDER', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='county',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='zipcode',
            field=models.CharField(max_length=10),
        ),
    ]
