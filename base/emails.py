
# from django.core.mail import send_mail
# from django.conf import settings
# def send_account_activation_email(email, token):
#     subject = 'Activate your account'
#     activation_link = f'http://127.0.0.1:8000/activate_email/{token}/'
#     message = f'Click the following link to activate your account:\n\n{activation_link}'
    
#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [email],
#         fail_silently=False,
#     )

import uuid
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache
from django.utils.crypto import get_random_string

# def send_verification_email(email, purpose, user_id=None, name=None, phone=None, address=None, first_name=None, last_name=None, password=None):
#     """
#     Sends an email verification link for both sign-up activation and email change verification.

#     Args:
#         email (str): The recipient's email.
#         purpose (str): Either 'signup' or 'email_change'.
#         user_id (int, optional): The user ID (for email change verification).
#         name (str, optional): The user's full name (for email change verification).
#         phone (str, optional): The user's phone number (for email change verification).
#         address (str, optional): The user's address (for email change verification).
#         first_name (str, optional): First name (for sign-up activation).
#         last_name (str, optional): Last name (for sign-up activation).
#         password (str, optional): Password (for sign-up activation).
#     """
#     email_token = get_random_string(32) if purpose == 'signup' else str(uuid.uuid4())
    
#     # Store data temporarily in cache
#     cache_key = f"verify_{email_token}" if purpose == 'signup' else f"email_verify_{email_token}"
#     cache_data = {
#         "email": email,
#         "email_token": email_token
#     }
    
#     if purpose == 'signup':
#         cache_data.update({
#             "first_name": first_name,
#             "last_name": last_name,
#             "password": password
#         })
#     else:
#         cache_data.update({
#             "user_id": user_id,
#             "name": name,
#             "phone": phone,
#             "address": address
#         })
    
#     cache.set(cache_key, cache_data, timeout=3600)  # Store for 1 hour
    
#     # Generate appropriate verification link
#     verification_link = f"{settings.SITE_URL}/activate_email/{email_token}/" if purpose == 'signup' else f"{settings.SITE_URL}/verify-email/{email_token}/"
    
#     subject = "Activate Your Account" if purpose == 'signup' else "Verify Your Email Address"
#     message = f"Click the link below to {'activate your account' if purpose == 'signup' else 'verify your email'}:\n\n{verification_link}"
    
#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [email],
#         fail_silently=False,
#     )



import uuid
from django.core.mail import send_mail
from django.conf import settings

# def send_verification_email(user, email):
#     from appname.models import ProFile  # ✅ Avoid circular import

#     email_token = str(uuid.uuid4())

#     user_profile = ProFile.objects.get(user=user)
#     user_profile.email_token = email_token
#     user_profile.save()

#     activation_link = f"http://127.0.0.1:8000/verify-email/{email_token}/"

#     subject = "Verify Your Email"
#     message = f"Click the link below to verify your email:\n\n{activation_link}"

#     send_mail(
#         subject,
#         message,
#         settings.EMAIL_HOST_USER,
#         [email],
#         fail_silently=False,
#     )
def send_verification_email(email, token):
    """ ✅ Send email verification link """
    activation_link = f"http://127.0.0.1:8000/activate-email/{token}/"

    subject = "Verify Your Email"
    message = (
        f"Welcome to TheDIYNight! You’re just one click away from unlocking your shop — "
        f"tap the link below to verify your email and start creating, customizing, and selling amazing gift items!\n\n"
        f"{activation_link}"
    )

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
