from django.contrib import admin

from gradapplication.models import User,PublicPlace,Hotel,Restaurant,Farm,Room,RoomBooking,FarmBooking,Table,TableBooking,City,Street,Governorate,Amenities,Service,MenuType
admin.site.register(User)
admin.site.register(PublicPlace)
admin.site.register(Hotel)
admin.site.register(Restaurant)
admin.site.register(Farm)
admin.site.register(Room)
admin.site.register(RoomBooking)
admin.site.register(FarmBooking)
admin.site.register(Table)
admin.site.register(Street)
admin.site.register(City)
admin.site.register(Governorate)
admin.site.register(Amenities)
admin.site.register(Service)
admin.site.register(MenuType)


# Register your models here.
