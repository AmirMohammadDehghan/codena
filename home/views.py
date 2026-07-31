from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView, View, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . import models
from blog.models import Post, Podcast
from blog.views import jalalidate
from roadmap.models import RoadMaps, RoadMapDetails
from MembersDietail.models import Our_Member
from .forms import CommentForm, TicketForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .tasks import upload_file_to_ftp, pp
from jdatetime import date as jdate


def jalalidate(date):
    gregorian_date = date
    jalali_date = jdate.fromgregorian(date=gregorian_date).strftime("%Y/%m/%d")
    return jalali_date


# Create your views here.
@login_required(login_url='account:login')
def temporary_discount_code_form_view(request):
    try:
        if request.method == 'POST':
            selected_course = models.Course.objects.filter(slug=request.POST.get('selected_course')).first()
            discount_course_code = request.POST.get('discount_code')

            if request.POST.get('selected_course') != None and discount_course_code != None:
                try:
                    if models.Course_Selled.objects.get(buyer=request.user, course=selected_course):
                        return redirect('/')
                except Exception as e:
                    print(e)

                if models.Course.objects.filter(temporary_discount_code=discount_course_code,
                                                slug=request.POST.get('selected_course')).first():
                    course_selled_factor = models.Course_Selled.objects.create(buyer=request.user,
                                                                               course=selected_course)
                    course_selled_factor.save()
                    return redirect('/')

                else:
                    return redirect('/temporary_discount_code/dvjhfdsj56fhosdar984dfd98we94/course_form/')

    except Exception as e:
        print(e)

    courses = models.Course.objects.all()
    context = {
        'courses': courses,
    }

    return render(request, 'home/temporary_discount_code_course.html', context=context)


@login_required(login_url='account:login')
def temporary_discount_code_form_faze_view(request):
    try:
        if request.method == 'POST':
            faze_id = request.POST.get('selected_faze')
            if faze_id:
                faze_id = int(faze_id)
            selected_faze = models.Course_Faze.objects.filter(id=faze_id).first()
            discount_course_code = request.POST.get('discount_code')
            if faze_id != None and discount_course_code != None:
                try:
                    if models.Faze_Selled.objects.get(buyer=request.user, course_faze=selected_faze):
                        return redirect('/')
                except Exception as e:
                    print(e)

                if models.Course_Faze.objects.filter(temporary_discount_code=discount_course_code, id=faze_id).first():
                    faze_selled_factor = models.Faze_Selled.objects.create(buyer=request.user,
                                                                           course_faze=selected_faze)
                    faze_selled_factor.save()
                    return redirect('/')

                else:
                    return redirect('/temporary_discount_code/knbvfdsj5g6fhosd3949348fd894k94/faze_form/')

    except Exception as e:
        print(e)

    fazes = models.Course_Faze.objects.all()
    context = {
        'fazes': fazes,
    }

    return render(request, 'home/temporary_discount_code_faze.html', context=context)


def index(request):
    # data
    main_slider = models.MainSlider.objects.first()
    course = models.Course.objects.all().order_by('fake_id')[:12]
    blog_post = Post.objects.all().order_by('-date')[:4]
    podcast = Podcast.objects.all().order_by('-date')[:4]
    roadmaps = RoadMaps.objects.all()

    for item in blog_post:
        item.date = jalalidate(item.date)

    for item in course:
        item.creat_at = jalalidate(item.creat_at)

    context = {
        'main_slider': main_slider,
        'course': course,
        'blog_post': blog_post,
        'podcasts': podcast,
        'roadmaps': roadmaps,
    }
    return render(request, 'home/index.html', context=context)


def about_us(request):
    # data

    return render(request, 'activitis/about.html')


def contact_us(request):
    # data

    return render(request, 'activitis/contact-us.html')


# def course_detail(request, slug, pk):
#     # course_detail = models.Course.objects.get(slug=slug, pk=pk)
#     course_detail = get_object_or_404(models.Course, pk=pk, slug=slug)
#     comments = course_detail.comments.filter(parent__isnull=True)
#     course_faze = models.Course_Faze.objects.filter(course=course_detail)
#     course_seasons = models.Course_Seasons.objects.all().order_by('pk')
#     course_sections = models.Course_Sections.objects.all().order_by('pk')
#     about_teacher = Our_Member.objects.filter(user=course_detail.teacher).first()
#     is_faze_selled = False
#     course_selled = False
#     faze_selled = {}
#     students_length = 0
#     episodes_length = 0
#     user_buyed = False
#     if request.user.is_authenticated:
#         if models.Course_Selled.objects.filter(course=course_detail,
#                                                buyer=request.user) or models.Faze_Selled.objects.filter(
#             buyer=request.user, course_faze__course=course_detail):
#             user_buyed = True
#
#     for i in models.Course_Selled.objects.filter(course=course_detail):
#         students_length += 1
#
#     for i in models.Faze_Selled.objects.filter(course_faze__course=course_detail):
#         students_length += 1
#
#     for i in models.Course_Sections.objects.filter(course_season__course_faze__course=course_detail):
#         episodes_length += 1
#
#     if request.user.is_authenticated:
#         course_selled = models.Course_Selled.objects.filter(course=course_detail, buyer=request.user).first()
#
#         faze_selled = models.Faze_Selled.objects.filter(buyer=request.user, course_faze__course=course_detail)
#         if len(faze_selled) == 0:
#             is_faze_selled = False
#         else:
#             is_faze_selled = True
#
#     context = {
#         'course_detail': course_detail,
#         'course_faze': course_faze,
#         'course_seasons': course_seasons,
#         'course_sections': course_sections,
#         'course_selled': course_selled,
#         'faze_selled': faze_selled,
#         'is_faze_selled': is_faze_selled,
#         'episodes_length': episodes_length,
#         'students_length': students_length,
#         'user_buyed': user_buyed,
#         'about_teacher': about_teacher,
#
#     }
#     return render(request, 'course/course_detail.html', context=context)


class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'course/course_detail.html'
    context_object_name = 'course_detail'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course_detail = self.get_object()

        # Retrieve all comments for the course
        comments = course_detail.comments.filter(parent__isnull=True, show_comments=True)

        # Retrieve all comments for the course
        tickets = None
        if self.request.user.is_authenticated:
            tickets = course_detail.tickets.filter(parent__isnull=True, author=self.request.user)
            if self.request.user.is_teacher:
                tickets = course_detail.tickets.filter(parent__isnull=True)

        # Pagination
        paginator = Paginator(comments, 10)
        page_number = self.request.GET.get('page')
        try:
            comments_page = paginator.page(page_number)
        except PageNotAnInteger:
            comments_page = paginator.page(1)
        except EmptyPage:
            comments_page = paginator.page(paginator.num_pages)

        context['comments_page'] = comments_page
        context['related_courses'] = course_detail.related_items.all()

        context['tickets'] = tickets
        context['course_faze'] = models.Course_Faze.objects.filter(course=course_detail)
        context['course_seasons'] = models.Course_Seasons.objects.all().order_by('pk')
        context['course_sections'] = models.Course_Sections.objects.all().order_by('pk')
        context['about_teacher'] = Our_Member.objects.filter(user=course_detail.teacher).first()
        context['is_faze_selled'] = False
        context['course_selled'] = False
        context['faze_selled'] = {}
        context['students_length'] = 0
        context['episodes_length'] = 0
        context['user_buyed'] = False
        context['form'] = CommentForm()
        # Add ticket form to the context
        context['ticket_form'] = TicketForm()

        if self.request.user.is_authenticated:
            if models.Course_Selled.objects.filter(course=course_detail, buyer=self.request.user).exists() or \
                    models.Faze_Selled.objects.filter(buyer=self.request.user,
                                                      course_faze__course=course_detail).exists():
                context['user_buyed'] = True

        context['students_length'] += models.Course_Selled.objects.filter(course=course_detail).count()
        context['students_length'] += models.Faze_Selled.objects.filter(course_faze__course=course_detail).count()
        context['episodes_length'] += models.Course_Sections.objects.filter(
            course_season__course_faze__course=course_detail).count()
        if course_detail.is_fake_student:
            context['students_length'] = course_detail.fake_student

        if self.request.user.is_authenticated:
            context['course_selled'] = models.Course_Selled.objects.filter(course=course_detail,
                                                                           buyer=self.request.user).first()
            context['faze_selled'] = models.Faze_Selled.objects.filter(buyer=self.request.user,
                                                                       course_faze__course=course_detail)
            context['is_faze_selled'] = context['faze_selled'].exists()

        return context

    @method_decorator(login_required(login_url='account:login'))
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.course = self.object
            comment.author = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = models.Course_Comment.objects.get(id=parent_id)
            comment.save()
            return redirect('home:course_detail', slug=self.object.slug, pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))


class CreateTicketView(View):
    pk_url_kwarg = 'pk'

    @method_decorator(login_required(login_url='account:login'))
    def post(self, request, *args, **kwargs):
        self.object = models.Course.objects.get(id=self.kwargs['pk'])
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.course = self.object
            ticket.author = request.user
            parent_id = request.POST.get('parent_id')
            if parent_id:
                ticket.parent = models.Tickets.objects.get(id=parent_id)
            ticket.save()
            return redirect('home:course_detail', slug=self.object.slug, pk=self.object.pk)
        return self.render_to_response(self.get_context_data(form=form))


# upload file to ftp server

# def upload_file(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#
#         # بررسی اندازه فایل
#         if myfile.size > settings.FILES_UPLOAD_MAX_SIZE:
#             error_message = f"The file size should not exceed {settings.FILES_UPLOAD_MAX_SIZE / (1024 * 1024)} MB."
#             return render(request, 'upload_fail.html', {'error_message': error_message})
#
#         try:
#             # ذخیره فایل به‌طور موقت در سرور Django
#             fs = FileSystemStorage()
#             filename = fs.save(myfile.name, myfile)
#             uploaded_file_path = fs.path(filename)  # مسیر فایل در سرور Django
#
#             # اتصال به سرور FTP و آپلود فایل
#             ftp = FTP(settings.FTP_HOST)
#             ftp.login(user=settings.FTP_USERNAME, passwd=settings.FTP_PASSWORD)
#
#             with open(uploaded_file_path, 'rb') as file:
#                 ftp.storbinary(f'STOR {myfile.name}', file)
#
#             ftp.quit()
#
#             # حذف فایل از سرور Django پس از آپلود
#             fs.delete(filename)
#
#             # اطلاعات آپلود موفق به تمپلیت منتقل می‌شود
#             context = {'uploaded_file_url': f"https://{settings.FTP_HOST}/{myfile.name}"}
#             return render(request, 'upload_success.html', context)
#
#         except Exception as e:
#             error_message = f"An error occurred: {str(e)}"
#             return render(request, 'upload_fail.html', {'error_message': error_message})
#
#     return render(request, 'upload.html')


def upload_ticket_media(request):
    if request.method == 'POST' and request.FILES['ticket_file']:
        ticket_file = request.FILES['ticket_file']

        ticket_id = int(request.POST.get('ticket_id'))

        print('ss')
        # بررسی اندازه فایل
        if ticket_file.size > settings.FILES_UPLOAD_MAX_SIZE:
            error_message = f"فایل اپلودی نباید بیشتر از {settings.FILES_UPLOAD_MAX_SIZE / (1024 * 1024)} MB باشد."
            return JsonResponse({'status': error_message})

        try:
            #     # ذخیره فایل به‌طور موقت در سرور Django
            fs = FileSystemStorage()
            filename = fs.save(ticket_file.name, ticket_file)
            uploaded_file_path = fs.path(filename)  # مسیر فایل در سرور Django
            pp.delay('upload')
            #
            upload_file_to_ftp.delay(uploaded_file_path, ticket_id, filename)

            #     # اتصال به سرور FTP و آپلود فایل
            #     ftp = FTP(settings.FTP_HOST)
            #     ftp.login(user=settings.FTP_USERNAME, passwd=settings.FTP_PASSWORD)
            #
            #     with open(uploaded_file_path, 'rb') as file:
            #         ftp.storbinary(f'STOR {myfile.name}', file)
            #
            #     ftp.quit()
            #
            #     # حذف فایل از سرور Django پس از آپلود
            #     fs.delete(filename)
            #
            #     # اطلاعات آپلود موفق به تمپلیت منتقل می‌شود
            #     context = {'uploaded_file_url': f"https://{settings.FTP_HOST}/{myfile.name}"}
            return JsonResponse({'status': 'فایل در حال اپلود در سرور است منتظر بمانید ...'})

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            print(error_message)
            return JsonResponse({'status': error_message})

    return redirect('/')


class CourseListView(ListView):
    # paginate_by = 12  # تعداد آیتم‌ها در هر صفحه
    model = models.Course
    template_name = 'course/courselist.html'  # مسیر به فایل template
    context_object_name = 'courses'  # نام شیئی که به template فرستاده می‌شود

    def get_queryset(self):
        courses = models.Course.objects.all()
        for course in courses:
            course.buyed = False
            if self.request.user.is_authenticated:
                if models.Course_Selled.objects.filter(course=course, buyer=self.request.user).exists() or \
                        models.Faze_Selled.objects.filter(buyer=self.request.user,
                                                          course_faze__course=course).exists():
                    course.buyed = True
            course.creat_at = jalalidate(course.creat_at)
        return courses