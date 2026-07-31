from django.contrib import admin
from . import models


# Register your models here.
class TQInline(admin.StackedInline):
    model = models.TopQuestions
    extra = 1  # تعداد فرم‌های خالی اضافه برای اضافه کردن کامنت‌های جدید در اینلاین


@admin.register(models.RoadMaps)
class RoadMaps(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("name",)
    list_display = ("name",)
    inlines = [TQInline]


@admin.register(models.RoadMapDetails)
class RoadMapDetails(admin.ModelAdmin):
    search_fields = ("roadmap", 'course', 'course_number')
    list_filter = ("roadmap", 'course', 'course_number')
    list_display = ("roadmap", 'course', 'course_number')