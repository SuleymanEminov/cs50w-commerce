from django.contrib import admin

from .models import User, Listing, Comment, Category, Bid
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','created_time', 'user', 'active')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username','first_name','last_name', 'email')


admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid)
admin.site.register(Category)
admin.site.register(Comment)
