from django.contrib import admin
from . import models
# Register your models here.
# admin.site.register(models.CustomUser)
@admin.register(models.CustomUser)
class CustomUser(admin.ModelAdmin):
    search_fields = ("phone_number",'username', 'email', 'date_joined')
    list_filter = ("phone_number",'username', 'email', 'phone_number_verified', 'is_staff', 'email_verified', 'is_teacher', 'date_joined')
    list_display = ("phone_number",'username', 'email', 'date_joined','phone_number_verified')
admin.site.register(models.Profile)



