from django.conf import settings
import requests
import json
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import ConsultationRequest
from roadmap.forms import ConsultationRequestForm

from home.models import Course_Selled, Faze_Selled, Course, Course_Faze

from cart.models import Cart, Cart_Faze

from .models import Payment_Course_Data, Payment_Faze_Data

# ? sandbox merchant
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = '00000000000'  # Optional
# Important: need to edit for realy server.
CallbackURL = f'{settings.CODENA_URL}ATM/verify/'

# contact callback
ZARINPAL_CALLBACK_URL = f'{settings.CODENA_URL}ATM/callback/'


def send_request(request, price):
    amount = price
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    #     # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    # new
    res = requests.post(ZP_API_REQUEST, data=data, headers=headers)
    if res.status_code == 200:
        response = res.json()
        if response['Status'] == 100:
            url = f"{ZP_API_STARTPAY}{response['Authority']}"
            return redirect(url)
    else:
        print(str(res.json()['errors']))
        return HttpResponse(str(res.json()['errors']))


#     try:
#         response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

#         if response.status_code == 200:
#             response = response.json()
#             if response['Status'] == 100:
#                 return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
#             else:
#                 return {'status': False, 'code': str(response['Status'])}
#         return response

#     except requests.exceptions.Timeout:
#         return {'status': False, 'code': 'timeout'}
#     except requests.exceptions.ConnectionError:
#         return {'status': False, 'code': 'connection error'}


def verify(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": request.GET['Authority'],
    }

    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZP_API_VERIFY, data=data, headers=headers)

    if res.status_code == 200:
        response = res.json()
        if response['Status'] == 100:
            # return {'status': True, 'RefID': response['RefID']}
            return HttpResponse({'status': response['Status'], 'RefID': response['RefID']})
        else:
            return HttpResponse({'status': response['Status'], 'RefID': response['RefID']})
    return HttpResponse('پرداخت نا موفق')


#  course payment system

def course_payment_request(request, cors_id, discount_code):
    course = Course.objects.get(id=cors_id)
    if Course_Selled.objects.filter(buyer=request.user, course=course):
        return redirect(verified)


    elif course.temporary_discount_code == str(discount_code) or course.status:

        course_selled = Course_Selled.objects.create(buyer=request.user, course=course)
        course_selled.save()
        Cart.objects.filter(user=request.user, course=course).delete()

        return redirect(verified)



    else:

        user = request.user
        phone = user.phone_number

        amount = course.original_price

        if course.discount_code:
            if str(discount_code) == course.discount_code.code:
                amount = amount - amount / 100 * course.discount_code.percent

        description = f'خرید دوره {course.name} از اکادمی کدنا '

        CallbackURL = f'{settings.CODENA_URL}ATM/verify/{cors_id}/{discount_code}/'
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Description": description,
            "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        #     # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        # new
        res = requests.post(ZP_API_REQUEST, data=data, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
        else:
            print(str(res.json()['errors']))
            return HttpResponse(str(res.json()['errors']))


def course_payment_verify(request, cors_id, discount_code):
    course = Course.objects.get(id=cors_id)
    amount = course.original_price
    if course.discount_code:
        if str(discount_code) == course.discount_code.code:
            amount = amount - amount / 100 * course.discount_code.percent
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": request.GET['Authority'],
    }

    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZP_API_VERIFY, data=data, headers=headers)
    response = res.json()
    context = {'refid': res.json()['RefID']}  # ['RefID']

    if res.status_code == 200:
        response = res.json()
        if response['Status'] == 100:

            # return {'status': True, 'RefID': response['RefID']}
            course_selled = Course_Selled.objects.create(buyer=request.user, course=course)
            course_selled.save()

            payment_course_data = Payment_Course_Data.objects.create(
                user=request.user,
                course=course,
                price=amount,
                RefId=response['RefID'],
                status=response['Status'],
                is_success=True,
            )
            payment_course_data.save()

            Cart.objects.filter(user=request.user, course=course).delete()

            return render(request, 'verify.html', context)
        else:
            payment_course_data = Payment_Course_Data.objects.create(
                user=request.user,
                course=course,
                price=amount,
                RefId=response['RefID'],
                status=response['Status'],
                is_success=False,
            )
            payment_course_data.save()

            return render(request, 'failed.html')

    payment_course_data = Payment_Course_Data.objects.create(
        user=request.user,
        course=course,
        price=amount,
        RefId=response['RefID'],
        status=response['Status'],
        is_success=False,
    )
    payment_course_data.save()
    return render(request, 'failed.html')


# faze

def faze_payment_request(request, faz_id, discount_code):
    faze = Course_Faze.objects.get(id=faz_id)
    if Faze_Selled.objects.filter(buyer=request.user, course_faze=faze):
        return redirect(verified)

    elif faze.temporary_discount_code == str(discount_code) or faze.is_free:

        faze_selled = Faze_Selled.objects.create(buyer=request.user, course_faze=faze)
        faze_selled.save()
        Cart_Faze.objects.filter(user=request.user, faze=faze).delete()

        return redirect(verified)



    else:

        user = request.user
        phone = user.phone_number

        amount = faze.original_price

        if faze.discount_code:
            if str(discount_code) == faze.discount_code.code:
                amount = amount - amount / 100 * faze.discount_code.percent

        description = f'خرید {faze.name} دوره {faze.course.name} از اکادمی کدنا'

        CallbackURL = f'{settings.CODENA_URL}ATM/verify/faze/{faz_id}/{discount_code}/'
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": amount,
            "Description": description,
            "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        #     # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data))}
        # new
        res = requests.post(ZP_API_REQUEST, data=data, headers=headers)
        if res.status_code == 200:
            response = res.json()
            if response['Status'] == 100:
                url = f"{ZP_API_STARTPAY}{response['Authority']}"
                return redirect(url)
        else:
            print(str(res.json()['errors']))
            return HttpResponse(str(res.json()['errors']))


def faze_payment_verify(request, faz_id, discount_code):
    faze = Course_Faze.objects.get(id=faz_id)
    amount = faze.original_price
    if faze.discount_code:
        if str(discount_code) == faze.discount_code.code:
            amount = amount - amount / 100 * faze.discount_code.percent
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": request.GET['Authority'],
    }

    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data))}
    res = requests.post(ZP_API_VERIFY, data=data, headers=headers)
    response = res.json()
    context = {'refid': res.json()['RefID']}  # ['RefID']

    if res.status_code == 200:
        response = res.json()
        if response['Status'] == 100:

            # return {'status': True, 'RefID': response['RefID']}
            faze_selled = Faze_Selled.objects.create(buyer=request.user, course_faze=faze)
            faze_selled.save()

            payment_faze_data = Payment_Faze_Data.objects.create(
                user=request.user,
                faze=faze,
                price=amount,
                RefId=response['RefID'],
                status=response['Status'],
                is_success=True,
            )
            payment_faze_data.save()

            Cart_Faze.objects.filter(user=request.user, faze=faze).delete()

            return render(request, 'verify.html', context)
        else:
            payment_faze_data = Payment_Faze_Data.objects.create(
                user=request.user,
                faze=faze,
                price=amount,
                RefId=response['RefID'],
                status=response['Status'],
                is_success=False,
            )
            payment_faze_data.save()

            return render(request, 'failed.html')

    payment_faze_data = Payment_Faze_Data.objects.create(
        user=request.user,
        faze=faze,
        price=amount,
        RefId=response['RefID'],
        status=response['Status'],
        is_success=False,
    )
    payment_faze_data.save()
    return render(request, 'failed.html')


def verified(request):
    return render(request, 'verify/verify_page.html')


def process_payment_view(request):
    if request.method == 'POST':
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            consultation_request = form.save(commit=False)
            consultation_request.amount = 200000 if consultation_request.consultation_type == 'supporters' else 500000
            consultation_request.save()

            data = {
                'MerchantID': settings.MERCHANT,
                'Amount': consultation_request.amount,
                'CallbackURL': ZARINPAL_CALLBACK_URL,
                'Description': f'مشاوره با {consultation_request.fullname}',
                'Email': consultation_request.email,
                'Mobile': consultation_request.phone_number,
            }
            response = requests.post(ZP_API_REQUEST, json=data)
            response_data = response.json()

            if response_data['Status'] == 100:
                consultation_request.authority = response_data[
                    'Authority']  # ذخیره authority در مدل ConsultationRequest
                consultation_request.save()
                return redirect(f"https://{sandbox}.zarinpal.com/pg/StartPay/{response_data['Authority']}")
            else:
                return render(request, 'error.html', {'message': 'خطا در اتصال به درگاه پرداخت زرین‌پال'})
        else:
            return redirect('roadmaps:RoadMapListView')
    else:
        return redirect('consultation_request')


def callback_view(request):
    authority = request.GET.get('Authority')
    status = request.GET.get('Status')

    if status == 'OK':
        consultation_request = get_object_or_404(ConsultationRequest, authority=authority)
        data = {
            'MerchantID': settings.MERCHANT,
            'Authority': authority,
            'Amount': consultation_request.amount,
        }
        response = requests.post(ZP_API_VERIFY, json=data)
        response_data = response.json()

        if response_data['Status'] == 100:
            consultation_request.is_paid = True
            consultation_request.save()
            return render(request, 'succes.html', {'message': 'پرداخت با موفقیت انجام شد.', 'authority': authority})
        else:
            return render(request, 'error.html', {'message': 'پرداخت انجام نشد. لطفا دوباره تلاش کنید.'})
    else:
        return render(request, 'error.html', {'message': 'پرداخت توسط کاربر لغو شد.'})
