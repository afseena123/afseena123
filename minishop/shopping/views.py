from django.shortcuts import render,get_object_or_404
from . models import *

from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,InvalidPage



# Create your views here.
def loadindex(request,c_slug=None):
     #For Displaying  
     c=None #CAtegory
     obj1=None #Products
     if c_slug != None:
         c=get_object_or_404(category,slug=c_slug)
         obj1=prducts.objects.filter(category=c,availablility=True) #category is F.K,availability is field name of that table
     else:
         obj1=prducts.objects.all().filter(availablility=True)  
     obj=category.objects.all() 


# ---------------------Paginator-----------------
     paginator=Paginator(obj1,3)    # No: of objects that u want to display in ur page 

    #  try:
     page=int(request.GET.get('page',1))      
    #  except:
        # print("something went wrong")
        # page=1

     try:
        pro=paginator.page(page)

     except(EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
        # print('Hai',pro)
        
    

# -------------------------------------------------


     return render(request,'index.html',{'d':obj,'d1':obj1,'pr':pro})


def searching(request):
    if 'q' in request.GET:
        sn=request.GET.get('q')
        if sn:
            print("hai")
            p=prducts.objects.all().filter(Q(pname__icontains=sn)|Q(description__icontains=sn),availablility=True)
            return render(request,'search.html',{'pd':p})
        else:
            return render(request,'search.html',{})
        
              


# def loadsinglepost(request,id):  
#     obj1=get_object_or_404(prducts,pk=id)  #pk keyword,Prducts=Table
#     return render(request,'product-single.html',{'d1':obj1})



def loadsinglepost(request,cname,pname): 

    p=prducts.objects.get(category__slug=cname,slug=pname)  #category__slug is fk of prducts table
    c={'d1':p}
    return render(request,'product-single.html',c)

    
# views.py

    







def loadblog(request):
    
    return render(request,'blog.html')

def loadabout(request):
    
    return render(request,'about.html')

def loadcontact(request):
    
    return render(request,'contact.html')


def loadshop(request):
    
    return render(request,'shop.html')



