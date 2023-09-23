# Generated by Django 4.2.5 on 2023-09-23 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gradapplication', '0022_amenities_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to=None)),
                ('PublicPlaceId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.publicplace')),
            ],
        ),
    ]
