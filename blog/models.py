from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    course_related = models.ForeignKey('home.Course', on_delete=models.SET_NULL, null=True, verbose_name='دوره مرتبت')
    slug = models.SlugField(max_length=150, null=False, blank=False, verbose_name='اسلاگ',
                            help_text='حتما باید با حروف انگلیسی باشه و بین حروف اسپیس نباشه این نکته خیلی مهمه')
    trending = models.BooleanField(default=False, verbose_name='پست برگزیده هفته')
    is_podcast = models.BooleanField(default=False, verbose_name='پادکست بودن')
    body = models.TextField(verbose_name='پیشگفتار')
    content = RichTextField(verbose_name='محتوای اصلی')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نوشتن')
    image = models.ImageField(default='default.jpg', blank=True, verbose_name='عکس اصلی مقاله')

    anthor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="نویسنده")
    meta_title = models.CharField(max_length=150, default='data', blank=True, null=True, verbose_name='متا تایتل',
                                  help_text='تمام فیلد هایی که با متا نام گذاری شده اند برای مباحس سئو استفاده می شوند با دقت پر کنید')
    meta_description = models.TextField(max_length=600, default='data', blank=True, null=True,
                                        verbose_name='متا توضیحات')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[0:140]

    class Meta:
        verbose_name_plural = 'پست های وبلاگ'
        verbose_name = 'پست های وبلاگ'


class Podcast(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=150, null=False, blank=False, verbose_name='اسلاگ',
                            help_text='حتما باید با حروف انگلیسی باشه و بین حروف اسپیس نباشه این نکته خیلی مهمه')
    length = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='تایم پادکست')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name="نویسنده")
    body = models.TextField(verbose_name='پیشگفتار')
    related_post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, verbose_name='پست مرتبط')
    audio_link = models.URLField(max_length=500)
    image = models.ImageField(default='default.jpg', blank=True, verbose_name='عکس اصلی مقاله')
    meta_title = models.CharField(max_length=150, default='data', blank=True, null=True, verbose_name='متا تایتل',
                                  help_text='تمام فیلد هایی که با متا نام گذاری شده اند برای مباحس سئو استفاده می شوند با دقت پر کنید')
    meta_description = models.TextField(max_length=600, default='data', blank=True, null=True,
                                        verbose_name='متا توضیحات')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ نوشتن')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'پادکست های وبلاگ'
        verbose_name = 'پادکست های وبلاگ'


class Blog_Slider(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام اسلاید')
    image = models.ImageField(null=False, blank=False, verbose_name='عکس اسلاید')
    link = models.CharField(max_length=250, verbose_name='لینک پیوست شده به اسلاید')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'اسلایدر وبلاگ'
        verbose_name = 'اسلایدر وبلاگ'
