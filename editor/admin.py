from django.contrib import admin
from .models import PythonEditorModel

@admin.register(PythonEditorModel)
class PythonEditorModelAdmin(admin.ModelAdmin):
    list_display = ('user',)  # فیلدهایی که در لیست نمایش داده می‌شوند
    search_fields = ('user__username', 'text_field')  # فیلدهایی که در جستجو پیشرفته نمایش داده می‌شوند