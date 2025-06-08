from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth import get_user_model
from .models import Cart, CartItems, ProFile
import uuid
from base.emails import send_verification_email

User = get_user_model()


@receiver(user_logged_in)
def restore_cart_on_login(sender, request, user, **kwargs):
    try:
        user_cart = Cart.objects.filter(user=user).first()
        if user_cart:
            cart_items = CartItems.objects.filter(cart=user_cart)
            request.session['cart'] = [
                {
                    'product_id': item.product_id,
                    'color_id': item.color_variant_id,
                    'size_id': item.size_variant_id,
                    'quantity': item.quantity
                }
                for item in cart_items
            ]
    except Exception as e:
        print(f"Error restoring cart on login: {e}")


from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from django.contrib.auth.models import User
from appname.models import ProFile
from base.emails import send_verification_email  # Import the function
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
import uuid
from .models import ProFile
# from .email import send_account_activation_email  # Import email function
import traceback  # ✅ Add this at the top

import traceback
from django.db.models.signals import post_save
from django.dispatch import receiver
from appname.models import ProFile
import uuid

# @receiver(post_save, sender=User)
# def send_email_token(sender, instance, created, **kwargs):
#     if not created:  # ✅ Ensure this only runs on new user creation
#         return

#     print(f"🔥 Signal triggered for {instance.email} | Created: {created}")

#     # ❌ Prevent duplicate profile creation
#     if ProFile.objects.filter(user=instance).exists():
#         print(f"⚠️ Profile already exists for {instance.email}, skipping creation.")
#         return

#     # ✅ Create profile only if it doesn't exist
#     profile = ProFile.objects.create(user=instance, email_token=str(uuid.uuid4()))

#     print(f"📧 Sending email token to {instance.email}")
#     send_verification_email(instance.email, profile.email_token)




from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from appname.models import ProFile
import uuid
from base.emails import send_verification_email  # Ensure this is the correct import

User = get_user_model()

@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    """ ✅ Ensure profile is only created once """
    if created and not hasattr(instance, "profile"):  
        ProFile.objects.create(
            user=instance,
            name=f"{instance.first_name} {instance.last_name}",
            email=instance.email,
            email_token=str(uuid.uuid4()),
            is_email_verified=False
        )
