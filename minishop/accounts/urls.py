from django.urls import path,include
from .import views
urlpatterns = [  
    path('loadlogin',views.loadlogin,name='loadlogin'),
    path('loadregister',views.loadregister,name='loadregister'),
    path('loadlogout',views.loadlogout,name='loadlogout'),
   
]
