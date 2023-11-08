from django.contrib import admin
from .models import category
from .models import prducts

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display = ['name','slug']  #display in admin dashboard



class productAdmin(admin.ModelAdmin):
    list_display = ['pname','slug','price','stock','image','availablility']
    list_editable = ['price','stock','image','availablility']
    prepopulated_fields={'slug':('pname',)}


admin.site.register(category,categoryAdmin)
admin.site.register(prducts,productAdmin)
