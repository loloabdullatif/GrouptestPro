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
    userId = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    placeType = (
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('farm', 'Farm')
    )

    name = models.CharField(max_length=255)
    #location = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=placeType)
    phoneNumber=models.CharField( max_length=10,default="")
    rating=models.IntegerField(default=1)
    area=models.FloatField(max_length=20,default="")

    class Meta:
        verbose_name_plural = 'public places'

    def __str__(self):
        return self.name


class Hotel(PublicPlace):
    #publicPlaceId = models.OneToOneField(PublicPlace, on_delete=models.CASCADE,related_name="publicPlaceId",default=None)
    # hotel_specific_attribute = models.CharField(max_length=255)
    numberOfRooms=models.IntegerField(default=1)
    numberOfStars=models.IntegerField(default=1)
    #placeFK = models.ForeignKey(PublicPlace, on_delete=models.CASCADE)



    class Meta:
        verbose_name_plural = 'hotels'


class Restaurant(PublicPlace):
    #restaurant_specific_attribute = models.CharField(max_length=255)
    openTime=models.TimeField()
    menuType=models.CharField(max_length=500,default="")
    

    class Meta:
        verbose_name_plural = 'restaurants'


class Table(models.Model):
    tableNumber=models.IntegerField(default=1)
    
class TableBooking(models.Model):
    price=models.FloatField(max_length=20,default="")
    checkInTime=models.DateTimeField(null=True,blank=True)
    checkoutTime=models.DateTimeField(null=True,blank=True)

class MenuType(models.Model):
    restaurantId= models.ForeignKey(Restaurant, on_delete=models.CASCADE,default=None)
    menuTypeList = (
        ('Tasting Menu', 'Tasting Menu'),
        ('Buffet Menu', 'Buffet Menu'),
        ('Specials Menu', 'Specials Menu'),
        ('Beverage Menu', 'Beverage Menu'),
        ('Kids Menu', 'Kids Menu')
    )
    menuType= models.CharField(max_length=30,choices=menuTypeList)


class Farm(PublicPlace):
    os_choice=(('daily' , 'Daily'),
                ('monthly' , 'Monthly'))
    # farm_specific_attribute = models.CharField(max_length=255)
    rentType= models.CharField(max_length=30,choices=os_choice)


    class Meta:
        verbose_name_plural = 'farms'
        
class Room(models.Model):
    hotelId=models.ForeignKey(Hotel, on_delete=models.CASCADE,default=None)
    roomTypes=(('single' , 'single'),
                ('double' , 'double'),
                ('vipRoom','vipRoom'),
                ('studio','studio'))
    roomType=models.CharField(max_length=10,choices=roomTypes,default=None)
    price=models.FloatField(max_length=10,default='')
    roomNumber=models.IntegerField(default=1)
    bedTypes=(('single' , 'single'),
                ('double' , 'double'))
    bedType=models.CharField(max_length=10,choices=bedTypes)
    area=models.FloatField(max_length=20,default="")
    numberOfPeople=models.IntegerField(default='')


class RoomBooking(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    roomId = models.OneToOneField(Room, on_delete=models.CASCADE,related_name="roomId",default=None)

    price=models.FloatField(max_length=20,default="")
    checkInDate=models.DateField(default=datetime.date.today)
    checkoutDate=models.DateField(default=datetime.date.today)

class FarmBooking(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    farmId = models.OneToOneField(Farm, on_delete=models.CASCADE,default=None)

    price=models.FloatField(max_length=20,default="")
    checkInDate=models.DateField(default=datetime.date.today)
    # date=models.TimeField(null=True)
    checkoutDate=models.DateField(default=datetime.date.today)


class Street(models.Model):
    PublicPlaceId = models.ForeignKey(PublicPlace, on_delete=models.CASCADE,default=None)
    name=models.CharField(default='',max_length=10)

class City(models.Model):
    streetId = models.ForeignKey(Street, on_delete=models.CASCADE,default=None)
    name=models.CharField(default='',max_length=10)

class Governorate(models.Model):
    cityId = models.ForeignKey(City, on_delete=models.CASCADE,default=None)
    name=models.CharField(default='',max_length=10)
    


class Amenities(models.Model):
    name=models.CharField(default='',max_length=10)
    placeType = (
        ('hotel', 'Hotel'),
        ('restaurant', 'Restaurant'),
        ('farm', 'Farm')
    )
    type = models.CharField(max_length=20, choices=placeType)
    freeParking =models.BooleanField(default=False)
    bar=models.BooleanField(default=False)
    currencyExchange=models.BooleanField(default=False)
    twintyFourHoursFrontDesk=models.BooleanField(default=False)
    carRental=models.BooleanField(default=False)
    airportDropOff=models.BooleanField(default=False)
    cleaningServices=models.BooleanField(default=False)
    laundryServices=models.BooleanField(default=False)
    dryCleaning=models.BooleanField(default=False)
    ATM=models.BooleanField(default=False)
    faxCopyingServices=models.BooleanField(default=False)
    firstAidServices=models.BooleanField(default=False)
    wifi=models.BooleanField(default=False)
    bbq=models.BooleanField(default=False)
    multiBathrooms=models.BooleanField(default=False)
    solarHeater=models.BooleanField(default=False)
    towels=models.BooleanField(default=False)
    multiRooms=models.BooleanField(default=False)
    filteredPool=models.BooleanField(default=False)
    toy=models.BooleanField(default=False)
    
    
class Service(models.Model):
    PublicPlaceId = models.ForeignKey(PublicPlace, on_delete=models.CASCADE,default=None)
    amenityId = models.ForeignKey(Amenities, on_delete=models.CASCADE,default=None)


class Images(models.Model):
    PublicPlaceId = models.ForeignKey(PublicPlace, on_delete=models.CASCADE,default=None)
    path=models.ImageField(upload_to=None,max_length=None)



