# accounts/adapters.py
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def confirm_email(self, request, email_address):
        print("Confirm email called!")  # (for checking if it is getting called)
        email_address.set_verified()
        email_address.save()

        user = email_address.user
        if not user.is_active:
            user.is_active = True
            user.save()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    pass
