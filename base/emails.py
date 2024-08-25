from django.core.mail import send_mail
from django.conf import settings

def send_account_activation_email(email, email_token):
    subject = 'Activate your account'
    message = f'Please click the following link to activate your account: http://127.0.0.1:8000/activate_email/{email_token}/'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
