# Generated by Django 4.2.5 on 2023-09-21 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gradapplication', '0006_farmbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableNumber', models.IntegerField(default=1, max_length=50)),
            ],
        ),
    ]