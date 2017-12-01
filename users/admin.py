from django.contrib import admin
from .models import users


class UsersAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'phno','address','city')
    search_fields = ('name', 'email','phno')
    list_filter = ('city','pincode')

admin.site.register(users, UsersAdmin)
# Register your models here.
