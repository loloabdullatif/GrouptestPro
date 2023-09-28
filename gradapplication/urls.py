from django.urls import path
from gradapplication import views
    
    
urlpatterns=[path("", views.farms, name="index"),
            path('create_account/', views.create_account, name='create_account'),
            path('login/', views.login_view, name='login')
    ]
