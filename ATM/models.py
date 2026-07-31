from django.db import models
from home.models import Course, Course_Faze
from django.conf import settings


# Create your models here.
class Payment_Course_Data(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    RefId = models.CharField(max_length=50, blank=True, null=True)
    is_success = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone_number


class Payment_Faze_Data(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    faze = models.ForeignKey(Course_Faze, on_delete=models.CASCADE)
    price = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    RefId = models.CharField(max_length=50, blank=True, null=True)
    is_success = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone_number


class ConsultationRequest(models.Model):
    FULLNAME_MAX_LENGTH = 100
    EMAIL_MAX_LENGTH = 100
    PHONE_NUMBER_MAX_LENGTH = 11

    fullname = models.CharField(max_length=FULLNAME_MAX_LENGTH)
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    phone_number = models.CharField(max_length=PHONE_NUMBER_MAX_LENGTH)
    consultation_type = models.CharField(max_length=50)
    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    authority = models.CharField(max_length=100, blank=True, null=True)  # افزودن فیلد برای ذخیره authority

    def __str__(self):
        return self.fullname
