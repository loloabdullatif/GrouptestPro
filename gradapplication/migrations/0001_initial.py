# Generated by Django 4.2.5 on 2023-09-25 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('hotel', 'Hotel'), ('restaurant', 'Restaurant'), ('farm', 'Farm')], max_length=20)),
                ('freeParking', models.BooleanField(default=False)),
                ('bar', models.BooleanField(default=False)),
                ('currencyExchange', models.BooleanField(default=False)),
                ('twintyFourHoursFrontDesk', models.BooleanField(default=False)),
                ('carRental', models.BooleanField(default=False)),
                ('airportDropOff', models.BooleanField(default=False)),
                ('cleaningServices', models.BooleanField(default=False)),
                ('laundryServices', models.BooleanField(default=False)),
                ('dryCleaning', models.BooleanField(default=False)),
                ('ATM', models.BooleanField(default=False)),
                ('faxCopyingServices', models.BooleanField(default=False)),
                ('firstAidServices', models.BooleanField(default=False)),
                ('wifi', models.BooleanField(default=False)),
                ('bbq', models.BooleanField(default=False)),
                ('multiBathrooms', models.BooleanField(default=False)),
                ('solarHeater', models.BooleanField(default=False)),
                ('towels', models.BooleanField(default=False)),
                ('multiRooms', models.BooleanField(default=False)),
                ('filteredPool', models.BooleanField(default=False)),
                ('toy', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Governate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PublicPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('hotel', 'Hotel'), ('restaurant', 'Restaurant'), ('farm', 'Farm')], max_length=20)),
                ('phoneNumber', models.CharField(default='', max_length=10)),
                ('rating', models.IntegerField(default=1)),
                ('area', models.FloatField(default='', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'public places',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomType', models.CharField(choices=[('single', 'single'), ('double', 'double'), ('vipRoom', 'vipRoom'), ('studio', 'studio')], default=None, max_length=10)),
                ('price', models.FloatField(default='', max_length=10)),
                ('roomNumber', models.IntegerField(default=1)),
                ('bedType', models.CharField(choices=[('single', 'single'), ('double', 'double')], max_length=10)),
                ('area', models.FloatField(default='', max_length=20)),
                ('numberOfPeople', models.IntegerField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableNumber', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TableBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default='', max_length=20)),
                ('checkInTime', models.DateTimeField(blank=True, null=True)),
                ('checkoutTime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='', max_length=255, unique=True)),
                ('phoneNumber', models.CharField(default='', max_length=10)),
                ('password', models.CharField(default='', max_length=10)),
                ('nationalNumber', models.CharField(default='', max_length=15, unique=True)),
                ('birthDate', models.DateField()),
                ('isOwner', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('publicplace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gradapplication.publicplace')),
                ('rentType', models.CharField(choices=[('daily', 'Daily'), ('monthly', 'Monthly')], max_length=30)),
            ],
            options={
                'verbose_name_plural': 'farms',
            },
            bases=('gradapplication.publicplace',),
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('publicplace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gradapplication.publicplace')),
                ('numberOfRooms', models.IntegerField(default=1)),
                ('numberOfStars', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name_plural': 'hotels',
            },
            bases=('gradapplication.publicplace',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('publicplace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gradapplication.publicplace')),
                ('openTime', models.TimeField()),
                ('menuType', models.CharField(default='', max_length=500)),
            ],
            options={
                'verbose_name_plural': 'restaurants',
            },
            bases=('gradapplication.publicplace',),
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10)),
                ('cityId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.city')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublicPlaceId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.publicplace')),
                ('amenityId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.amenities')),
            ],
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default='', max_length=20)),
                ('checkInDate', models.DateField(default=datetime.date.today)),
                ('checkoutDate', models.DateField(default=datetime.date.today)),
                ('roomId', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='roomId', to='gradapplication.room')),
                ('userId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.user')),
            ],
        ),
        migrations.AddField(
            model_name='publicplace',
            name='streetId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.street'),
        ),
        migrations.AddField(
            model_name='publicplace',
            name='userId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.user'),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.ImageField(upload_to=None)),
                ('PublicPlaceId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.publicplace')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='governateId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.governate'),
        ),
        migrations.AddField(
            model_name='room',
            name='hotelId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.hotel'),
        ),
        migrations.CreateModel(
            name='FarmBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default='', max_length=20)),
                ('checkInDate', models.DateField(default=datetime.date.today)),
                ('checkoutDate', models.DateField(default=datetime.date.today)),
                ('userId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.user')),
                ('farmId', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='gradapplication.farm')),
            ],
        ),
    ]
