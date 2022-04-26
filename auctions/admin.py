from django.contrib import admin

from .models import *

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','created_time', 'user', 'category', 'active')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','first_name','last_name', 'email')

# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('id','image')


admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid)
# admin.site.register(Category)
admin.site.register(Comment)
# admin.site.register(Image)
