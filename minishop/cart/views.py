from collections import UserList
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from . models import *
from shopping.models import *
from accounts.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

# session

def c_id(request):
    ct_id=request.session.session_key # Try to retrieve the ct_id from the session
    if not ct_id:
        ct_id=request.create()
    return ct_id



# decorator
@login_required(login_url='loadregister')
def addcart(request,pid):
    prod=prducts.objects.get(id=pid)
    user=request.user
    
    try:
        ct=cartlist.objects.get(cartid=c_id(request))

    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cartid=c_id(request),user=user)
        ct.save()

    try:
        c_items=cartitem.objects.get(product=prod,cart=ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
            prod.stock-=1
            prod.save()
        c_items.save()
    except cartitem.DoesNotExist:
        c_items=cartitem.objects.create(product=prod,quantity=1,cart=ct)
        c_items.save()    
    return redirect('loadcart')
















# def loadcart(request):
#     return render(request,'cart.html')

def loadcart(request,tot=0,count=0,cart_items=None,ct_items=None):
    try:
        user=request.user
        if user.is_authenticated:
            ct=cartlist.objects.filter(user=user)
        else:
            cartid= request.session.get('cartid')
            ct = cartlist.objects.filter(cartid=cartid)
        ct_items = cartitem.objects.filter(cart__in=ct, active=True)
        for i in ct_items:
            tot += (i.product.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        return HttpResponse("<script> alert('Empty Cart');window.location='/';</script>")
    return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})





@login_required(login_url='login')  # Change 'register' to 'login' if you want to redirect to the login page
def min_cart(request, product_id):
    user = request.user
    try:
        if user.is_authenticated:
            ct_list = cartlist.objects.filter(user=user)
        else:
            cartid = request.session.get('cartid')
            ct_list = cartlist.objects.filter(cartid=cartid)
        if ct_list.exists():
            for ct in ct_list:
                prod = get_object_or_404(prducts, id=product_id)
                try:
                    c_items = cartitem.objects.get(product=prod, cart=ct)
                    if c_items.quantity > 1:
                        c_items.quantity -= 1
                        c_items.save()
                    else:
                        c_items.delete()
                except cartitem.DoesNotExist:
                    pass
    except cartlist.DoesNotExist:
        pass
    return redirect('loadcart')






































@login_required(login_url='register')
def cart_delete(request,product_id):
    user = request.user
    try:
        if user.is_authenticated:
            ct_list=cartlist.objects.filter(user=user)
        else:
            cart_id=request.session.get('cartid')
            ct_list=cartlist.objects.filter(cartid=cart_id)
        if ct_list.exists():
            for ct in ct_list:
                prod = get_object_or_404(prducts,id=product_id)
                try:
                    c_items=cartitem.objects.get(product=prod,cart=ct)
                    c_items.delete()
                except cartitem.DoesNotExist:
                    pass
    except cartlist.DoesNotExist:
        pass
    return redirect('loadcart')


 
def checkout(request):
    if request.method == "POST":

        # Retrieve data from the form
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        country = request.POST.get('Country', '')
        streetaddress = request.POST.get('streetaddress', '')
        apartment = request.POST.get('apartment', '')
        towncity = request.POST.get('towncity', '')
        postcodezip = request.POST.get('postcodezip', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('emailaddress', '')

        # Create a new Person object with the data
        person = Checkout(
            user=request.user,
            firstname=firstname,
            lastname=lastname,
            country=country,
            address=streetaddress,
            
            towncity=towncity,
            postcodezip=postcodezip,
            phone=phone,
            email=email
        )

        # Save the person's details to the database
        person.save()

     
        return redirect('payment.html')  

   
    return render(request, 'checkout.html')



 
def payment(request):
    if request.method == 'POST':
        
        account_number = request.POST.get('account_number')
        name= request.POST.get('name')
        expiry_month = request.POST.get('expiry_month')
        cvv = request.POST.get('cvv')

        p=payment(
            user=request.user,
            account_number=account_number,
            name=name,
            expiry_month=expiry_month,
            cvv=cvv,

        )
        p.save()

        user=request.user
        ct=cartlist.objects.get(user=user,cartid=c_id(request))
        cartitem.objects(cart=ct).delete()
        return redirect('sucsess.html')  

    return render(request,'payment.html') 


