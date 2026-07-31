from django.contrib import admin
from . import models


# Register your models here.


# admin.site.register(models.Course)
@admin.register(models.Payment_Course_Data)
class Courses(admin.ModelAdmin):
    search_fields = ("user", 'course', 'price', 'status', 'is_success', 'created_at', 'RefId')
    list_filter = ("user", 'course', 'price', 'status', 'is_success', 'created_at', 'RefId')
    list_display = ("user", 'course', 'price', 'status', 'is_success', 'created_at', 'RefId')


@admin.register(models.Payment_Faze_Data)
class Faze(admin.ModelAdmin):
    search_fields = ("user", 'faze', 'price', 'status', 'is_success', 'created_at', 'RefId')
    list_filter = ("user", 'faze', 'price', 'status', 'is_success', 'created_at', 'RefId')
    list_display = ("user", 'faze', 'price', 'status', 'is_success', 'created_at', 'RefId')


class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone_number', 'consultation_type', 'amount', 'is_paid', 'authority', 'created_at')
    list_filter = ('consultation_type', 'is_paid', 'authority')
    search_fields = ('fullname', 'email', 'phone_number', 'authority')
    readonly_fields = ('amount', 'created_at')


admin.site.register(models.ConsultationRequest, ConsultationRequestAdmin)
