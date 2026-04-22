from django.conf import settings
from collections import defaultdict
from django.core.mail import send_mail


def send_confirmation_emails(suborder):
    order = suborder.main_order  # Get the parent Order
    user = order.user
    profile = getattr(user, 'profile', None)

    customer_email = user.email
    customer_name = user.get_full_name() or user.username
    customer_phone = getattr(profile, 'phone', '')
    customer_address = getattr(profile, 'address', '')
    merchant_email = settings.EMAIL_HOST_USER

    # Fetch items related to this suborder
    order_items = suborder.items.select_related('product')

    # Format order item lines
    item_lines = "\n".join([
        f"- {item.product.product_name} (x{item.quantity}) @ Rs. {item.price}"
        for item in order_items
    ])
    total = f"\nTotal Amount: Rs. {suborder.total_amount}\nSub-Order ID: {suborder.id}"

    tracking_info = ""
    if suborder.awb_code:
        tracking_info += f"\nTracking AWB: {suborder.awb_code} ({suborder.selected_courier})"
        tracking_info += f"\nTrack: https://shiprocket.co/tracking/{suborder.awb_code}"

    # ---------------------
    # Seller Info
    seller = suborder.seller
    seller_profile = getattr(seller, 'profile', None)
    seller_email = seller.email
    seller_name = getattr(seller_profile, 'name', seller.username)
    seller_phone = getattr(seller_profile, 'phone', '')

    # ---------------------
    # Email to Customer
    customer_subject = '🛒 Your Order Confirmation - TheDIYNight'
    customer_message = f"""Hi {customer_name},

Thanks for shopping with TheDIYNight! 🎉

Items:
{item_lines}
{total}
{tracking_info}

💬 Need customizations?
You can reach out to your seller:

Seller: {seller_name}
Email: {seller_email}
Phone: {seller_phone}

We'll notify you when your order is out for delivery.

Best,  
TheDIYNight Team
"""

    send_mail(
        subject=customer_subject,
        message=customer_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[customer_email],
        fail_silently=False
    )

    # ---------------------
    # Email to Admin
    merchant_subject = '📦 New SubOrder Received'
    merchant_message = f"""Hello Admin,

New SubOrder has been placed.

Customer: {customer_name}
Email: {customer_email}
Phone: {customer_phone}
Address: {customer_address}

Items:
{item_lines}
{total}

Please coordinate for shipping.

Regards,
TheDIYNight System
"""

    send_mail(
        subject=merchant_subject,
        message=merchant_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[merchant_email],
        fail_silently=False
    )

    # ---------------------
    # Email to Seller
    if seller_email:
        seller_subject = "🛍️ New Order for Your Product - TheDIYNight"
        seller_message = f"""Hello {seller_name},

You received a new order!

Customer: {customer_name}
Email: {customer_email}
Phone: {customer_phone}
Address: {customer_address}

Items:
{item_lines}
Sub-Order ID: {suborder.id}

Please prepare your items for dispatch.

Best,  
TheDIYNight Team
"""
        send_mail(
            subject=seller_subject,
            message=seller_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[seller_email],
            fail_silently=False
        )
