from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress

class MyAccountAdapter(DefaultAccountAdapter):
    def confirm_email(self, request, email_address):
        # Call the original confirm method
        email_address.set_verified()
        email_address.save()

        # Activate the user if needed
        user = email_address.user
        if not user.is_active:
            user.is_active = True
            user.save()
