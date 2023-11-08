from django.db import models
from django.urls import reverse
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return '{}'.format(self.name)
    
    def get_url(self):
        return reverse('product-cat',args=[self.slug])
    

class prducts(models.Model):
    pname=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='products')
    description=models.TextField()
    stock=models.IntegerField()
    availablility=models.BooleanField()
    price=models.IntegerField()
    date=models.DateTimeField()
    category=models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.pname)
    
    def get_url(self):
        return reverse('loadsinglepost',args=[self.category.slug,self.slug])   #category =f.k,loadsinglepost=urlname



