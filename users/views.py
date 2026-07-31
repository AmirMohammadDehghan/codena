from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import uuid
from .models import CustomUser
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from .email_helpers import send_forget_password_email
from .number_phone_helper import send_forget_password_sms
import re
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from excel_response import ExcelResponse
# Create your views here.

def Login(request):
    try:
        if request.method == 'POST':
            number_phone = request.POST.get('number_phone')
            password = request.POST.get('password')

            if not number_phone or not password:
                messages.success(request, ' وارد کردن فیلد های شماره تلفن  و رمز اجباریست')
                return redirect('/accounts/login/')
            user_obj = CustomUser.objects.filter(phone_number=number_phone).first()
            if user_obj is None:
                messages.success(request, 'کاربری با این مشخصات پیدا نشد')
                return redirect('/accounts/login/')
            

            user = authenticate(phone_number=number_phone, password=password)

            if user is None:
                messages.success(request, 'رمز یا شماره تلفن شما اشتباه است')
                return redirect('/accounts/login/')
            
            login(request, user)
            return redirect('/')
        


    except Exception as e:
        print(e)
    return render(request, 'login.html')




def Register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            number_phone = request.POST.get('number_phone')
            email = request.POST.get('email')
            password = request.POST.get('password')

        try:
            if CustomUser.objects.filter(phone_number=number_phone).first():
                messages.success(request, 'کاربری با این شماره تلفن از قبل موجود است')
                return redirect('/accounts/register/')
            
            if CustomUser.objects.filter(email=email).first():
                messages.success(request, 'کاربری با این ایمیل از قبل مجود است')
                return redirect('/accounts/register/')

            user_obj = CustomUser(username=username, phone_number=number_phone, email=email)
            user_obj.set_password(password)
            user_obj.save()

            profile_obj = Profile.objects.create(user=user_obj)
            profile_obj.save()
            return redirect('/accounts/login/')
        except Exception as e:
            print(e)

    except Exception as e:
        print(e)
    return render(request, 'register.html')


def Logout(request):
    logout(request)
    return redirect('/')


def ChangePassword(request, token):
    
    try:
        Profile_obj = Profile.objects.filter(forget_password_token=token).first()
        context={
            'user_id': Profile_obj.user.id
        }
        if request.method == "POST":


            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id =request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'کاربری با این مشخصات یافت نشد .')
                return redirect(f'/accounts/change-password/{token}/')
            
            if new_password != confirm_password:
                messages.success(request, 'رمز و تکرار رمز باید با هم برابر باشند.')
                print(new_password)
                print(confirm_password)
                return redirect(f'/accounts/change-password/{token}/')
            print(new_password)
            print(confirm_password)
            
            user_obj = CustomUser.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('/accounts/login/')
        
    except Exception as e:
        print(e)
        
    return render(request, 'change-password.html', context=context)


def ForgetPassword(request):
    try:
        if request.method == 'POST':
            number_phone = request.POST.get('number_phone')

            regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

            if re.fullmatch(regex, number_phone):
                if not CustomUser.objects.filter(email=number_phone).first():
                    messages.success(request, 'کاربری با این مشخصات وجود ندارد.')
                    return redirect('/accounts/forget-password/')

                user_obj = CustomUser.objects.filter(email=number_phone).first()
                token = str(uuid.uuid4())
                print(user_obj)
                profile_obj = Profile.objects.get(user=user_obj)
                profile_obj.forget_password_token = token
                profile_obj.save()
                send_forget_password_email(user_obj.email, token)
                messages.success(request, ' پیام به ایمیل ,وارد شده ارسال شد ایمیل خود را چک کنید ارسال ممکن است چند ثانیه زمان ببرد دکمه ارسال را مکررا نفشارید.')
                return redirect('/accounts/forget-password/')
            else:
                if not CustomUser.objects.filter(phone_number=number_phone).first():
                    messages.success(request, 'کاربری با این مشخصات وجود ندارد.')
                    return redirect('/accounts/forget-password/')

                user_obj = CustomUser.objects.filter(phone_number=number_phone).first()
                token = str(uuid.uuid4())[:20]
                print(user_obj)
                profile_obj = Profile.objects.get(user=user_obj)
                profile_obj.forget_password_token = token
                profile_obj.save()
                send_forget_password_sms(user_obj.phone_number, token)
                messages.success(request, 'پیام به شماره ,وارد شده ارسال شد پیامک های خود را چک کنید ارسال ممکن است چند ثانیه زمان ببرد دکمه ارسال را مکررا نفشارید.')
                return redirect('/accounts/forget-password/')
    except Exception as e:
        print(e)
    return render(request, 'forget-password.html')


class UsersListView(UserPassesTestMixin, ListView ):
    model = CustomUser
    template_name = 'users_list.html'  # نام تمپلیت مربوطه
    context_object_name = 'users'
    raise_exception = True

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        # این تابع برای انجام اقدامات خاصی در صورت عدم دسترسی به لیست ویو استفاده می‌شود
        raise Http404("صفحه مورد نظر یافت نشد")


def export_users_excel(request):
    if request.user.is_superuser:
        users = CustomUser.objects.all()  # جایگزین YourUserModel با مدل کاربر شما
        
        response = ExcelResponse(users, output_filename='exported_users.xlsx', force_csv=False)
        response['Content-Disposition'] = 'attachment; filename="exported_users.xlsx"'
        return response
    raise Http404("صفحه مورد نظر یافت نشد")
