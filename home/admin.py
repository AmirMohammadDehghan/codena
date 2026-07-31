from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.MainSlider)


# admin.site.register(models.Course)
@admin.register(models.Course)
class Courses(admin.ModelAdmin):
    search_fields = ("name", 'teacher', 'description', 'original_price')
    list_filter = ('name', 'teacher', 'trending', 'status', 'original_price',)
    list_display = ('name', 'teacher', 'trending', 'status', 'original_price',)


admin.site.register(models.Discount)


# admin.site.register(models.Course_Faze)
@admin.register(models.Course_Faze)
class Courses_Faze(admin.ModelAdmin):
    search_fields = ("name", 'course', 'selling_price', 'original_price')
    list_filter = ('name', 'course', 'original_price', 'is_free')
    list_display = ('name', 'course', 'original_price', 'is_free')


@admin.action(description='فعال کردن تیک اپلود از گوگل درایو برای تمام قسمت ها')
def is_google_drive_to_true(modeladmin, request, queryset):
    for a in queryset:
        a.is_google_drive = True
        a.save()


# admin.site.register(models.Course_Sections)
@admin.register(models.Course_Sections)
class Courses_Sections(admin.ModelAdmin):
    search_fields = ("section_name", 'course_season')
    list_filter = ('section_name', 'course_season', 'is_free')
    list_display = ('section_name', 'course_season', 'is_free')
    actions = [is_google_drive_to_true]


# admin.site.register(models.Course_Seasons)


@admin.register(models.Course_Seasons)
class Courses_Seasons(admin.ModelAdmin):
    search_fields = ("name", 'course_faze')
    list_filter = ('name', 'course_faze', 'is_free')
    list_display = ('name', 'course_faze', 'is_free')


admin.site.register(models.Course_Selled)
admin.site.register(models.Faze_Selled)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'course', 'parent', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author__username', 'text')


admin.site.register(models.Course_Comment, CommentAdmin)


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('author', 'course', 'title', 'course_ep', 'parent', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author__username', 'text')


admin.site.register(models.Tickets, TicketsAdmin)
admin.site.register(models.Ticket_Uploader)
admin.site.register(models.Search)
