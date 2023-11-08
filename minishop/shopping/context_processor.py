from .views import *

from cart.views import *



def categ(request):
    obj=category.objects.all()
    return {'d':obj}    




def cart_total(request):
    tot=0
    count=0
    user=request.user
    if user.is_authenticated:
        ct = cartlist.objects.filter(user=user)
    else:
        cart_id=request.session.get('cartid')
        ct=cartlist.objects.filter(cartid=cart_id)
    ct_items=cartitem.objects.filter(cart__in=ct,active=True)
    for i in ct_items:
        tot += (i.product.price * i.quantity)
        count += i.quantity
    return {'t' : tot, 'cn':count}
    
