from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import PythonEditorModel
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'editor_landing.html')



@login_required()
def python_editor(request):
    user = request.user
    try:
        your_model_instance = PythonEditorModel.objects.get(user=user)
        initial_value = your_model_instance.text_field
    except PythonEditorModel.DoesNotExist:
        initial_value = "# اولین کد خود را در کد ادیتور کدنا بنویسید"

    # ارسال مقدار به ویو تمپلیت
    context = {
        'initial_value': initial_value
    }

    return render(request, 'python/editor.html', context)



def save_data(request):
    if request.method == 'POST':
        input_value = request.POST.get('input_value', None)
        user = request.user  # یافتن کاربر فعلی

        # برای هر کاربر یک رکورد جدید ایجاد یا بروزرسانی کنید
        your_model, created = PythonEditorModel.objects.get_or_create(user=user)

        # ذخیره مقدار در مدل
        your_model.text_field = input_value
        your_model.save()

        return JsonResponse({'message': 'مقدار با موفقیت ذخیره شد.'})

    return JsonResponse({'message': 'درخواست معتبر نیست.'}, status=400)