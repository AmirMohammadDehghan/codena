from django.core.mail import send_mail
from django.conf import settings

def send_forget_password_email(email, token):

    subject = 'بازیابی رمز عبور کدنا'
    message = f'https://codena.org/accounts/change-password/{token}/ برای بازیابی رمز عبور خود بر روی این اینک کلیک کنید  '
    from_email = 'support@academycodena.ir'
    print(from_email)
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)
    return True