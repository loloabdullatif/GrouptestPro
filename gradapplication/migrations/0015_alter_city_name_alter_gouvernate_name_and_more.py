# Generated by Django 4.2.5 on 2023-09-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradapplication', '0014_city_gouvernate_street'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='gouvernate',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(default='', max_length=10),
        ),
    ]