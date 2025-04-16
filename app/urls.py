from django.urls import path,include

from app import views

urlpatterns=[
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.index,name='index'),
    path('Services/',views.Services,name='Services'),
    path('Contactus/',views.Contactus,name='Contactus'),
    path('LocalMoving/',views.LocalMoving,name='LocalMoving'),
    path('Longdistance/',views.Longdistance,name='Longdistance'),
    path('CommercialMoving/',views.CommercialMoving,name='CommercialMoving'),
    path('Storage/',views.Storage,name='Storage'),
    path('Packunpacking/',views.Packunpacking,name='Packunpacking'),
    path('Petrelocation/',views.Petreloctaion,name='Petrelocation'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('aboutus/',views.aboutus,name='aboutus'),
]