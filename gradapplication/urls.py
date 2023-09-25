from django.urls import path
from gradapplication import views
    
    
urlpatterns=[path("", views.farms, name="index"),
    ]
