from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerlamp/',views.powerbulb,name="powerlamp"),
    path('',views.powerbulb,name="powerlamp")
]