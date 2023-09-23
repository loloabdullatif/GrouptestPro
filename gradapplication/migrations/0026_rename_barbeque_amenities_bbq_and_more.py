# Generated by Django 4.2.5 on 2023-09-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradapplication', '0025_remove_amenities_firstaidservices_amenities_barbeque_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='amenities',
            old_name='barbeque',
            new_name='bbq',
        ),
        migrations.RemoveField(
            model_name='amenities',
            name='CcrRental',
        ),
        migrations.AddField(
            model_name='amenities',
            name='crRental',
            field=models.BooleanField(default=False),
        ),
    ]
