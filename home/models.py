from django.db import models
from ckeditor.fields import RichTextField

from django.conf import settings


class MainSlider(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام اسلاید')
    image = models.ImageField(null=False, blank=False, verbose_name='عکس اسلاید')
    link = models.CharField(max_length=250, verbose_name='لینک پیوست شده به اسلاید')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "اسلایدر"
        verbose_name = "اسلاید ها"


class Discount(models.Model):
    code = models.CharField(max_length=150, null=False, blank=False, verbose_name='کد تخفیف')
    percent = models.IntegerField(null=False, blank=False, verbose_name='درصد تخفیف')

    def __str__(self):
        return f'{self.percent} درصد تخفیف '

    class Meta:
        verbose_name_plural = "سیستم کد تخفیف"
        verbose_name = "سیستم کد تخفیف"


class Course(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False, verbose_name='اسلاگ',
                            help_text='حتما باید با حروف انگلیسی باشه و بین حروف اسپیس نباشه این نکته خیلی مهمه')
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام دوره')
    eitaa = models.CharField(max_length=250, null=True, verbose_name='لینک کانال ایتای دوره')
    course_weigth = models.CharField(max_length=50, null=False, default='0 ساعت', blank=False,
                                     verbose_name='زمان حدودی تمام قسمت های دوره')
    support = models.CharField(max_length=150, null=False, default='پشتیبانی دائمی', blank=False,
                               verbose_name='درباره پشتیبانی دوره')
    course_image = models.ImageField(null=False, verbose_name='عکس پیش نمایش دوره')
    introduction_video = models.FileField(upload_to='videos/', null=True, verbose_name="ویدیو معارفه ")
    small_description = models.CharField(max_length=800, null=False, blank=False, verbose_name='توضیحات پیش نمایش')
    description = RichTextField(verbose_name='توضیحات کامل دوره')
    original_price = models.IntegerField(null=False, blank=False, verbose_name='قیمت اصلی دوره')
    show_price = models.IntegerField(null=True, blank=False, verbose_name='قیمت نمایشی دوره')
    show_discount = models.IntegerField(null=True, blank=False, verbose_name='تخفیف نمایشی دوره')
    unable_buy = models.BooleanField(default=False,
                                        help_text='در صورت زدن این تیک دوره غیر قابل خرید می شود',
                                        verbose_name='غیر قابل خرید')
    is_price_show = models.BooleanField(default=False,
                                        help_text='در صورت زدن این تیک قیمت نمایشی این دوره به صورت خط خورده نمایش داده می شود',
                                        verbose_name='نمایش قیمت نمایشی')
    status = models.BooleanField(default=False, help_text='در صورت زدن این تیک توره به سورت رایگان نمایش داده می شود',
                                 verbose_name='رایگان بودن دوره')
    is_soft = models.BooleanField(default=False,
                                  help_text='در صورت زدن این تیک دوره در دسته نرم قرار میگیرد نمایش داده می شود',
                                  verbose_name='نرم بودن')
    is_discount = models.BooleanField(default=False,
                                      help_text='در صورت زدن این تیک تخیفیف ها روی این دوره اعمال می شود',
                                      verbose_name='اعمال تخفیف دوره')
    is_discount_timer = models.BooleanField(default=False,
                                            help_text='در صورت زدن این تیک تایمر تخفیف رودمپ فعال می شود',
                                            verbose_name='تایمر تخفیف رودمپ')
    discount_date = models.CharField(max_length=50, default='', verbose_name='تاریخ تخفیف رودمپ',
                                     help_text=' مثال:Dec 31, 2024 23:59:59')
    trending = models.BooleanField(default=False,
                                   help_text='در صورت زدن این تیک دوره در قسمت پیشنهاد های کدنا نمایش داده می شود',
                                   verbose_name='پیشنهاد های کدنا')
    is_fake_student = models.BooleanField(default=False,
                                          help_text='در صورت زدن این تیک تعداد دانش اموزان را به صورت فیک نمایش می دهد نمایش داده می شود',
                                          verbose_name='تیک دانش اموز فیک')
    fake_student = models.CharField(max_length=150, null=True, blank=True, verbose_name='تعداد دانش اموزان')
    fake_id = models.IntegerField(null=True, blank=False, verbose_name='ترتیب نمایش اخرین دوره ها')
    tag = models.CharField(max_length=150, null=False, blank=False, verbose_name='تگ های مرتبط به دوره')
    discount_code = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, verbose_name='درصد تخفیف دوره',
                                      help_text='برای استفاده از کد تخفیف اول باید یک کد تخفیف بسازید و بعد اینجا انتخابش کنید')
    temporary_discount_code = models.CharField(max_length=150, null=True, verbose_name='کد تخفیف موقت')
    meta_title = models.CharField(max_length=150, null=False, blank=False, verbose_name='متا تایتل',
                                  help_text='تمام فیلد هایی که با متا نام گذاری شده اند برای مباحس سئو استفاده می شوند با دقت پر کنید')
    meta_keywords = models.CharField(max_length=150, null=False, blank=False, verbose_name='متا کلمات کیلیدی')
    meta_description = models.TextField(max_length=600, null=False, blank=False, verbose_name='متا توضیحات')
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه کردن دوره')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='مدرس')
    related_items = models.ManyToManyField('self', symmetrical=False, related_name='related_to')

    def discount_offer(self):
        # original_price - original_price / 100 * percent
        return self.original_price - self.original_price / 100 * self.discount_code.percent

    def snippet(self):
        return self.small_description[0:44]

    def roadmap_snippet(self):
        return self.small_description[0:165] + '...'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "دوره ها"
        verbose_name = "دوره"


class Course_Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    show_comments = models.BooleanField(default=False,
                                        verbose_name='در صورتی که این تیک زده شود کامنت نمایش داده خواهد شد')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:20]


class Tickets(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='کاربر')
    course = models.ForeignKey(Course, related_name='tickets', on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    course_ep = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Ticket_Uploader(models.Model):
    file_name = models.CharField(max_length=255)
    file_url = models.URLField(max_length=255)
    ticket = models.ForeignKey(Tickets, related_name='ticket_uploader', on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name


class Course_Faze(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faze', verbose_name='دوره مورد نظر')
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام فاز')
    original_price = models.IntegerField(null=False, blank=False, verbose_name='قیمت اصلی فاز ')
    discount_code = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, verbose_name='درصد تخفیف دوره',
                                      help_text='برای استفاده از کد تخفیف اول باید یک کد تخفیف بسازید و بعد اینجا انتخابش کنید')
    temporary_discount_code = models.CharField(max_length=150, null=True, verbose_name='کد تخفیف موقت')
    is_free = models.BooleanField(default=False, help_text='اگر تیک را بزنید فاز به صورت رایگان ارزه می شود',
                                  verbose_name='رایگان بودن')
    is_discount = models.BooleanField(default=False,
                                      help_text='در صورت زدن این تیک تخیفیف ها روی این فاز اعمال می شود',
                                      verbose_name='اعمال تخفیف فاز')

    def __str__(self):
        return f'{self.name} ( {self.course.name} )'

    class Meta:
        verbose_name_plural = "فاز های دوره ها"
        verbose_name = "فاز های دوره ها"


class FazeFiles(models.Model):
    faze = models.ForeignKey(Course_Faze, on_delete=models.SET_NULL, null=True, verbose_name="فاز")
    name = models.CharField(max_length=225, verbose_name='نام فایل')
    link = models.CharField(max_length=550, verbose_name='لینک فایل مورد نظر')



class Course_Seasons(models.Model):
    course_faze = models.ForeignKey(Course_Faze, on_delete=models.CASCADE, verbose_name='فاز مورد نظر')
    name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام فصل')
    is_free = models.BooleanField(default=False, help_text='اگر تیک را بزنید فصل به صورت رایگان ارزه می شود',
                                  verbose_name='رایگان بودن')

    def __str__(self):
        return f'{self.name} {self.course_faze.name} {self.course_faze.course.name}'

    class Meta:
        verbose_name_plural = 'فصل های هر فاز'
        verbose_name = "فصل ها"


class Course_Sections(models.Model):
    course_season = models.ForeignKey(Course_Seasons, on_delete=models.CASCADE, verbose_name='فصل مورد نظر')
    section_name = models.CharField(max_length=150, null=False, blank=False, verbose_name='نام قسمت')
    video_id = models.CharField(max_length=800, null=True, blank=False, verbose_name='آی دی ویدئو')
    is_free = models.BooleanField(default=False, help_text='اگر تیک را بزنید قسمت به صورت رایگان نمایش داده می شود',
                                  verbose_name='رایگان بودن')
    download_access = models.BooleanField(default=True, help_text='اگر تیک را بزنید قسمت قابل دانلود خواهد بود',
                                          verbose_name='قابلیت دانلود')
    is_google_drive = models.BooleanField(default=True,
                                          help_text='اگر تیک را بزنید تنظیمات پلی از گوگل درایو لحاظ می شود',
                                          verbose_name='اپلود از گوگل درایو')

    def __str__(self):
        return f'{self.course_season.course_faze.course.name} {self.course_season.course_faze.name}  {self.course_season.name}  {self.section_name} '

    class Meta:
        verbose_name_plural = "قسمت های هر فصل"
        verbose_name = "قسمت ها"


class Course_Selled(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='دوره مورد نظر')
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه کردن دوره')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='خریدار')

    class Meta:
        verbose_name_plural = "سیستم خرید دوره"
        verbose_name = "خرید دوره"

    def __str__(self):
        return f'{self.buyer}  {self.course.name}'


class Faze_Selled(models.Model):
    course_faze = models.ForeignKey(Course_Faze, on_delete=models.CASCADE, verbose_name='فاز مورد نظر')
    creat_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه کردن فاز')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='خریدار')

    def __str__(self):
        return f'{self.buyer}  {self.course_faze.name}'

    class Meta:
        verbose_name_plural = "سیستم خرید فاز"
        verbose_name = "خرید فاز"


class Search(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name} '

    class Meta:
        verbose_name_plural = "افزودن فیلد های سرچ"
        verbose_name = "سیستم سرچ"
