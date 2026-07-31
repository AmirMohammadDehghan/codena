from django.http import JsonResponse
from django.shortcuts import render, redirect
# from django.contrib import messages
from .models import Cart , Cart_Faze
from home.models import Course_Selled, Faze_Selled
from django.contrib.auth.decorators import login_required


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            cors_id = int(request.POST.get('course_id'))
            if Cart.objects.filter(user=request.user, course_id=cors_id) or Course_Selled.objects.filter(buyer=request.user, course_id=cors_id):
                pass
            else:
                Cart.objects.create(user=request.user, course_id=cors_id)
        return JsonResponse({'status': "محصول با موفقیت اضافه شد لطفا سبد خرید خود را برای پرداخت چک کنید!"})
    return redirect('/')

@login_required(login_url='account:login')
def viewcartlist(request):
    cartlist = Cart.objects.filter(user=request.user)
    cartfazelist = Cart_Faze.objects.filter(user=request.user)
    context = {
        'cartlist': cartlist,
        'cartfazelist': cartfazelist
        }
    return render(request, 'cart/cart.html', context)



def deletecartlistitem(request):
    if request.method == 'POST':
        cors_id = int(request.POST.get('course_id'))
        if Cart.objects.filter(user=request.user, course_id=cors_id):
            cartitem = Cart.objects.get(course_id=cors_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "حذف  با موفقیت انجام شد!"})
    return redirect('/')










def addfazetocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            faz_id = int(request.POST.get('faze_id'))
            if Cart_Faze.objects.filter(user=request.user, faze_id=faz_id) or Faze_Selled.objects.filter(buyer=request.user, course_faze_id=faz_id):
                pass
            else:
                Cart_Faze.objects.create(user=request.user, faze_id=faz_id)
        return JsonResponse({'status': "محصول با موفقیت اضافه شد!"})
    return redirect('/')



def deletefazecartlistitem(request):
    if request.method == 'POST':
        faz_id = int(request.POST.get('faze_id'))
        if Cart_Faze.objects.filter(user=request.user, faze_id=faz_id):
            cartitem = Cart_Faze.objects.get(faze_id=faz_id, user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "حذف  با موفقیت انجام شد!"})
    return redirect('/')
