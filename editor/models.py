from django.db import models
from django.conf import settings # اگر از مدل کاربران پیش‌فرض Django استفاده می‌کنید

class PythonEditorModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ForeignKey به کاربرها
    text_field = models.TextField()

    # def __str__(self):
    #     return self.user.username  # نمایش نام کاربر در مدل به عنوان نام آن