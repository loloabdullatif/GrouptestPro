# Generated by Django 4.2.5 on 2023-09-22 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradapplication', '0018_hotel_publicplacefk'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmbooking',
            name='date',
            field=models.TimeField(null=True),
        ),
    ]
