from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone

from .manager import CustomUserManager

from django.conf import settings


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_image = models.ImageField(default='user_picel.png', blank=True)

    username = models.CharField(_('نام کاربری'), max_length=150 , blank=True, null=True)
    
    email = models.EmailField(_('آدرس ایمیل'), unique=True)

    phone_number = models.CharField(
        _('شماره موبایل'),
        max_length=11,
        unique=True,
        validators=[RegexValidator(regex=r'09(\d{9})$')])
    phone_number_verified = models.BooleanField(_("تایید شماره موبایل"), default=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
    )

    email_verified = models.BooleanField(
        _('تایید ایمیل'),
        default=False,
    )

    is_teacher = models.BooleanField(
        _('مدرس بودن کاربر'),
        default=False,
    )


    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    forget_password_token = models.CharField( max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)