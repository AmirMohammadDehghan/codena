from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileUpdateForm
from home.models import Faze_Selled, Course_Selled


# Create your views here.
@login_required
def user_area(request):
    user = request.user
    form = UserProfileUpdateForm(instance=user, initial={
        'username': user.username,
        'email': user.email,
        'phone_number': user.phone_number,
    }
                                 )

    faze_selled = Faze_Selled.objects.filter(buyer=user)
    course_selled = Course_Selled.objects.filter(buyer=user)
    return render(request, 'dashboard.html', {'form': form, 'faze_selled': faze_selled, 'course_selled': course_selled})


@login_required
def validate_and_save_user_informations(request):
    if request.method == 'POST':
        form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            request.user.phone_number_verified = False
            return redirect('..')  # مسیر به نمایه کاربری

    return redirect('..')  #
