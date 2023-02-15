from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(qgenerator)
# admin.site.register(tablebook)
# admin.site.register(email_post)
admin.site.register(cityies)
admin.site.register(payment)
admin.site.register(rooms)
admin.site.register(creatuser)
admin.site.register(weekenddeals)

@admin.register(Tours)
class tourAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'amount', 'city', 'availble_date')
    search_fields = ["hotel_name"]
    
@admin.register(tourbooking)
class tourbookingAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','checkindate','checkoutdate')


@admin.register(favoritedestination)
class favoritedestinationAdmin(admin.ModelAdmin):
    list_disply=('destinations_name','description', 'destination_img')
