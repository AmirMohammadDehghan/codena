from django.db import models
from ckeditor.fields import RichTextField
from home.models import Course


# Create your models here.
class RoadMaps(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام رودمپ')
    small_description = models.CharField(max_length=150, null=False, blank=False, verbose_name='توضیحات پیش نمایش')
    image = models.TextField(null=False, blank=False, verbose_name='عکس ایکون رودمپ')
    main_image = models.ImageField(null=True, blank=False, verbose_name='عکس اصلی رودمپ')
    video_id = models.CharField(max_length=800, null=True, blank=False, verbose_name='آی دی ویدئو')
    cover_image = models.ImageField(null=True, blank=False, verbose_name='عکس پیش نمایش رودمپ')
    voice_id = models.CharField(max_length=800, null=True, blank=False, verbose_name='آی دی فایل صوتی ')
    description = RichTextField(verbose_name='توضیحات کامل درباره رودمپ', default='به زودی اضافه می گردد...')
    color = models.CharField(max_length=50, default='', verbose_name='رنگ رودمپ')
    is_discount = models.BooleanField(default=False,
                                      help_text='در صورت زدن این تیک تایمر تخفیف رودمپ فعال می شود',
                                      verbose_name='تایمر تخفیف رودمپ')
    discount_date = models.CharField(max_length=50, default='', verbose_name='تاریخ تخفیف رودمپ',
                                     help_text=' مثال:Dec 31, 2024 23:59:59')

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name_plural = "رودمپ ها"
        verbose_name = "رودمپ "


class RoadMapDetails(models.Model):
    roadmap = models.ForeignKey(RoadMaps, on_delete=models.CASCADE, verbose_name='رودمپ مورد نظر')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    course_number = models.IntegerField(null=False, blank=False, verbose_name='شماره دوره ')

    def __str__(self):
        return f'{self.course.name}'

    class Meta:
        verbose_name_plural = "دوره های هر رودمپ"
        verbose_name = "دوره های  رودمپ"


class TopQuestions(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='طرح سوال')
    description = RichTextField(verbose_name='توضیحات سوال', default='به زودی اضافه می گردد...')
    roadmap = models.ForeignKey(RoadMaps, on_delete=models.CASCADE, verbose_name='رودمپ مورد نظر', related_name='questions')