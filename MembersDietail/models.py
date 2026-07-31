from django.db import models
from django.conf import settings


# Create your models here.
class Our_Member(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='عضو')
    small_description = models.CharField(max_length=400, null=False, blank=False, verbose_name='توضیحات پیش نمایش')
    slug = models.SlugField(max_length=150, null=False, blank=False, verbose_name='اسلاگ',
                            help_text='حتما باید با حروف انگلیسی باشه و بین حروف اسپیس نباشه این نکته خیلی مهمه')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = "عضو های مجموعه"
        verbose_name = "عضو ها"


class Member_Cantact_Way(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='عضو')
    name_way = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام راه ارتباطی')
    way = models.CharField(max_length=400, null=False, blank=False, verbose_name=' راه ارتباطی')

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = "راه های ارتباطی با اعضا"
        verbose_name = "راه ارتباطی"
