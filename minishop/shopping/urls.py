
from django.urls import path,include
from .import views
urlpatterns = [  
    path('',views.loadindex,name='loadindex'),    
    path('search',views.searching,name='search'),
    path('loadblog',views.loadblog,name='loadblog'),
    path('loadabout',views.loadabout,name='loadabout'),
    path('loadcontact',views.loadcontact,name='loadcontact'),
    
    path('loadshop',views.loadshop,name='loadshop'),
    path('<slug:cname>/<slug:pname>/',views.loadsinglepost,name='loadsinglepost'), 
    path('<slug:c_slug>',views.loadindex,name='product-cat'),
    # path('<int:id>',views.loadsinglepost,name='loadsinglepost'), 
   
   
]



