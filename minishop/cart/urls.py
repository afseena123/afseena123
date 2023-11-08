from django.urls import path,include
from .import views
urlpatterns = [  
    path('loadcart',views.loadcart,name='loadcart'),
    path('add/<int:pid>/',views.addcart,name='addcart'),
    path('mincart/<int:product_id>',views.min_cart,name='min_cart'),
    path('deletecart/<int:product_id>',views.cart_delete,name='cart_delete'),
    path('checkout', views.checkout, name='checkout'),
    path('payment', views.payment, name='payment'),
   
]
    

   

