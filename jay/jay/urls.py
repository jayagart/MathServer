from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerofalamp/',views.powerbulb,name="powerofalamp"),
    path('',views.powerbulb,name="powerofalamp")
]
