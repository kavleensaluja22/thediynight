from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse , HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,  logout 
from django.contrib.auth import authenticate, login as auth_login
from .models import ProFile
from django.db.models import Sum

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

import json
import uuid
import base64
import logging
from decimal import Decimal
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.utils.text import slugify
import razorpay

# from .models import Category, Product, ColorVariant, SizeVariant, ProductImage

# Initialize Razorpay client
import base64
import json
import logging
import uuid

from django.conf import settings
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.text import slugify
import json
import logging
import base64
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
from django.core.files.base import ContentFile
from django.utils.text import slugify
import razorpay
import razorpay
import base64
import imghdr
from django.core.files.base import ContentFile
from accounts.models import Product
from .models import Cart
from .models import CartItems
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from accounts.models import Category
from accounts.models import SizeVariant
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appname.models import ProFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appname.models import ProFile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from appname.models import ProFile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appname.models import ProFile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import uuid 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ProFile
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from appname.models import ProFile  # Ensure you import the Profile model
from django.shortcuts import render, redirect
from .forms import UpdateProfileForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from appname.models import Address, Phone
from appname.forms import AddressForm, PhoneForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

import base64
import uuid
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Product, ColorVariant, SizeVariant, ProductImage, Category
from django.utils.text import slugify
import json
import json
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import ProFile  # Adjust as needed
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import ProFile
from base.emails import send_verification_email  # Ensure this function exists

from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from base.emails import send_verification_email
import uuid
import logging
from django.contrib.auth import get_user_model, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.shortcuts import redirect
from django.contrib import messages
from appname.models import ProFile
from django.shortcuts import render
# from .models import Address, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from appname.models import ProFile  # Use the correct model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import json
from accounts.models import Order, OrderItem
import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import hmac
import hashlib
import logging
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Address

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import Order

from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from .models import Cart, Product, SizeVariant, ColorVariant

# In your Django views.py
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from .models import Cart, Product, SizeVariant, ColorVariant
from django.http import JsonResponse
import json

from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib import messages
from .models import ProFile, Cart, CartItems
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout as auth_logout


from .models import Cart, Product, SizeVariant, ColorVariant

from django.http import JsonResponse
from .models import Cart, Product, SizeVariant, ColorVariant
from django.views.decorators.csrf import csrf_exempt



from django.http import JsonResponse
from .models import Cart


from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import JsonResponse
from .models import Cart
from appname.models import Address






from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

from django.shortcuts import render
from .models import Product

from django.shortcuts import redirect
from django.contrib import messages
from appname.models import ProFile, User

from django.shortcuts import redirect
from django.contrib import messages
from appname.models import ProFile
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib import messages
import random
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.utils.crypto import get_random_string
from .models import Product
# from .utils import send_verification_email 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
import logging
import uuid
from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from accounts.models import Product, SizeVariant, ColorVariant
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, SizeVariant, ColorVariant
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from accounts.models import Product, Review
from accounts.forms import ReviewForm
# from appname.utils import send_account_activation_email  # Ensure correct import



from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from appname.models import ProFile
from django.contrib import messages

from django.contrib.auth import login
from django.contrib.auth import get_backends
from django.shortcuts import redirect
from django.contrib.auth.models import User
from appname.models import ProFile
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.core.cache import cache
from django.contrib import messages
from django.shortcuts import redirect
from appname.models import ProFile  # Import the ProFile model

from django.core.cache import cache
from django.utils.crypto import get_random_string
from base.emails import send_verification_email # Use your existing function

def sign(request):
    """ ✅ Handle user sign-up with email verification """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User = get_user_model()

        # ✅ Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('sign')

        # ✅ Generate a verification token
        token = get_random_string(32)

        # ✅ Store user data in cache
        cache.set(f"verify_{token}", {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
        }, timeout=3600)  # Store for 1 hour

        # ✅ Send email verification
        send_verification_email(email, token)

        messages.success(request, "Check your email to activate your account.")
        return redirect('sign')

    # Fetch products and pass them to the template
    products = list(Product.objects.all())  # Convert QuerySet to a list
    random.shuffle(products)  # Shuffle the products list

    context = {
        'products': products,
    }

    return render(request, 'user/sign.html', {'products': products})



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, 'Email and password are required')
            return render(request, 'user/login.html')

        user = authenticate(request, email=email, password=password)  # ← use email param

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
            return redirect('/')
        else:
            messages.error(request, 'Invalid email or password')

    # Fetch all products from the database
    products = list(Product.objects.all())  # Convert to list for shuffling
    
    # Shuffle the products randomly
    random.shuffle(products)
    
    # Select the first 4 products after shuffling
    featured_products = products[:4]
    
    # Pass the featured products to the template
    return render(request, 'user/login.html', {'products': featured_products})




def activate_email(request, token):
    """ ✅ Verify user email and activate account """
    user_data = cache.get(f"verify_{token}")
    if not user_data:
        messages.error(request, "Invalid or expired token. Please register again.")
        return redirect("sign")

    User = get_user_model()

    # ✅ Create the user if not exists
    user, created = User.objects.get_or_create(
        username=user_data["email"],
        defaults={
            "email": user_data["email"],
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "is_active": True
        }
    )

    # ✅ Set and hash password
    if created:
        user.set_password(user_data["password"])
        user.save()

    # ✅ Ensure `ProFile` exists with correct details
    profile, created = ProFile.objects.get_or_create(
        user=user,
        defaults={
            "name": f"{user_data['first_name']} {user_data['last_name']}",
            "email": user_data["email"],
            "is_email_verified": True,
        }
    )

    # ✅ Ensure profile updates correctly
    if not created:
        profile.name = f"{user_data['first_name']} {user_data['last_name']}"
        profile.email = user_data["email"]
        profile.is_email_verified = True
        profile.save()

    # ✅ Log the user in
    user.backend = settings.AUTHENTICATION_BACKENDS[0]
    login(request, user)

    # ✅ Remove cached token
    cache.delete(f"verify_{token}")

    messages.success(request, "Your account has been activated successfully!")
    return redirect("home")

    
@login_required
def remove_cart(request , cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        CartItems.delete()

    except Exception as e :
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





def get_price(request):
    size_name = request.GET.get('size')
    color_name = request.GET.get('color')
    
    # Assuming you have a method to get the price based on size and color
    price = calculate_price(size_name, color_name)
    
    return JsonResponse({'price': price})

def calculate_price(size_name, color_name):

    base_price = 100  # Example base price
    size_price = 10  # Example size price adjustment
    color_price = 5  # Example color price adjustment
    total_price = base_price + size_price + color_price
    return total_price



def product_detail(request, uid):
    product = get_object_or_404(Product, uid=uid)
    reviews = product.reviews.all()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return JsonResponse({'message': 'Review submitted successfully'}, status=200)
    
    context = {
        'product': product,
        'reviews': reviews,
        'form': ReviewForm()
    }
    return render(request, 'home/prod.html', context)





from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import CartItems
from .models import Cart

@require_POST



@csrf_exempt
def update_quantity(request):
    if request.method == 'POST':
        item_id = request.POST.get("item_id")
        quantity = request.POST.get("quantity")

        print("[DEBUG] Raw POST data:", request.POST)
        print("[DEBUG] Received item_id:", item_id)
        print("[DEBUG] Received quantity:", quantity)

        if not item_id or not quantity:
            return JsonResponse({"success": False, "error": "Missing data"}, status=400)

        try:
            quantity = int(quantity)

            # FIX: Use correct model name (if your app uses SavedCartItem)
            cart_item = CartItems.objects.get(id=item_id, cart__user=request.user)

            cart_item.quantity = quantity
            cart_item.save()

            item_total = cart_item.get_total_price()
            cart_items = CartItems.objects.filter(cart__user=request.user)
            cart_total = sum(item.get_total_price() for item in cart_items)

            return JsonResponse({
                "success": True,
                "updated_quantity": quantity,
                "item_total": str(item_total),
                "cart_total": str(cart_total)
            })

        except CartItems.DoesNotExist:
            return JsonResponse({"success": False, "error": "Item not found"}, status=404)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)





from django.contrib.auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset_password.html'  # Your custom reset password page
    email_template_name = 'password_reset_email.html'  # Email content template
    subject_template_name = 'password_reset_subject.txt'  # Subject of the email

def user_main(request):
    return render(request,'user_main.html')

from django.http import JsonResponse
from accounts.models import Category  # Adjust the import path as needed

def get_categories(request):
    categories = Category.objects.all().values('id', 'category_name')
    return JsonResponse(list(categories), safe=False)





from django.http import JsonResponse



from django.shortcuts import redirect
def redirect_user_to_profile(request):
    return redirect("profile")

@login_required
def checkout(request):
    cart = request.session.get('cart', {})  # Fetch cart from session

    # Get the user's profile and filter addresses accordingly
    user_profile = request.user.profile
    addresses = Address.objects.filter(profile=user_profile)  # Use profile, not user

    if not cart:
        return render(request, 'checkout.html', {'error': 'Your cart is empty.'})

    return render(request, 'checkout.html', {'cart': cart, 'addresses': addresses})




def get_addresses(request):
    if request.user.is_authenticated:
        addresses = Address.objects.filter(user=request.user).values(
            'id', 'address_type', 'street', 'city', 'state', 'zip_code', 'country'
        )
        return JsonResponse(list(addresses), safe=False)
    return JsonResponse({'error': 'Unauthorized'}, status=401)

@login_required
@require_POST
def delete_address(request, address_id):
    try:
        address = Address.objects.get(id=address_id, user=request.user)
        address.delete()
        return JsonResponse({'success': True})
    except Address.DoesNotExist:
        return JsonResponse({'success': False})

@login_required
@require_POST
def add_phone(request):
    form = PhoneForm(request.POST)
    if form.is_valid():
        phone = form.save(commit=False)
        phone.user = request.user
        phone.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': form.errors})

@login_required
@require_POST
def delete_phone(request, phone_id):
    try:
        phone = Phone.objects.get(id=phone_id, user=request.user)
        phone.delete()
        return JsonResponse({'success': True})
    except Phone.DoesNotExist:
        return JsonResponse({'success': False})




def custom_logout(request):
    if request.user.is_authenticated:
        # Save cart items to the database
        cart_items = request.session.get('cart', [])
        for item in cart_items:
            product_id = item.get('product_id')
            quantity = item.get('quantity')
            size_id = item.get('size_id')
            color_id = item.get('color_id')

            try:
                product = Product.objects.get(id=product_id)
                size = SizeVariant.objects.get(id=size_id) if size_id else None
                color = ColorVariant.objects.get(id=color_id) if color_id else None

                Cart.objects.update_or_create(
                    user=request.user,
                    product=product,
                    size=size,
                    color=color,
                    defaults={'quantity': quantity}
                )
            except Product.DoesNotExist:
                continue

        # Clear the session
        request.session.flush()

    auth_logout(request)
    return redirect('user_login')  # Redirect to your home page or desired URL


@csrf_exempt
def save_address(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Address.objects.create(
            user=request.user,
            address_type=data["address_type"],
            street=data["street"],
            city=data["city"],
            state=data["state"],
            zip_code=data["zip_code"],
            country=data["country"],
        )
        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)





def get_products(request):
    products = Product.objects.prefetch_related('product_images').all()
    product_list = [
        {
            "id": product.uid,
            "name": product.product_name,
            "price": product.price,
            "image": product.product_images.first().image.url if product.product_images.first() else None
        }
        for product in products
    ]
    return JsonResponse({"products": product_list})





from accounts.models import Category, SizeVariant, ColorVariant

@login_required
def profile_view(request):
    user = request.user
    user_profile, _ = ProFile.objects.get_or_create(user=user)
    address_form = AddressForm()
    orders = Order.objects.filter(user=user).prefetch_related('items').order_by("-created_at")

    products = Product.objects.filter(user=user)
    has_products = products.exists()
    products_count = products.count()

    # 👇 Add these lines to fetch the main image URL for each product, with a fallback to a default image
    for product in products:
        main_image = product.product_images.filter(is_main=True).first()
        if main_image and main_image.image:
            product.main_image_url = main_image.image.url
        else:
            # You can provide a placeholder or default image URL here
            product.main_image_url = "/media/products/default.jpg"  # Update the path to match your default image

    # 👇 Fetch categories, sizes, and colors for the user
    categories = Category.objects.all()
    sizes = SizeVariant.objects.all()
    colors = ColorVariant.objects.all()

    return render(request, "home/user.html", {
        "user_profile": user_profile,
        "address_form": address_form,
        "orders": orders,
        "products": products,
        "has_products": has_products,
        "products_count": products_count,
        "categories": categories,
        "sizes": sizes,
        "colors": colors,
    })




import json
import uuid
import logging
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProFile

from base.emails import send_verification_email


from django.contrib.auth.decorators import login_required
import json
from accounts.models import SavedCart


from accounts.models import Order

def dashboard_view(request):
    user = request.user
    user_profile, created = ProFile.objects.get_or_create(user=user)

    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "").strip()
            last_name = data.get("last_name", "").strip()
            phone = data.get("phone", "").strip()
            house_number = data.get("house_number", "").strip()
            street = data.get("street", "").strip()
            locality = data.get("locality", "").strip()
            address = data.get("address", "").strip()
            coustmer_pincode = data.get("coustmer_pincode", "").strip()
            city = data.get("city", "").strip()
            state = data.get("state", "").strip()

            # Update profile fields if present
            if name:
                user_profile.name = name
            if last_name:
                user_profile.last_name = last_name
            if phone:
                user_profile.phone = phone
            if house_number:
                user_profile.house_number = house_number
            if street:
                user_profile.street = street
            if locality:
                user_profile.locality = locality
            if address:
                user_profile.address = address
            if coustmer_pincode:
                user_profile.coustmer_pincode = coustmer_pincode
            if city:
                user_profile.city = city
            if state:
                user_profile.state = state

            user_profile.save()
            return JsonResponse({"success": True, "message": "Profile updated successfully."})
        
        except json.JSONDecodeError:
            return JsonResponse({"success": False, "message": "Invalid JSON data."}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=500)

    orders = Order.objects.filter(user=user).prefetch_related('items').order_by("-created_at")
    products = Product.objects.filter(user=user)

    return render(request, "home/user.html", {
        "user_profile": user_profile,
        "orders": orders,
        "products": products
    })

from django.shortcuts import redirect

from django.shortcuts import render


from django.contrib.auth.decorators import login_required
from accounts.models import SubOrder



import logging

logger = logging.getLogger(__name__)
@login_required
def sellerdashboard(request):
    user = request.user
    logger.debug(f"[sellerdashboard] View accessed by user: {user.email}")

    user_profile, _ = ProFile.objects.get_or_create(user=user)
    address_form = AddressForm()

    # Get seller's products
    products = Product.objects.filter(user=user)
    has_products = products.exists()
    products_count = products.count()

    # Attach main image URL to each product
    for product in products:
        main_image = product.product_images.filter(is_main=True).first()
        product.main_image_url = main_image.image.url if main_image and main_image.image else "/media/products/default.jpg"

    # Get suborders related to seller
    seller_suborders = SubOrder.objects.filter(seller=user) \
        .select_related('main_order', 'main_order__user__profile') \
        .prefetch_related('items__product') \
        .order_by("-created_at")

    # Count by order status
    pending_orders_count = seller_suborders.filter(status="Pending").count()
    cancelled_orders_count = seller_suborders.filter(status="Cancelled").count()
    shipped_orders_count = seller_suborders.filter(status="Shipped").count()

    logger.debug(f"[sellerdashboard] Orders for {user.email} — Pending: {pending_orders_count}, Cancelled: {cancelled_orders_count}, Shipped: {shipped_orders_count}")

    # Product filters
    categories = Category.objects.all()
    sizes = SizeVariant.objects.all()
    colors = ColorVariant.objects.all()

    return render(request, "sellerdashboard.html", {
        "user_profile": user_profile,
        "address_form": address_form,
        "orders": Order.objects.filter(user=user).prefetch_related('items').order_by("-created_at"),
        "products": products,
        "has_products": has_products,
        "products_count": products_count,
        "categories": categories,
        "sizes": sizes,
        "colors": colors,
        "seller_suborders": seller_suborders,
        "pending_orders_count": pending_orders_count,
        "cancelled_orders_count": cancelled_orders_count,
        "shipped_orders_count": shipped_orders_count,
    })
# def sellerdashboard(request):
#     """Main seller dashboard view"""
#     # Get seller's products
#     products = Product.objects.filter(seller=request.user)

#     # Get seller's suborders
#     seller_suborders = SubOrder.objects.filter(
#         items__product__seller=request.user
#     ).distinct().order_by('-created_at')

#     # Calculate statistics
#     products_count = products.count()
#     pending_orders_count = seller_suborders.filter(status='Pending').count()
#     ready_orders_count = seller_suborders.filter(status='Ready to Ship').count()
#     shipped_orders_count = seller_suborders.filter(status='Shipped').count()
#     cancelled_orders_count = seller_suborders.filter(status='Cancelled').count()

#     # Get categories for the edit form
#     categories = Category.objects.all()

#     context = {
#         'products': products,
#         'seller_suborders': seller_suborders,
#         'products_count': products_count,
#         'pending_orders_count': pending_orders_count,
#         'ready_orders_count': ready_orders_count,
#         'shipped_orders_count': shipped_orders_count,
#         'cancelled_orders_count': cancelled_orders_count,
#         'categories': categories,
#         'cart_count': 0,  # Add cart count if needed
#     }

#     return render(request, 'sellerdashboard.html', context)


from django.contrib import messages


from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse

def remove_product(request, product_id):
    print(f"Attempting to remove product with ID: {product_id}")
    product = get_object_or_404(Product, uid=product_id, user=request.user)
    print(f"Found product: {product}")

    product.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'message': 'Product deleted successfully'})

    messages.success(request, "Product deleted successfully.")
    return redirect('sellerdashboard')



import json
import razorpay
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from accounts.models import Order, OrderItem  # Ensure models are imported




from accounts.models import SavedCart

def cart_count_processor(request):
    if request.user.is_authenticated:
        try:
            saved_cart = SavedCart.objects.get(user=request.user)
            count = sum(item.quantity for item in saved_cart.items.all())
            return {'cart_count': count}
        except SavedCart.DoesNotExist:
            return {'cart_count': 0}
    return {'cart_count': 0}
import razorpay
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Product
from accounts.models import Order
from accounts.models import SavedCartItem
# Initialize Razorpay client
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
import razorpay
from decimal import Decimal



from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
import requests



from collections import defaultdict
from decimal import Decimal
import requests
from django.conf import settings
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin



from decimal import Decimal
from collections import defaultdict
from django.views import View
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
import logging



import logging
import requests
from decimal import Decimal
from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from razorpay import Client
from django.conf import settings
# from .models import ProFile, SavedCart, SavedCartItem, Order
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
logger = logging.getLogger(__name__)
@method_decorator(csrf_exempt, name='dispatch')


# class CreatePaymentView(View):
#     def post(self, request, *args, **kwargs):
#         user = request.user
#         profile = get_object_or_404(ProFile, user=user)
#         delivery_pincode = profile.coustmer_pincode

#         logger.debug(f"[CreatePaymentView] Checkout POST received | User: {user.email}")

#         try:
#             cart = SavedCart.objects.get(user=user)
#             cart_items = SavedCartItem.objects.filter(cart=cart)
#         except SavedCart.DoesNotExist:
#             logger.warning(f"[CreatePaymentView] No cart found for user {user.id}")
#             return JsonResponse({'error': 'Cart is empty'}, status=400)

#         subtotal = sum(Decimal(item.get_total_price()) for item in cart_items).quantize(Decimal('0.01'))
#         logger.debug(f"[CreatePaymentView] Subtotal: ₹{subtotal}")

#         discount = Decimal(str(request.session.get('pending_discount_amount', 0))).quantize(Decimal('0.01'))
#         discounted_total = (subtotal - discount).quantize(Decimal('0.01'))
#         logger.debug(f"[CreatePaymentView] Discount: ₹{discount} | Discounted Total: ₹{discounted_total}")

#         try:
#             auth_res = requests.post(
#                 "https://sr-auth.shiprocket.in/v1/external/auth/login",
#                 json={"email": settings.SHIPROCKET_EMAIL, "password": settings.SHIPROCKET_PASSWORD}
#             )
#             shiprocket_token = auth_res.json().get("token")
#             headers = {"Authorization": f"Bearer {shiprocket_token}"}
#             logger.debug("[CreatePaymentView] Shiprocket token successfully obtained.")
#         except Exception as e:
#             logger.error(f"[CreatePaymentView] Shiprocket auth failed: {e}")
#             return JsonResponse({'error': 'Shipping service error'}, status=500)

#         shipping_cost = Decimal("0.00")
#         shipping_breakdown = []

#         for item in cart_items:
#             product = item.product
#             quantity = item.quantity

#             if not all([product.weight, product.length, product.breadth, product.height]):
#                 fallback_cost = Decimal("120.00") * quantity
#                 shipping_cost += fallback_cost
#                 logger.warning(f"[CreatePaymentView] Missing dimensions for product {product.uid}, fallback ₹{fallback_cost}")
#                 shipping_breakdown.append({
#                     "product": product.product_name,
#                     "product_id": str(product.uid),
#                     "provider": "Fallback",
#                     "cost": float(fallback_cost),
#                     "reason": "Missing dimensions"
#                 })
#                 continue

#             params = {
#                 "pickup_postcode": product.pincode,
#                 "delivery_postcode": delivery_pincode,
#                 "weight": product.weight,
#                 "length": product.length,
#                 "breadth": product.breadth,
#                 "height": product.height,
#                 "cod": 0
#             }

#             url = "https://apiv2.shiprocket.in/v1/external/courier/serviceability/"

#             try:
#                 response = requests.get(url, params=params, headers=headers, timeout=10)
#                 data = response.json()

#                 if data.get("data") and data["data"].get("available_courier_companies"):
#                     cheapest = min(data["data"]["available_courier_companies"], key=lambda c: c["rate"])
#                     rate = Decimal(str(cheapest["rate"])).quantize(Decimal('0.01'))
#                     total_rate = rate * quantity
#                     shipping_cost += total_rate

#                     logger.info(f"[CreatePaymentView] Courier for {product.product_name} (x{quantity}): {cheapest['courier_name']} at ₹{total_rate}")

#                     shipping_breakdown.append({
#                         "product": product.product_name,
#                         "product_id": str(product.uid),
#                         "provider": cheapest['courier_name'],
#                         "cost": float(total_rate),
#                         "estimated_delivery_days": cheapest.get("estimated_delivery_days"),
#                     })
#                 else:
#                     fallback = Decimal("120.00") * quantity
#                     shipping_cost += fallback
#                     logger.warning(f"[CreatePaymentView] No courier found for product {product.uid}. Fallback ₹{fallback}")
#                     shipping_breakdown.append({
#                         "product": product.product_name,
#                         "product_id": str(product.uid),
#                         "provider": "Fallback",
#                         "cost": float(fallback),
#                         "reason": "No courier found"
#                     })

#             except requests.exceptions.Timeout:
#                 fallback = Decimal("120.00") * quantity
#                 shipping_cost += fallback
#                 logger.warning(f"[CreatePaymentView] Timeout while fetching rate for {product.uid}. Fallback ₹{fallback}")
#                 shipping_breakdown.append({
#                     "product": product.product_name,
#                     "product_id": str(product.uid),
#                     "provider": "Fallback",
#                     "cost": float(fallback),
#                     "reason": "Request timeout"
#                 })
#             except Exception as e:
#                 fallback = Decimal("120.00") * quantity
#                 shipping_cost += fallback
#                 logger.error(f"[CreatePaymentView] Error for product {product.uid}: {e}. Fallback ₹{fallback}")
#                 shipping_breakdown.append({
#                     "product": product.product_name,
#                     "product_id": str(product.uid),
#                     "provider": "Fallback",
#                     "cost": float(fallback),
#                     "reason": "Rate fetch error"
#                 })

#         final_total = (discounted_total + shipping_cost).quantize(Decimal('0.01'))
#         amount_paisa = int((final_total * 100).quantize(Decimal('1')))
#         logger.debug(f"[CreatePaymentView] Final total ₹{final_total}, amount in paisa: {amount_paisa}")

#         client = Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
#         payment = client.order.create({
#             "amount": amount_paisa,
#             "currency": "INR",
#             "payment_capture": 1
#         })
#         logger.debug(f"[CreatePaymentView] Razorpay order created: {payment['id']}")

#         Order.objects.create(
#             user=user,
#             name=user.get_full_name(),
#             email=user.email,
#             phone=profile.phone or "",
#             address=', '.join(filter(None, [
#                 profile.house_number,
#                 profile.street,
#                 profile.locality,
#                 profile.city,
#                 profile.state,
#                 str(profile.coustmer_pincode)
#             ])),
#             payment_method="Prepaid",
#             razorpay_order_id=payment["id"],
#             total_amount=final_total,
#             shipping_cost=shipping_cost,
#             is_paid=False,
#         )
#         logger.info(f"[CreatePaymentView] Temporary Order created for Razorpay order {payment['id']}")

#         return JsonResponse({
#             "order_id": payment["id"],
#             "amount": amount_paisa,
#             "currency": "INR",
#             "razorpay_key_id": settings.RAZORPAY_KEY_ID,
#             "shipping_cost": float(shipping_cost),
#             "total_shipping": float(shipping_cost),
#             "shipping_breakdown": shipping_breakdown,
#             "subtotal": float(subtotal),
#             "discount_amount": float(discount),
#             "total": float(final_total),
#             "user_name": user.get_full_name(),
#             "user_email": user.email,
#             "user_contact": profile.phone,
#         })
class CreatePaymentView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(ProFile, user=user)
        delivery_pincode = profile.coustmer_pincode

        logger.debug(f"[CreatePaymentView] Checkout POST received | User: {user.email}")

        try:
            cart = SavedCart.objects.get(user=user)
            cart_items = SavedCartItem.objects.filter(cart=cart)
        except SavedCart.DoesNotExist:
            logger.warning(f"[CreatePaymentView] No cart found for user {user.id}")
            return JsonResponse({'error': 'Cart is empty'}, status=400)

        subtotal = sum(Decimal(item.get_total_price()) for item in cart_items).quantize(Decimal('0.01'))
        logger.debug(f"[CreatePaymentView] Subtotal: ₹{subtotal}")

        discount = Decimal(str(request.session.get('pending_discount_amount', 0))).quantize(Decimal('0.01'))
        discounted_total = (subtotal - discount).quantize(Decimal('0.01'))
        logger.debug(f"[CreatePaymentView] Discount: ₹{discount} | Discounted Total: ₹{discounted_total}")

        try:
            auth_res = requests.post(
                "https://sr-auth.shiprocket.in/v1/external/auth/login",
                json={"email": settings.SHIPROCKET_EMAIL, "password": settings.SHIPROCKET_PASSWORD}
            )
            shiprocket_token = auth_res.json().get("token")
            headers = {"Authorization": f"Bearer {shiprocket_token}"}
            logger.debug("[CreatePaymentView] Shiprocket token successfully obtained.")
        except Exception as e:
            logger.error(f"[CreatePaymentView] Shiprocket auth failed: {e}")
            return JsonResponse({'error': 'Shipping service error'}, status=500)

        shipping_cost = Decimal("0.00")
        shipping_breakdown = []
        sellers_set = set()

        for item in cart_items:
            product = item.product
            quantity = item.quantity
            sellers_set.add(product.user_id)

            if not all([product.weight, product.length, product.breadth, product.height]):
                fallback_cost = Decimal("120.00") * quantity
                shipping_cost += fallback_cost
                logger.warning(f"[CreatePaymentView] Missing dimensions for product {product.uid}, fallback ₹{fallback_cost}")
                shipping_breakdown.append({
                    "product": product.product_name,
                    "product_id": str(product.uid),
                    "provider": "Fallback",
                    "cost": float(fallback_cost),
                    "reason": "Missing dimensions"
                })
                continue

            params = {
                "pickup_postcode": product.pincode,
                "delivery_postcode": delivery_pincode,
                "weight": product.weight,
                "length": product.length,
                "breadth": product.breadth,
                "height": product.height,
                "cod": 0
            }

            url = "https://apiv2.shiprocket.in/v1/external/courier/serviceability/"

            try:
                response = requests.get(url, params=params, headers=headers, timeout=10)
                data = response.json()

                if data.get("data") and data["data"].get("available_courier_companies"):
                    cheapest = min(data["data"]["available_courier_companies"], key=lambda c: c["rate"])
                    rate = Decimal(str(cheapest["rate"])).quantize(Decimal('0.01'))
                    total_rate = rate * quantity
                    shipping_cost += total_rate

                    logger.info(f"[CreatePaymentView] Courier for {product.product_name} (x{quantity}): {cheapest['courier_name']} at ₹{total_rate}")

                    shipping_breakdown.append({
                        "product": product.product_name,
                        "product_id": str(product.uid),
                        "provider": cheapest['courier_name'],
                        "cost": float(total_rate),
                        "estimated_delivery_days": cheapest.get("estimated_delivery_days"),
                    })
                else:
                    fallback = Decimal("120.00") * quantity
                    shipping_cost += fallback
                    logger.warning(f"[CreatePaymentView] No courier found for product {product.uid}. Fallback ₹{fallback}")
                    shipping_breakdown.append({
                        "product": product.product_name,
                        "product_id": str(product.uid),
                        "provider": "Fallback",
                        "cost": float(fallback),
                        "reason": "No courier found"
                    })

            except requests.exceptions.Timeout:
                fallback = Decimal("120.00") * quantity
                shipping_cost += fallback
                logger.warning(f"[CreatePaymentView] Timeout while fetching rate for {product.uid}. Fallback ₹{fallback}")
                shipping_breakdown.append({
                    "product": product.product_name,
                    "product_id": str(product.uid),
                    "provider": "Fallback",
                    "cost": float(fallback),
                    "reason": "Request timeout"
                })
            except Exception as e:
                fallback = Decimal("120.00") * quantity
                shipping_cost += fallback
                logger.error(f"[CreatePaymentView] Error for product {product.uid}: {e}. Fallback ₹{fallback}")
                shipping_breakdown.append({
                    "product": product.product_name,
                    "product_id": str(product.uid),
                    "provider": "Fallback",
                    "cost": float(fallback),
                    "reason": "Rate fetch error"
                })

        platform_fee = Decimal("10.00") * len(sellers_set)
        logger.debug(f"[CreatePaymentView] Platform Fee: ₹{platform_fee}")

        final_total = (discounted_total + shipping_cost + platform_fee).quantize(Decimal('0.01'))
        amount_paisa = int((final_total * 100).quantize(Decimal('1')))
        logger.debug(f"[CreatePaymentView] Final total ₹{final_total}, amount in paisa: {amount_paisa}")

        client = Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        payment = client.order.create({
            "amount": amount_paisa,
            "currency": "INR",
            "payment_capture": 1
        })
        logger.debug(f"[CreatePaymentView] Razorpay order created: {payment['id']}")

        Order.objects.create(
            user=user,
            name=user.get_full_name(),
            email=user.email,
            phone=profile.phone or "",
            address=', '.join(filter(None, [
                profile.house_number,
                profile.street,
                profile.locality,
                profile.city,
                profile.state,
                str(profile.coustmer_pincode)
            ])),
            payment_method="Prepaid",
            razorpay_order_id=payment["id"],
            total_amount=final_total,
            shipping_cost=shipping_cost,
            is_paid=False,
        )
        logger.info(f"[CreatePaymentView] Temporary Order created for Razorpay order {payment['id']}")

        return JsonResponse({
            "order_id": payment["id"],
            "amount": amount_paisa,
            "currency": "INR",
            "razorpay_key_id": settings.RAZORPAY_KEY_ID,
            "shipping_cost": float(shipping_cost),
            "total_shipping": float(shipping_cost),
            "shipping_breakdown": shipping_breakdown,
            "subtotal": float(subtotal),
            "discount_amount": float(discount),
            "platform_fee": float(platform_fee),
            "total": float(final_total),
            "user_name": user.get_full_name(),
            "user_email": user.email,
            "user_contact": profile.phone,
        })

from_email = settings.EMAIL_HOST_USER  # for sending from your Gmail

from accounts.tasks import send_confirmation_emails_task  
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import razorpay
import logging
from accounts.models import PromoCode
from decimal import Decimal
import json
from django.http import JsonResponse
# from .models import PromoCode, SavedCart, SavedCartItem
from accounts.views import calculate_shipping_rate
from decimal import Decimal
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def apply_promo_code(request):
    if request.method != 'POST':
        logger.warning("[apply_promo_code] Invalid request method.")
        return JsonResponse({'error': 'Invalid request method.'}, status=405)

    try:
        data = json.loads(request.body)
        promo_code = data.get('promo_code', '').strip()
        if not promo_code:
            logger.warning("[apply_promo_code] Promo code missing in request.")
            return JsonResponse({'error': 'Promo code is required.'}, status=400)
    except json.JSONDecodeError as e:
        logger.error(f"[apply_promo_code] JSON decode error: {e}")
        return JsonResponse({'error': 'Invalid JSON request'}, status=400)

    try:
        promo = PromoCode.objects.get(code__iexact=promo_code)
        logger.debug(f"[apply_promo_code] Promo code '{promo_code}' found.")
    except PromoCode.DoesNotExist:
        logger.warning(f"[apply_promo_code] Promo code '{promo_code}' not found.")
        return JsonResponse({'error': 'Invalid promo code.'}, status=400)

    if promo.used_by.filter(id=request.user.id).exists():
        logger.info(f"[apply_promo_code] User {request.user.id} already used promo code '{promo_code}'.")
        return JsonResponse({'error': 'You have already used this promo code.'}, status=400)

    if promo.is_used:
        logger.info(f"[apply_promo_code] Promo code '{promo_code}' is marked as used.")
        return JsonResponse({'error': 'This promo code has already been used.'}, status=400)

    cart = SavedCart.objects.filter(user=request.user).first()
    if not cart:
        logger.warning(f"[apply_promo_code] Cart not found for user {request.user.id}.")
        return JsonResponse({'error': 'Your cart is empty.'}, status=400)

    cart_items = SavedCartItem.objects.filter(cart=cart)
    if not cart_items.exists():
        logger.warning(f"[apply_promo_code] Cart items not found for cart {cart.id}.")
        return JsonResponse({'error': 'Your cart is empty.'}, status=400)

    # Log each cart item
    for item in cart_items:
        logger.debug(f"[apply_promo_code] Item: {item.product.product_name}, Qty: {item.quantity}, Price: {item.get_total_price()}")

    subtotal = sum(Decimal(str(item.get_total_price())) for item in cart_items)
    logger.debug(f"[apply_promo_code] Subtotal before discount: ₹{subtotal}")

    discount_amount = Decimal(str(promo.discount_percentage))
    discount_amount = min(discount_amount, subtotal).quantize(Decimal('0.01'))
    logger.debug(f"[apply_promo_code] Discount applied: ₹{discount_amount}")

    # Shipping cost calculation (fixed: multiplied by quantity)
    shipping_cost = Decimal('0.00')
    profile = request.user.profile

    for item in cart_items:
        product = item.product
        quantity = item.quantity

        try:
            result = calculate_shipping_rate(product, profile)
            rate = Decimal(str(result.get('rate'))) if result.get('rate') else Decimal('120.00')
            total_rate = rate * quantity
            shipping_cost += total_rate
            logger.debug(f"[apply_promo_code] Shipping rate for product {product.uid}: ₹{rate} × {quantity} = ₹{total_rate}")
        except Exception as e:
            fallback = Decimal('120.00') * quantity
            logger.error(f"[apply_promo_code] Shipping rate fetch failed for product {product.uid}: {e}")
            shipping_cost += fallback

    total = (subtotal - discount_amount + shipping_cost).quantize(Decimal('0.01'))
    logger.debug(f"[apply_promo_code] Final total: ₹{total}")

    # Save to session
    request.session['pending_promo_id'] = promo.id
    request.session['pending_discount_amount'] = float(discount_amount)
    logger.info(f"[apply_promo_code] Promo code '{promo_code}' applied successfully for user {request.user.id}.")

    discounted_subtotal = (subtotal - discount_amount).quantize(Decimal('0.01'))

    return JsonResponse({
        'discount_amount': float(discount_amount),
        'subtotal': float(discounted_subtotal),  # 👈 Updated to reflect discount
        'shipping_cost': float(shipping_cost),
        'total': float(total)
    }, status=200)


# from accounts.views import get_shiprocket_token, create_shiprocket_order



# logger = logging.getLogger(__name__)


# @method_decorator(csrf_exempt, name='dispatch')
from django.views import View
from accounts.views import split_and_create_orders
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from accounts.models import Order, SavedCart, OrderItem, PromoCode  # Adjust to your app name
from accounts.views import get_shiprocket_token,  create_shiprocket_order
from accounts.tasks import send_confirmation_emails_task  
import razorpay
import logging
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from decimal import Decimal
import json
import logging
import razorpay
from accounts.models import SubOrder

logger = logging.getLogger(__name__)
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
@method_decorator(csrf_exempt, name='dispatch')




class PaymentCallbackView(View):
    def post(self, request):
        data = request.POST
        order_id = data.get("razorpay_order_id")
        payment_id = data.get("razorpay_payment_id")
        signature = data.get("razorpay_signature")

        try:
            order = get_object_or_404(Order, razorpay_order_id=order_id)

            # ✅ Verify Razorpay payment signature
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            })

            # ✅ Update order with payment details
            order.razorpay_payment_id = payment_id
            order.razorpay_signature = signature
            order.transaction_id = payment_id
            order.payment_method = "Prepaid"  # <-- Add this line
            order.is_paid = True
            order.status = 'Pending'
            order.save()


            # ✅ Apply promo code if available
            if 'pending_promo_id' in request.session:
                promo_id = request.session.pop('pending_promo_id')
                discount = request.session.pop('pending_discount_amount', None)
                promo = PromoCode.objects.get(id=promo_id)
                promo.is_used = True
                promo.used_by.add(request.user)
                promo.save()

            # ✅ Retrieve cart
            cart = SavedCart.objects.filter(user=order.user).first()
            if not cart:
                return JsonResponse({"status": "failed", "reason": "Cart not found"})

            cart_items = cart.items.select_related('product')

            # ✅ Parse shipping breakdown from frontend (with fallback)
            try:
                raw_breakdown = request.POST.get("shipping_breakdown", "[]")
                shipping_breakdown = json.loads(raw_breakdown)
            except json.JSONDecodeError:
                shipping_breakdown = []

            # ✅ Patch product.id → product.uid
            for item in shipping_breakdown:
                if 'product_id' in item:
                    item['product_id'] = str(item['product_id'])

            # ✅ Get Shiprocket token
            token = get_shiprocket_token()

            # ✅ Split and create orders per seller
            created_orders = split_and_create_orders(
                user=request.user,
                cart_items=cart_items,
                base_order=order,
                shipping_breakdown=shipping_breakdown,
                shiprocket_token=token
            )

            # ✅ Clear cart
            cart.items.all().delete()

            # ✅ Send confirmation emails
            for o in created_orders:
                if isinstance(o, SubOrder):
                    send_confirmation_emails_task.delay(o.id) 

            return JsonResponse({"status": "success"})

        except Exception as e:
            logger.error(f"[ERROR] PaymentCallbackView failed: {e}")
            return JsonResponse({"status": "failed", "reason": str(e)})

from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetConfirmView

from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

class CustomPasswordResetView(auth_views.PasswordResetView):
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'reset_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain'] = '127.0.0.1:8000'  # or 'localhost:8000'
        context['protocol'] = 'http'
        return context

    

    from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetConfirmView

from django.contrib.auth.views import PasswordResetConfirmView
from django.utils import timezone

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.user
        if hasattr(user, 'profile'):
            user.profile.last_password_reset = timezone.now()
            # Optionally, mark email verified on password reset
            user.profile.is_email_verified = True
            user.profile.save()
        return response

from django.http import JsonResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# from .models import Product, ProductImage, SizeVariant, ColorVariant

@login_required
@require_POST
def edit_product(request, product_id):
    product = get_object_or_404(Product, uid=product_id, user=request.user)

    # 📌 Basic fields
    product.product_name = request.POST.get("product_name")
    product.price = request.POST.get("price")
    product.product_description = request.POST.get("product_description")
    product.category_id = request.POST.get("category")
    product.save()

    # 🔄 Clear old variants
    product.size_variants.clear()
    product.color_variants.clear()

    # 🔢 Size Variants
    size_names = request.POST.getlist("size_name[]")
    size_prices = request.POST.getlist("size_price[]")
    for name, price in zip(size_names, size_prices):
        if name.strip():
            size = SizeVariant.objects.create(size_name=name.strip(), price=int(price or 0))
            product.size_variants.add(size)

    # 🎨 Color Variants
    color_names = request.POST.getlist("color_name[]")
    color_prices = request.POST.getlist("color_price[]")
    for name, price in zip(color_names, color_prices):
        if name.strip():
            color = ColorVariant.objects.create(color_name=name.strip(), price=float(price or 0))
            product.color_variants.add(color)

    # 🖼 Replace Main Image (is_main=True)
    if request.FILES.get("main_image"):
        # Delete existing main image
        existing_main = product.product_images.filter(is_main=True).first()
        if existing_main:
            existing_main.delete()

        # Save new main image
        ProductImage.objects.create(
            product=product,
            image=request.FILES["main_image"],
            is_main=True
        )

    # ➕ Additional Images (is_main=False by default)
    additional_images = request.FILES.getlist("additional_images")
    if len(additional_images) > 3:
        return JsonResponse({"error": "You can upload a maximum of 3 additional images."}, status=400)

    # 🔁 Optional: clear old additional images if new ones uploaded
    if additional_images:
        product.product_images.filter(is_main=False).delete()
        for img in additional_images:
            ProductImage.objects.create(product=product, image=img)

    # ✅ Get updated images
    main_image_obj = product.product_images.filter(is_main=True).first()
    main_image_url = main_image_obj.image.url if main_image_obj else ""

    additional_image_urls = [
        img.image.url for img in product.product_images.filter(is_main=False)
    ]

    # ✅ Return updated info with image URLs
    return JsonResponse({
        "product_name": product.product_name,
        "price": product.price,
        "product_description": product.product_description,
        "main_image_url": main_image_url,
        "additional_images": additional_image_urls,
    })



@method_decorator(csrf_exempt, name='dispatch')
class CreateSellerPaymentView(LoginRequiredMixin, View):
    def post(self, request):
        data = json.loads(request.body)
        product_fee = Decimal('3.00')  # ₹3 per product
        amount_in_paisa = int(product_fee * 100)

        razorpay_order = client.order.create({
            "amount": amount_in_paisa,
            "currency": "INR",
            "payment_capture": 1
        })

        # Optionally, log seller payment intent in DB if you want

        return JsonResponse({
            "order_id": razorpay_order["id"],
            "razorpay_key_id": settings.RAZORPAY_KEY_ID,
            "amount": amount_in_paisa,
        })


# from .models import Product, Category, ColorVariant, SizeVariant, ProductImage
# from .models import Product, ProductImage, ColorVariant, SizeVariant, Category

logger = logging.getLogger(__name__)

from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
# from .models import Product, Category, ProductImage, ProFile
from django.core.files.base import ContentFile
import uuid
import razorpay
from .models import SellerPayment
@method_decorator(csrf_exempt, name='dispatch')
class SellerPaymentCallbackView(LoginRequiredMixin, View):
    def post(self, request):
        user = request.user
        profile = user.profile

        # Step 1: Verify Razorpay signature
        razorpay_order_id = request.POST.get("razorpay_order_id")
        razorpay_payment_id = request.POST.get("razorpay_payment_id")
        razorpay_signature = request.POST.get("razorpay_signature")

        client = razorpay.Client(auth=("rzp_test_4t8nCdN7uI0xEP", "6PWff6o8IE8dtouN2DMfBquc"))

        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': razorpay_payment_id,
                'razorpay_signature': razorpay_signature
            })
        except razorpay.errors.SignatureVerificationError:
            return JsonResponse({"status": "failure", "error": "Payment verification failed."}, status=400)

        # Step 2: Mark user as seller (if not already)
        if not profile.is_seller:
            profile.is_seller = True
            profile.save()

        # Step 3: Log the verified payment
        SellerPayment.objects.create(
            user=user,
            razorpay_order_id=razorpay_order_id,
            razorpay_payment_id=razorpay_payment_id,
            amount=Decimal('3.00'),
            status='paid'
        )

        # Step 4: Create Product ONLY after verified payment
        product_name = request.POST.get("product_name")
        description = request.POST.get("description")
        base_price = request.POST.get("base_price")
        category_id = request.POST.get("category_id")

        weight = request.POST.get("weight")
        length = request.POST.get("length")
        breadth = request.POST.get("breadth")
        height = request.POST.get("height")
        pincode = request.POST.get("pincode")

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return JsonResponse({"status": "failure", "error": "Invalid category"})

        product = Product.objects.create(
            product_name=product_name,
            product_description=description,
            category=category,
            price=base_price,
            slug=slugify(product_name),
            user=user,
            weight=weight,
            length=length,
            breadth=breadth,
            height=height,
            pincode=pincode
        )

        # Save main image
        main_image = request.FILES.get("main_image")
        if main_image:
            ProductImage.objects.create(product=product, image=main_image)

        # Save additional images
        for i in range(3):
            image = request.FILES.get(f"additional_image_{i}")
            if image:
                ProductImage.objects.create(product=product, image=image)

        # Handle colors
        colors_json = request.POST.get("colors")
        if colors_json:
            import json
            colors = json.loads(colors_json)
            for color in colors:
                name = color['name']
                price = color['price']
                color_obj, _ = ColorVariant.objects.get_or_create(color_name=name, defaults={'price': price})
                product.color_variants.add(color_obj)

        # Handle sizes
        sizes_json = request.POST.get("sizes")
        if sizes_json:
            sizes = json.loads(sizes_json)
            for size in sizes:
                name = size['name']
                price = size['price']
                size_obj, _ = SizeVariant.objects.get_or_create(size_name=name, defaults={'price': price})
                product.size_variants.add(size_obj)

        return JsonResponse({
    "status": "success",
    "product_id": str(product.uid),
    "redirect_url": "/sellerdashboard/"
})


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils.text import slugify
import uuid
import base64


@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Extract fields
        product_name = data['productName']
        description = data['description']
        base_price = int(data['basePrice'])
        category_name = data['category']
        color_variants = data['colors']
        size_variants = data['sizes']
        main_image_data = data['mainImage']
        additional_images = data['additionalImages']

        # Category
        category = Category.objects.get(name=category_name)

        # Create Product
        product = Product.objects.create(
            product_name=product_name,
            product_description=description,
            category=category,
            price=base_price,
            slug=slugify(product_name),
        )

        # Handle Colors
        for color in color_variants:
            color_obj, _ = ColorVariant.objects.get_or_create(
                color_name=color['name'],
                defaults={'price': float(color['price'])}
            )
            product.color_variants.add(color_obj)

        # Handle Sizes
        for size in size_variants:
            size_obj, _ = SizeVariant.objects.get_or_create(
                size_name=size['name'],
                defaults={'price': int(size['price'])}
            )
            product.size_variants.add(size_obj)

        # Decode and save main image
        if main_image_data:
            format, imgstr = main_image_data.split(';base64,')
            ext = format.split('/')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            image = ContentFile(base64.b64decode(imgstr), name=filename)
            ProductImage.objects.create(product=product, image=image)

        # Additional images
        for img_data in additional_images:
            format, imgstr = img_data.split(';base64,')
            ext = format.split('/')[-1]
            filename = f"{uuid.uuid4()}.{ext}"
            image = ContentFile(base64.b64decode(imgstr), name=filename)
            ProductImage.objects.create(product=product, image=image)

        return JsonResponse({'message': 'Product created successfully'})



