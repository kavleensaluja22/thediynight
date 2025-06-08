from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse , HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate ,  logout 
from django.contrib.auth import authenticate, login as auth_login
from .models import ProFile 
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
    # Logic to calculate price based on size and color
    # This is a placeholder; you should implement your actual logic here
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




@login_required
def update_quantity(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    action = request.GET.get('action')
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease' and cart_item.quantity > 1:
        cart_item.quantity -= 1
    cart_item.save()
    return redirect('cart')

def track(request):
    return render(request,'home/track.html')
from django.contrib.auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset_password.html'  # Your custom reset password page
    email_template_name = 'password_reset_email.html'  # Email content template
    subject_template_name = 'password_reset_subject.txt'  # Subject of the email

def user_main(request):
    return render(request,'user_main.html')


import base64
import uuid
from django.core.files.base import ContentFile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Product, ColorVariant, SizeVariant, ProductImage, Category
from django.utils.text import slugify
import json

# def user(request):
#     return render(request,'home/user.html')
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





from django.http import JsonResponse







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
    user = request.user  # ✅ Add this line!
    user_profile, created = ProFile.objects.get_or_create(user=user)

    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name", "").strip()
        phone = data.get("phone", "").strip()
        address = data.get("address", "").strip()
        coustmer_pincode = data.get("coustmer_pincode", "").strip()
        if name:
            user_profile.name = name
        if phone:
            user_profile.phone = phone
        if address:
            user_profile.address = address
        if coustmer_pincode:
            user_profile.coustmer_pincode = coustmer_pincode

        user_profile.save()
        return JsonResponse({"success": True, "message": "Profile updated successfully."})

    orders = Order.objects.filter(user=user).prefetch_related('items').order_by("-created_at")
    products = Product.objects.filter(user=request.user)
    return render(request, "home/user.html", {
        "user_profile": user_profile,
        "orders": orders,
        "products": products
    })



    

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
    return redirect('redirect_user_to_profile')



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
# from accounts.models import SavedCart, SavedCartItem, Order

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

@method_decorator(csrf_exempt, name='dispatch')



class CreatePaymentView(LoginRequiredMixin, View):
    def post(self, request):
        cart = SavedCart.objects.filter(user=request.user).first()
        cart_items = SavedCartItem.objects.filter(cart=cart)

        if not cart or not cart_items.exists():
            return JsonResponse({"error": "Cart is empty"}, status=400)

        # Get subtotal (before any discounts)
        subtotal = sum(Decimal(str(item.get_price())) for item in cart_items)

        # Get discount from session if user applied promo
        discount_amount = Decimal(str(request.session.get('pending_discount_amount', 0)))

        # Calculate total after discount
        discounted_total = subtotal - discount_amount

        # Add shipping cost
        shipping_cost = Decimal('120')
        total = discounted_total + shipping_cost

        # Ensure the amount is in paisa (smallest unit of INR)
        amount_in_paisa = int(total * 100)

        # Create Razorpay order
        razorpay_order = client.order.create({
            "amount": amount_in_paisa,
            "currency": "INR",
            "payment_capture": 1
        })

        # Save order to database
        order = Order.objects.create(
            user=request.user,
            name=request.user.profile.name or request.user.get_full_name(),
            email=request.user.email,
            phone=request.user.profile.phone or "",
            address=request.user.profile.address or "Not Provided",
            payment_method="Razorpay",
            transaction_id=razorpay_order["id"],
            total_amount=float(total),
            razorpay_order_id=razorpay_order["id"]
        )

        return JsonResponse({
            "order_id": razorpay_order["id"],
            "razorpay_key_id": settings.RAZORPAY_KEY_ID,
            "amount": amount_in_paisa,
            "product_name": "Cart Purchase + Shipping",
            "user_name": order.name,
            "user_email": order.email,
            "user_contact": getattr(request.user.profile, 'phone', ''),
            "callback_url": "/payment-callback/",
            "shipping_cost": float(shipping_cost),
            "subtotal": float(subtotal),
            "total": float(total),
            "discount_amount": float(discount_amount)
        })

from django.conf import settings

from_email = settings.EMAIL_HOST_USER  # for sending from your Gmail

from accounts.views import send_confirmation_emails
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

def apply_promo_code(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            promo_code = data.get('promo_code', '').strip()
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON request'}, status=400)

        try:
            promo = PromoCode.objects.get(code=promo_code)
        except PromoCode.DoesNotExist:
            return JsonResponse({'error': 'Invalid promo code.'}, status=400)

        if promo.used_by.filter(id=request.user.id).exists():
            return JsonResponse({'error': 'You have already used this promo code.'}, status=400)

        if promo.is_used:
            return JsonResponse({'error': 'This promo code has already been used globally.'}, status=400)

        # Calculate cart subtotal
        cart = SavedCart.objects.filter(user=request.user).first()
        if not cart:
            return JsonResponse({'error': 'Your cart is empty.'}, status=400)

        cart_items = SavedCartItem.objects.filter(cart=cart)
        subtotal = sum(Decimal(str(item.get_price())) for item in cart_items)  # Ensure it's Decimal

        # Apply flat discount (not percentage)
        discount_amount = Decimal(str(promo.discount_percentage))  # Treat this as flat ₹ amount

        # Ensure discount does not exceed subtotal
        discount_amount = min(discount_amount, subtotal)
        discount_amount = round(discount_amount, 2)

        # Calculate total with shipping
        shipping_cost = Decimal('120')  # Ensure this is Decimal
        total = round(subtotal - discount_amount + shipping_cost, 2)

        # Store in session as JSON-safe types
        request.session['pending_promo_id'] = promo.id
        request.session['pending_discount_amount'] = float(discount_amount)

        return JsonResponse({
            'discount_amount': float(discount_amount),
            'subtotal': float(subtotal),
            'total': float(total)
        }, status=200)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')

class PaymentCallbackView(View):
    def post(self, request):
        data = request.POST
        order_id = data.get("razorpay_order_id")
        payment_id = data.get("razorpay_payment_id")
        signature = data.get("razorpay_signature")

        try:
            order = get_object_or_404(Order, razorpay_order_id=order_id)

            client = razorpay.Client(auth=("rzp_test_4t8nCdN7uI0xEP", "6PWff6o8IE8dtouN2DMfBquc"))
            client.utility.verify_payment_signature({
                "razorpay_order_id": order_id,
                "razorpay_payment_id": payment_id,
                "razorpay_signature": signature
            })

            order.razorpay_payment_id = payment_id
            order.razorpay_signature = signature
            order.is_paid = True
            order.save()

            # Apply promo if present in session
            if 'pending_promo_id' in request.session:
                promo_id = request.session['pending_promo_id']
                promo = PromoCode.objects.get(id=promo_id)
                promo.is_used = True
                promo.used_by.add(request.user)
                promo.save()
                del request.session['pending_promo_id']
                del request.session['pending_discount_amount']

            saved_cart = SavedCart.objects.filter(user=order.user).first()
            if saved_cart:
                cart_items = saved_cart.get_items()
                for item in cart_items:
                    product = item.product
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item.quantity,
                        price=item.get_price()
                    )
                saved_cart.items.all().delete()

            send_confirmation_emails(order)
            return JsonResponse({"status": "success"})
        
        except Exception as e:
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
# from .models import Product, Category, ColorVariant, SizeVariant, ProductImage
# from .models import Product, ProductImage, ColorVariant, SizeVariant, Category

logger = logging.getLogger(__name__)

@method_decorator(csrf_exempt, name='dispatch')
class SellerPaymentCallbackView(View):

    def post(self, request):
        try:
            razorpay_order_id = request.POST.get('razorpay_order_id')
            razorpay_payment_id = request.POST.get('razorpay_payment_id')
            razorpay_signature = request.POST.get('razorpay_signature')

            if not all([razorpay_order_id, razorpay_payment_id, razorpay_signature]):
                logger.warning("Missing required Razorpay fields.")
                return JsonResponse({'status': 'failure', 'message': 'Missing payment verification fields.'}, status=400)

            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            try:
                client.utility.verify_payment_signature({
                    'razorpay_order_id': razorpay_order_id,
                    'razorpay_payment_id': razorpay_payment_id,
                    'razorpay_signature': razorpay_signature
                })
            except razorpay.errors.SignatureVerificationError as e:
                logger.error("Signature verification failed: %s", e)
                return JsonResponse({'status': 'failure', 'message': 'Signature verification failed.'}, status=400)

            # User must be authenticated
            if not request.user.is_authenticated:
                return JsonResponse({'status': 'failure', 'message': 'User not authenticated.'}, status=403)

            category_id = request.POST.get("category_id")
            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return JsonResponse({'status': 'failure', 'message': 'Invalid category.'}, status=400)

            product = Product.objects.create(
                user=request.user,
                category=category,
                product_name=request.POST.get("product_name"),
                product_description=request.POST.get("description"),
                price=request.POST.get("base_price"),
                seller_email=request.user.email,
                seller_name=request.user.first_name,
                seller_phone=request.user.profile.phone,
                weight = request.POST.get('weight'),
                length = request.POST.get('length'),
                breadth = request.POST.get('breadth'),
                height = request.POST.get('height'),
                pincode = request.POST.get('pincode'),
                
            )

            # Save color variants
            colors = json.loads(request.POST.get("colors", "[]"))
            for color in colors:
                variant, _ = ColorVariant.objects.get_or_create(color_name=color["name"], price=color["price"])
                product.color_variants.add(variant)

            # Save size variants
            sizes = json.loads(request.POST.get("sizes", "[]"))
            for size in sizes:
                variant, _ = SizeVariant.objects.get_or_create(size_name=size["name"], price=size["price"])
                product.size_variants.add(variant)

            # Save main image
            if 'main_image' in request.FILES:
                ProductImage.objects.create(product=product, image=request.FILES['main_image'], is_main=True)

            # Save additional images
            for key in request.FILES:
                if key.startswith("additional_image_"):
                    ProductImage.objects.create(product=product, image=request.FILES[key], is_main=False)

            return JsonResponse({"status": "success"})

        except Exception as e:
            logger.exception("Error processing product upload:")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
        

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



