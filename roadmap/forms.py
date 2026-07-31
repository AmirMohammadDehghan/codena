from django import forms
from ATM.models import ConsultationRequest


class ConsultationRequestForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ['fullname', 'email', 'phone_number', 'consultation_type']

        labels = {
            'fullname': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'شماره موبایل',
            'consultation_type': 'مشاور',
        }

        widgets = {
            'fullname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'fullnameInput',
                'placeholder': 'مثلا محمد حمزه قلعه خانی',
                'aria-describedby': 'fullname'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'EmailInput',
                'placeholder': 'مثلا test@gmail.com',
                'aria-describedby': 'email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phoneNumberInput',
                'placeholder': 'مثلا 09167872788',
                'aria-describedby': 'phoneNumber',
                'type': 'number',
                'required': 'required',
                'pattern': '^0[0-9]{10}$',
                'oninvalid': 'setCustomValidity("شماره تلفن شما باید با صفر شروع شود و 11 رقم باشد!")',
                'oninput': 'setCustomValidity("")'
            }),
            'consultation_type': forms.RadioSelect(choices=[
                ('supporters', 'مشاوره یک ساعته با پشتیبان ها (200 هزار تومان)'),
                ('professors', 'مشاوره یک ساعته با اساتید (500 هزار تومان)')
            ], attrs={

            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['consultation_type'].widget.choice_label = lambda choice: {
            'supporters': 'مشاوره یک ساعته با پشتیبان ها (200 هزار تومان)',
            'professors': 'مشاوره یک ساعته با اساتید (500 هزار تومان)'
        }[choice]

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('0') or len(phone_number) != 11:
            raise forms.ValidationError('شماره تلفن شما باید با صفر شروع شود و 11 رقم باشد!')
        return phone_number