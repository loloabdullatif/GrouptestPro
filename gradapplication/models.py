import datetime
import enum
from django.db import models
from django.forms import DateTimeField 
from model_utils.managers import InheritanceManager
#from enumfields import EnumField
from enum import Enum

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=255,default="")
    lastname = models.CharField(max_length=255,default="")
    phoneNumber=models.CharField( max_length=10,default="")
    password=models.CharField(max_length=10,default="")
    nationalNumber=models.CharField(max_length=15,default="")
    birthDate=models.DateField()
    isOwner=models.BooleanField()
    
    
class PublicPlace(models.Model):
    PLACE_TYPES = (
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('farm', 'Farm')
    )

    name = models.CharField(max_length=255)
    #location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=PLACE_TYPES)
    phoneNumber=models.CharField( max_length=10,default="")
    rate=models.IntegerField(max_length=20,default=1)
    area=models.FloatField(max_length=20,default="")

    class Meta:
        verbose_name_plural = 'public places'

    def __str__(self):
        return self.name


class Hotel(PublicPlace):
   # hotel_specific_attribute = models.CharField(max_length=255)
    numberOfRooms=models.IntegerField(default=1)
    numberOfStars=models.IntegerField(default=1)
    #placeFK = models.ForeignKey(PublicPlace, on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural = 'hotels'


class Restaurant(PublicPlace):
    #restaurant_specific_attribute = models.CharField(max_length=255)
    openTime=models.DateField()
    menuType=models.CharField(max_length=20,default="")
    

    class Meta:
        verbose_name_plural = 'restaurants'


class Table(models.Model):
    tableNumber=models.IntegerField(default=1,max_length=50)
    
class TableBooking(models.Model):
    price=models.FloatField(max_length=20,default="")
    checkin=models.DateTimeField(null=True,blank=True)
    checkout=models.DateTimeField(null=True,blank=True)


class Farm(PublicPlace):
    os_choice=(('Daily' , 'daily'),
                ('Monthly' , 'monthly'))
    # farm_specific_attribute = models.CharField(max_length=255)
    rentType= models.CharField(max_length=10,choices=os_choice)


    class Meta:
        verbose_name_plural = 'farms'
        
class Room(models.Model):
    typeRoom=(('single' , 'single'),
                ('double' , 'double'),
                ('vip_room','vip_room'),
                ('studio','studio'))
    type_room=models.CharField(max_length=10,choices=typeRoom)
    price=models.FloatField(max_length=10,default='')
    roomNumber=models.IntegerField(default=1)
    bedType=(('single' , 'single'),
                ('double' , 'double'))
    type_bed=models.CharField(max_length=10,choices=bedType)
    area=models.FloatField(max_length=20,default="")
    numberOfPerson=models.IntegerField(max_length=10,default='')


class RoomBooking(models.Model):
    price=models.FloatField(max_length=20,default="")
    checkin=models.DateField(default=datetime.date.today)
    checkout=models.DateField(default=datetime.date.today)

class FarmBooking(models.Model):
    price=models.FloatField(max_length=20,default="")
    checkin=models.DateField(default=datetime.date.today)
    checkout=models.DateField(default=datetime.date.today)


class Street(models.Model):
    name=models.CharField(default='',max_length=10)

class City(models.Model):
    name=models.CharField(default='',max_length=10)

class Gouvernate(models.Model):
    name=models.CharField(default='',max_length=10)

# class Images(models.Model):
#     path=models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)



