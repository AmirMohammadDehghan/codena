from django import forms
from users.models import CustomUser


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'user_image']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل خود را وارد کنید'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'user_image': forms.ClearableFileInput(attrs={'class': 'form-control form-image-upload' , 'placeholder': 'انتخاب عکس', 'aria-describedby':'عکس نمایه'}),
        }