
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, HttpResponse , HttpResponseRedirect 
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import SavedCart, Order, OrderItem
import json
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
import json
from django.http import JsonResponse, HttpResponseBadRequest

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SavedCart
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from .models import SavedCart, SavedCartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import SavedCart
from .models import ProductView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SavedCart

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SavedCart

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SavedCart, SavedCartItem


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import SavedCart
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from accounts.models import SavedCart
from django.shortcuts import render
from .models import SavedCart, SavedCartItem
from django.shortcuts import render
from .models import SavedCart, ColorVariant, SizeVariant
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from .models import Product
from django.views.decorators.csrf import csrf_protect
from accounts.models import Review
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Order, OrderItem
import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
import json
import requests
from django.conf import settings
from django.http import JsonResponse
from .models import Category
from .models import SavedCart, Order, OrderItem

from django.core.mail import send_mail
from django.conf import settings

from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings
from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings

from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings
from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings


from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from accounts.models import Category
from accounts.models import Product, ColorVariant, SizeVariant
from django.http import JsonResponse
from .models import Category
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Product, ColorVariant, SizeVariant, ProductImage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product, Category, ProductImage, ColorVariant, SizeVariant

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, ProductImage, ColorVariant, SizeVariant, Category
import json
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, ProductImage, Category, ColorVariant, SizeVariant
# from .forms import ProductForm  # assuming you have a form for the product
# from .models import Product, Category, Color, Size
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Product, ProductImage, ColorVariant, SizeVariant, Category
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json

from .models import Product, ProductImage, Category, ColorVariant, SizeVariant


from django.shortcuts import render
from django.http import JsonResponse
from .models import PromoCode

import json
from django.http import JsonResponse
from .models import PromoCode


from django.http import JsonResponse
from .models import PromoCode, Order



from django.shortcuts import render
from .models import Product
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Product, ProductImage, ColorVariant, SizeVariant, Category
from appname.models import ProFile
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

# Create your views here.
# views.py
from django.http import JsonResponse
from .models import SavedCart
from django.contrib.auth.decorators import login_required
import json

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Only use if you're not handling CSRF properly in JS
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import SavedCart
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import SavedCart

import json
from django.http import JsonResponse
from .models import SavedCart

from accounts.models import SavedCart, Product, ColorVariant, SizeVariant
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from accounts.models import SavedCartItem


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def save_cart(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            items = data if isinstance(data, list) else [data]

            cart_obj, _ = SavedCart.objects.get_or_create(user=request.user)

            for item in items:
                product = Product.objects.get(uid=item["id"])

                # Validate size and color if required
                if product.size_variants.exists() and not item.get("selected_size"):
                    return JsonResponse({"status": "error", "message": "Size selection is required."}, status=400)
                if product.color_variants.exists() and not item.get("selected_color"):
                    return JsonResponse({"status": "error", "message": "Color selection is required."}, status=400)

                size_variant = SizeVariant.objects.filter(size_name=item.get("selected_size")).first() if item.get("selected_size") else None
                color_variant = ColorVariant.objects.filter(color_name=item.get("selected_color")).first() if item.get("selected_color") else None

                existing_item = SavedCartItem.objects.filter(
                    cart=cart_obj,
                    product=product,
                    size_variant=size_variant,
                    color_variant=color_variant
                ).first()

                if existing_item:
                    existing_item.quantity += item["quantity"]  # 🔥 Add instead of replace
                    existing_item.image = item.get("image", "")
                    existing_item.save()
                else:
                    SavedCartItem.objects.create(
                        cart=cart_obj,
                        product=product,
                        quantity=item["quantity"],
                        size_variant=size_variant,
                        color_variant=color_variant,
                        image=item.get("image", "")
                    )

            return JsonResponse({"status": "success", "message": "Cart saved!"})

        except Exception as e:
            print("Error saving cart:", e)
            return JsonResponse({"status": "error", "message": str(e)}, status=500)




@login_required
def load_cart(request):
    try:
        cart = SavedCart.objects.get(user=request.user)
        items = cart.items.all()
        cart_data = []

        for item in items:
            cart_data.append({
                "product_id": str(item.product.uid),
                "name": item.product.product_name,
                "image": item.image or (item.product.product_images.first().image.url if item.product.product_images.exists() else None),
                "quantity": item.quantity,
                "selected_size": item.size_variant.size_name if item.size_variant else None,
                "selected_color": item.color_variant.color_name if item.color_variant else None,
                "price": item.get_price(),
            })

        return JsonResponse({"cart": cart_data})

    except SavedCart.DoesNotExist:
        return JsonResponse({"cart": []})






def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Add filled and empty star ranges to each product
    for product in products:
        star = product.get_star_rating() if hasattr(product, 'get_star_rating') else 0
        product.star_rating_filled = range(star)
        product.star_rating_empty = range(5 - star)

    # Track the product view if the user is authenticated
    if request.user.is_authenticated:
        for product in products:
            ProductView.objects.get_or_create(user=request.user, product=product)

    cart_count = 0
    if request.user.is_authenticated:
        try:
            saved_cart = SavedCart.objects.get(user=request.user)
            cart_count = sum(item.quantity for item in saved_cart.items.all())
        except SavedCart.DoesNotExist:
            pass

    return render(request, 'home/home.html', {
        'products': products,
        'categories': categories,
        'cart_count': cart_count
    })




from decimal import Decimal

def cart_view(request):
    user = request.user
    cart, created = SavedCart.objects.get_or_create(user=user)
    cart_items = []
    total = Decimal('0.00')
    platform_fee_per_seller = Decimal('10.00')

    sellers = set()
    cart_quantity = sum(item.quantity for item in cart.items.all())

    for item in cart.items.select_related('product', 'color_variant', 'size_variant'):
        product = item.product
        sellers.add(product.user)

        color_name = item.color_variant.color_name if item.color_variant else None
        size_name = item.size_variant.size_name if item.size_variant else None

        item_data = {
            'id': item.id,
            'name': product.product_name,
            'image': item.image or (product.product_images.first().image.url if product.product_images.exists() else None),
            'price': item.get_price(),
            'quantity': item.quantity,
            'selected_size': size_name,
            'selected_color': color_name,
            'available_sizes': [s.size_name for s in product.size_variants.all()],
            'available_colors': [c.color_name for c in product.color_variants.all()],
            'item_total': item.get_total_price(),
        }

        cart_items.append(item_data)
        total += item.get_total_price()

    platform_fee = platform_fee_per_seller * len(sellers)
    grand_total = total + platform_fee

    context = {
        'cart_items': cart_items,
        'total': float(round(total, 2)),
        'platform_fee': float(round(platform_fee, 2)),
        'grand_total': float(round(grand_total, 2)),
        'cart_count': cart_quantity,
    }

    return render(request, 'cart.html', context)

@require_POST
@login_required
@csrf_exempt
@login_required
def remove_item(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        data = json.loads(request.body)
        item_id = data.get('item_id')
    except (json.JSONDecodeError, TypeError):
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    if not item_id or not str(item_id).isdigit():
        return JsonResponse({'error': 'Invalid item ID'}, status=400)

    item = get_object_or_404(SavedCartItem, id=int(item_id), cart__user=request.user)
    item.delete()

    cart_items = SavedCartItem.objects.filter(cart__user=request.user)
    cart_total = sum(i.get_total_price() for i in cart_items)
    cart_count = cart_items.aggregate(Sum("quantity"))["quantity__sum"] or 0

    return JsonResponse({
        'success': True,
        'cart_total': str(cart_total),
        'cart_count': cart_count,
    })

    

@require_POST
@login_required
@csrf_exempt  # optional if you're handling CSRF via header
def update_quantity(request):
    if request.method != "POST":
        return JsonResponse({"success": False, "error": "Invalid request"}, status=400)

    item_id = request.POST.get("item_id")
    quantity = request.POST.get("quantity")

    if not item_id or not quantity:
        return JsonResponse({"success": False, "error": "Missing data"}, status=400)

    try:
        quantity = int(quantity)
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        cart_item = SavedCartItem.objects.get(id=item_id, cart__user=request.user)
        cart_item.quantity = quantity
        cart_item.save()

        item_total = cart_item.get_total_price()
        cart_items = SavedCartItem.objects.filter(cart__user=request.user)
        cart_total = sum(item.get_total_price() for item in cart_items)
        cart_count = cart_items.aggregate(Sum("quantity"))["quantity__sum"] or 0

        return JsonResponse({
            "success": True,
            "updated_quantity": quantity,
            "item_total": str(item_total),
            "cart_total": str(cart_total),
            "cart_count": cart_count,
        })

    except SavedCartItem.DoesNotExist:
        return JsonResponse({"success": False, "error": "Item not found"}, status=404)
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)

@require_POST
@login_required
@csrf_exempt
@require_POST
@login_required
@csrf_exempt
def update_size(request):
    try:
        data = json.loads(request.body)
        item_id = data.get("item_id")
        new_size = data.get("size")

        item = SavedCartItem.objects.get(id=item_id)
        size_variant = SizeVariant.objects.filter(size_name=new_size).first()
        item.size_variant = size_variant
        item.save()

        updated_price = item.get_price()
        item_total = item.get_total_price()
        cart_items = SavedCartItem.objects.filter(cart__user=request.user)
        cart_count = cart_items.aggregate(Sum("quantity"))["quantity__sum"] or 0

        return JsonResponse({
            "success": True,
            "updated_price": updated_price,
            "quantity": item.quantity,
            "item_total": item_total,
            "cart_count": cart_count,
        })

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=400)

@require_POST
@login_required
@csrf_exempt
def update_color(request):
    try:
        data = json.loads(request.body)
        item_id = data.get("item_id")
        new_color = data.get("color")

        item = SavedCartItem.objects.get(id=item_id)
        color_variant = ColorVariant.objects.filter(color_name=new_color).first()
        item.color_variant = color_variant
        item.save()

        updated_price = item.get_price()
        item_total = item.get_total_price()
        cart_items = SavedCartItem.objects.filter(cart__user=request.user)
        cart_count = cart_items.aggregate(Sum("quantity"))["quantity__sum"] or 0

        return JsonResponse({
            "success": True,
            "updated_price": updated_price,
            "quantity": item.quantity,
            "item_total": item_total,
            "cart_count": cart_count,
        })

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=400)


def category_detail(request, slug=None):
    categories = Category.objects.all()

    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)

        # Add star rating properties
        for product in products:
            rating = int(product.get_star_rating())  # Ensure it's an int
            product.star_rating_filled = range(rating)
            product.star_rating_empty = range(5 - rating)

        context = {
            'category': category,
            'products': products,
            'categories': categories
        }
    else:
        context = {'categories': categories}

    return render(request, 'category_detail.html', context)



from django.shortcuts import render, get_object_or_404
from .models import Order  # Make sure Order is imported




def prodd(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        similar_products = Product.objects.filter(category=product.category).exclude(uid=product.uid)

        seller_profile = getattr(product.user, "profile", None)

        context = {
            'product': product,
            'similar_products': similar_products,
            'product_id': product.uid,
            'seller_name': product.user.username,  # or product.user.get_full_name() if you use first/last name
            'seller_phone': product.user.profile.phone
        }

        return render(request, "home/prodd.html", context)

    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")


@login_required
def submit_review(request, product_uid):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = get_object_or_404(Product, uid=product_uid)  # Changed to uid
            review.save()
            return JsonResponse({
                'message': 'Review submitted successfully',
                'review': {
                    'id': review.id,
                    'rating': review.rating,
                    'text': review.text,
                    'media': review.media.url if review.media else None,
                    'user': review.user.username,
                    'created_at': review.created_at.isoformat(),
                    'can_delete': True
                }
            })
        return JsonResponse({'message': 'Invalid form data'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

def get_reviews(request, product_uid):
    product = get_object_or_404(Product, uid=product_uid)
    reviews = Review.objects.filter(product=product).order_by('-created_at')

    return JsonResponse({
        'reviews': [{
            'id': review.id,
            'rating': review.rating,
            'text': review.text,
            'media': review.media.url if review.media else None,
            'user': review.user.username,
            'created_at': review.created_at.isoformat(),
            'can_delete': review.user == request.user or request.user.is_superuser
        } for review in reviews]
    })

@login_required
@csrf_protect  # Ensure CSRF is enabled for the delete view
def delete_review(request, review_id):
    if request.method == 'POST':
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return JsonResponse({"message": "Review deleted successfully"})
        except Review.DoesNotExist:
            return JsonResponse({"message": "Review not found"}, status=404)
    return JsonResponse({"message": "Invalid request method"}, status=400)



from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings
from collections import defaultdict
from django.core.mail import send_mail
from django.conf import settings
from collections import defaultdict
from django.core.mail import send_mail

# def send_confirmation_emails(suborder):
#     order = suborder.main_order  # Get the parent Order
#     user = order.user
#     profile = getattr(user, 'profile', None)

#     customer_email = user.email
#     customer_name = user.get_full_name() or user.username
#     customer_phone = getattr(profile, 'phone', '')
#     customer_address = getattr(profile, 'address', '')
#     merchant_email = settings.EMAIL_HOST_USER

#     # Fetch items related to this suborder
#     order_items = suborder.items.select_related('product')


#     # Customer Item Lines
#     item_lines = "\n".join([
#         f"- {item.product.product_name} (x{item.quantity}) @ Rs. {item.price}"
#         for item in order_items
#     ])
#     total = f"\nTotal Amount: Rs. {suborder.total_amount}\nSub-Order ID: {suborder.id}"

#     tracking_info = ""
#     if suborder.awb_code:
#         tracking_info += f"\nTracking AWB: {suborder.awb_code} ({suborder.selected_courier})"
#         tracking_info += f"\nTrack: https://shiprocket.co/tracking/{suborder.awb_code}"

#     # ---------------------
#     # Email to Customer
#     customer_subject = '🛒 Your Order Confirmation - TheDIYNight'
#     customer_message = f"""Hi {customer_name},

# Thanks for shopping with TheDIYNight! 🎉

# Items:
# {item_lines}
# {total}
# {tracking_info}

# We'll notify you when your order is out for delivery.

# Best,
# TheDIYNight Team
# """

#     send_mail(
#         subject=customer_subject,
#         message=customer_message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[customer_email],
#         fail_silently=False
#     )

#     # ---------------------
#     # Email to Admin
#     merchant_subject = '📦 New SubOrder Received'
#     merchant_message = f"""Hello Admin,

# New SubOrder has been placed.

# Customer: {customer_name}
# Email: {customer_email}
# Phone: {customer_phone}
# Address: {customer_address}

# Items:
# {item_lines}
# {total}

# Please coordinate for shipping.

# Regards,
# TheDIYNight System
# """

#     send_mail(
#         subject=merchant_subject,
#         message=merchant_message,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[merchant_email],
#         fail_silently=False
#     )

#     # ---------------------
#     # Email to Seller
#     seller = suborder.seller
#     seller_profile = getattr(seller, 'profile', None)
#     seller_email = seller.email
#     seller_name = getattr(seller_profile, 'name', seller.username)

#     if seller_email:
#         seller_subject = "🛍️ New Order for Your Product - TheDIYNight"
#         seller_message = f"""Hello {seller_name},

# You received a new order!

# Customer: {customer_name}
# Email: {customer_email}
# Phone: {customer_phone}
# Address: {customer_address}

# Items:
# {item_lines}
# Sub-Order ID: {suborder.id}

# Please prepare your items for dispatch.

# Best,
# TheDIYNight Team
# """
#         send_mail(
#             subject=seller_subject,
#             message=seller_message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[seller_email],
#             fail_silently=False
#         )




def success(request):
    return redirect(request, 'home/home.html')



@login_required
def order_summary_view(request):
    try:
        saved_cart = SavedCart.objects.get(user=request.user)
        cart_items = saved_cart.get_items()
    except SavedCart.DoesNotExist:
        cart_items = []

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
    })





@login_required
def cart_summary_api(request):
    try:
        saved_cart = SavedCart.objects.get(user=request.user)
        items = saved_cart.get_items()

        cart_data = []
        for item in items:
            cart_data.append({
                'product': item.product.product_name,
                'quantity': item.quantity,
                'price': item.get_price(),
                'image': item.image,
                'size': item.size_variant.size_name if item.size_variant else None,
                'color': item.color_variant.color_name if item.color_variant else None,
            })

        return JsonResponse({'cart': cart_data})
    
    except SavedCart.DoesNotExist:
        return JsonResponse({'cart': []}) 






@method_decorator(login_required, name='dispatch')
class CreateProductView(View):
    def post(self, request):
        try:
            # Get user profile data
            user = request.user
            profile = user.profile

            # Fetch data from request
            product_name = request.POST.get("productName")
            description = request.POST.get("description")
            base_price = request.POST.get("basePrice")
            category_id = request.POST.get("category")
            colors = request.POST.get("colors", "[]")
            sizes = request.POST.get("sizes", "[]")

            # Validate category_id
            if not category_id:
                return JsonResponse({"detail": "Missing category ID"}, status=400)

            try:
                category = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                return JsonResponse({"detail": "Invalid category ID"}, status=400)

            # Validate and convert base_price to integer
            try:
                base_price = int(base_price)
            except ValueError:
                return JsonResponse({"detail": "Base price should be a valid number"}, status=400)

            # Parse colors and sizes as JSON
            try:
                colors = json.loads(colors)
            except json.JSONDecodeError:
                return JsonResponse({"detail": "Invalid JSON for colors"}, status=400)

            try:
                sizes = json.loads(sizes)
            except json.JSONDecodeError:
                return JsonResponse({"detail": "Invalid JSON for sizes"}, status=400)

            # Create the product
            product = Product.objects.create(
                user=user,
                product_name=product_name,
                product_description=description,
                price=base_price,
                category=category,
                seller_email=profile.email,
                seller_name=profile.name,
                seller_phone=profile.phone,
            )

            # Handle main image
            if 'mainImage' in request.FILES:
                ProductImage.objects.create(
                    product=product,
                    image=request.FILES['mainImage']
                )

            # Handle additional images (optional, max 3 images)
            additional_images = request.FILES.getlist('additionalImages')
            for i, f in enumerate(additional_images[:3]):  # Limit to 3 additional images
                ProductImage.objects.create(
                    product=product,
                    image=f
                )

            # Handle color variants
            for color in colors:
                color_variant = ColorVariant.objects.create(
                    color_name=color['name'],
                    price=color['price']
                )
                product.color_variants.add(color_variant)

            # Handle size variants
            for size in sizes:
                size_variant = SizeVariant.objects.create(
                    size_name=size['name'],
                    price=size['price']
                )
                product.size_variants.add(size_variant)

            # Seller info
            seller_info = {
                "name": profile.name,
                "email": profile.email,
                "phone": profile.phone
            }

            return JsonResponse({
                "message": "Product created successfully.",
                "seller_info": seller_info
            }, status=201)

        except Exception as e:
            # Log full request and error for debugging
            print("POST:", request.POST)
            print("FILES:", request.FILES)
            print("ERROR:", e)

            return JsonResponse({"detail": str(e)}, status=400)


def get_categories(request):
    categories = Category.objects.all().values('id', 'category_name')
    return JsonResponse(list(categories), safe=False)



def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(
        Q(product_name__icontains=query) |
        Q(product_description__icontains=query)
    ).distinct() if query else Product.objects.all()
    
    return render(request, 'home/home.html', {'products': products})

# utils.py or views.py (helper)
from django.http import JsonResponse
from django.shortcuts import render
import json
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import SavedCart, Order, OrderItem
# from .utils import calculate_shipping_rate, choose_best_courier, send_confirmation_emails
import requests
import math
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import SavedCartItem

import requests
import logging

logger = logging.getLogger(__name__)

import requests
from django.conf import settings
import json







def choose_best_courier(couriers):
    if not isinstance(couriers, list) or len(couriers) == 0:
        print("[DEBUG] No courier companies available")
        return None

    best_score = float('inf')
    best_courier = None

    for courier in couriers:
        rate = courier.get("rate")
        etd = courier.get("etd", "")
        try:
            estimated_days = int(etd.split("-")[0].strip())
        except Exception:
            estimated_days = 10  # fallback if parsing fails

        if rate is not None:
            score = rate + (estimated_days * 10)
            print(f"[DEBUG] Courier: {courier['courier_name']}, Rate: {rate}, Days: {estimated_days}, Score: {score}")

            if score < best_score:
                best_score = score
                best_courier = courier

    return best_courier







import logging

logger = logging.getLogger(__name__)  # Add this at the top of your views.py or utils.py
import requests
from decimal import Decimal
import requests
from decimal import Decimal

def calculate_shipping_rate(product, profile):
    token = get_shiprocket_token()
    if not token:
        logger.error("[ERROR] Failed to get Shiprocket token.")
        return {'success': False, 'message': 'Token generation failed'}

    headers = {
        'Authorization': f'Bearer {token}'
    }

    try:
        pickup_pincode = str(product.pincode or '133001')
        delivery_pincode = str(profile.coustmer_pincode or '134203')

        weight = float(product.weight or 0.5)
        length = float(product.length or 10)
        breadth = float(product.breadth or 10)
        height = float(product.height or 10)

        # Safety check
        if weight <= 0: weight = 0.5

        params = {
            'pickup_postcode': pickup_pincode,
            'delivery_postcode': delivery_pincode,
            'weight': weight,
            'length': length,
            'breadth': breadth,
            'height': height,
            'cod': 0
        }

        logger.debug(f"[DEBUG] Requesting Shiprocket rates with: {params}")

        response = requests.get(
            'https://apiv2.shiprocket.in/v1/external/courier/serviceability/',
            headers=headers,
            params=params,
            timeout=10,
        )
        response.raise_for_status()
        data = response.json()

        if data.get('status') == 200:
            couriers = data['data'].get('available_courier_companies', [])
            if not couriers:
                logger.warning(f"[WARN] No courier companies available for {product.product_name}")
                return {'success': False, 'message': 'No couriers available', 'params': params}

            # Choose cheapest courier
            cheapest = min(
                (c for c in couriers if c.get('rate') is not None),
                key=lambda c: c['rate'],
                default=None
            )

            if not cheapest:
                return {'success': False, 'message': 'No courier with valid rate', 'params': params}

            logger.info(
                f"[INFO] Cheapest courier for {product.product_name}: "
                f"{cheapest['courier_name']} at ₹{cheapest['rate']}"
            )

            return {
                'success': True,
                'carrier_name': cheapest['courier_name'],
                'freight_charge': Decimal(str(cheapest['rate'])),
                'estimated_delivery_days': cheapest.get('estimated_delivery_days'),
                'rate': Decimal(str(cheapest['rate'])),
                'raw_response': cheapest
            }

        else:
            logger.warning(f"[WARN] Shiprocket returned unexpected response: {data}")
            return {'success': False, 'message': 'Invalid response from Shiprocket', 'details': data}

    except requests.RequestException as e:
        logger.exception(f"[EXCEPTION] Shiprocket API request failed: {e}")
        return {'success': False, 'message': 'Shiprocket API request exception', 'error': str(e)}

    except Exception as e:
        logger.exception(f"[EXCEPTION] Unexpected error: {e}")
        return {'success': False, 'message': 'Unexpected error', 'error': str(e)}


import logging
import requests
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import SavedCartItem

logger = logging.getLogger(__name__)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.conf import settings
import requests
import logging
from decimal import Decimal
from .models import SavedCartItem

logger = logging.getLogger(__name__)

class GetShippingCostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        address = request.data.get("address", {})
        delivery_pincode = address.get("pincode")

        if not delivery_pincode:
            logger.warning("[WARN] Delivery pincode missing from request.")
            return JsonResponse({"error": "Delivery pincode required."}, status=400)

        cart_items = SavedCartItem.objects.filter(cart__user=user)
        if not cart_items.exists():
            logger.info(f"[INFO] No items in cart for user: {user.email}")
            return JsonResponse({"shipping": [], "message": "Cart is empty."})

        # --- Authenticate with Shiprocket
        try:
            auth_payload = {
                "email": settings.SHIPROCKET_EMAIL,
                "password": settings.SHIPROCKET_PASSWORD,
            }
            logger.debug(f"[DEBUG] Authenticating with Shiprocket for user {user.email}")
            auth_response = requests.post(
                "https://sr-auth.shiprocket.in/v1/external/auth/login",
                json=auth_payload,
                timeout=10,
            )
            auth_response.raise_for_status()
            token = auth_response.json().get("token")
            if not token:
                raise ValueError("Shiprocket token not found in auth response.")
        except Exception as e:
            logger.exception(f"[ERROR] Shiprocket authentication failed: {e}")
            return JsonResponse({"error": "Authentication with Shiprocket failed"}, status=500)

        headers = {"Authorization": f"Bearer {token}"}
        shipping_data = []

        for item in cart_items:
            product = item.product
            pickup_pincode = product.pincode or "133001"  # Default fallback for pickup

            try:
                # --- Calculate weight
                actual_weight = float(product.weight or 0.5) * item.quantity
                length = float(product.length or 10)
                breadth = float(product.breadth or 10)
                height = float(product.height or 10)

                volumetric_weight = ((length * breadth * height) / 5000) * item.quantity
                chargeable_weight = round(max(actual_weight, volumetric_weight), 2)

                logger.debug(
                    f"[DEBUG] {product.product_name}: Actual={actual_weight}kg, "
                    f"Volumetric={volumetric_weight}kg, Final={chargeable_weight}kg"
                )

                rate_payload = {
                    "pickup_postcode": str(pickup_pincode),
                    "delivery_postcode": str(delivery_pincode),
                    "cod": 0,
                    "weight": chargeable_weight,
                    "length": length,
                    "breadth": breadth,
                    "height": height,
                }

                rate_response = requests.get(
                    "https://apiv2.shiprocket.in/v1/external/courier/serviceability/",
                    params=rate_payload,
                    headers=headers,
                    timeout=10,
                )
                rate_response.raise_for_status()
                rate_data = rate_response.json()
                couriers = rate_data.get("data", {}).get("available_courier_companies", [])

                if not couriers:
                    logger.warning(f"[WARN] No couriers found for {product.product_name}")
                    continue

                # --- Choose the cheapest valid courier with a non-null rate
                valid_couriers = [c for c in couriers if c.get("rate") is not None]
                cheapest = min(valid_couriers, key=lambda x: x["rate"], default=None)

                if cheapest:
                    shipping_data.append({
                        "product": product.product_name,
                        "pickup_pincode": pickup_pincode,
                        "delivery_pincode": delivery_pincode,
                        "chargeable_weight": chargeable_weight,
                        "freight_charge": round(cheapest["rate"], 2),
                        "courier_name": cheapest["courier_name"],
                        "estimated_delivery_days": cheapest.get("estimated_delivery_days"),
                    })
                    logger.info(
                        f"[INFO] {product.product_name}: Courier - {cheapest['courier_name']}, ₹{cheapest['rate']}"
                    )
                else:
                    logger.warning(f"[WARN] No valid courier with rate found for {product.product_name}")

            except Exception as e:
                logger.exception(f"[ERROR] Failed shipping cost calc for {product.product_name}: {e}")

        return JsonResponse({"shipping": shipping_data}, status=200)


import json
from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
from .models import SavedCart, Order, OrderItem
# from .utils import calculate_shipping_rate, choose_best_courier, send_confirmation_emails


import json
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import json
import logging
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import SavedCart, Order, OrderItem
# from .utils import calculate_shipping_rate, choose_best_courier, send_confirmation_emails
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import json
import logging


logger = logging.getLogger(__name__)

import requests
import logging

logger = logging.getLogger(__name__)


def assign_awb_view(request):
    shipment_id = request.GET.get("shipment_id")

    if not shipment_id:
        return JsonResponse({"error": "Missing shipment_id"}, status=400)

    try:
        suborder = SubOrder.objects.get(shipment_id=shipment_id)
    except SubOrder.DoesNotExist:
        return JsonResponse({"error": "SubOrder not found"}, status=404)

    token = get_shiprocket_token()

    try:
        awb_code, courier_name = assign_awb(suborder.shipment_id, token)
        suborder.awb_code = awb_code
        suborder.selected_courier = courier_name
        suborder.save()
        return JsonResponse({"success": True, "awb_code": awb_code})
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


import requests
from datetime import datetime
import logging


logger = logging.getLogger(__name__)

import requests
import logging

logger = logging.getLogger(__name__)

import requests
import logging
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)
import requests
import logging
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)
import requests
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def create_shiprocket_order(order, token):
    logger.debug(f"[ENTRY] Creating Shiprocket order for Order ID: {order.id}")

    user_profile = order.user.profile
    logger.debug(f"[DEBUG] Fetched user profile: {user_profile}")

    billing_address_parts = [
        user_profile.house_number,
        user_profile.street,
        user_profile.locality,
        user_profile.address,
    ]
    billing_address = ", ".join(part for part in billing_address_parts if part)

    required_fields = {
        "name": user_profile.name,
        "phone": user_profile.phone,
        "pincode": user_profile.coustmer_pincode,
        "city": user_profile.city,
        "state": user_profile.state,
        "email": user_profile.email,
        "address": billing_address,
    }
    missing_fields = [field for field, value in required_fields.items() if not value]
    if missing_fields:
        logger.error(f"[ERROR] Missing user profile fields: {missing_fields}")
        raise Exception(f"Missing required profile fields for Shiprocket order: {', '.join(missing_fields)}")

    first_item = order.items.first()
    if not first_item:
        logger.error("[ERROR] Order has no items.")
        raise Exception("Order has no items.")

    seller = getattr(first_item.product, 'user', None)
    if not seller:
        logger.error("[ERROR] Product has no associated seller user.")
        raise Exception("Product missing seller user.")

    try:
        seller_profile = seller.profile
        logger.debug(f"[DEBUG] Seller profile retrieved: {seller_profile}")
    except ObjectDoesNotExist:
        logger.error("[ERROR] Seller profile is missing.")
        raise Exception("Seller profile is missing.")

    seller_address_parts = [
        seller_profile.house_number,
        seller_profile.street,
        seller_profile.locality,
        seller_profile.address,
    ]
    seller_full_address = ", ".join(part for part in seller_address_parts if part)

    required_seller_fields = {
        "phone": seller_profile.phone,
        "city": seller_profile.city,
        "state": seller_profile.state,
        "address": seller_full_address,
    }
    missing_seller_fields = [f for f, val in required_seller_fields.items() if not val]
    if missing_seller_fields:
        logger.error(f"[ERROR] Missing seller profile fields: {missing_seller_fields}")
        raise Exception(f"Missing seller fields for Shiprocket pickup: {', '.join(missing_seller_fields)}")

    pickup_name = seller_profile.custom_pickup_name
    if not pickup_name:
        logger.debug(f"[DEBUG] Creating new pickup location for seller: {seller}")
        pickup_name = create_shiprocket_pickup_location(seller, token)
        seller_profile.custom_pickup_name = pickup_name
        seller_profile.save()
        logger.debug(f"[DEBUG] New pickup location saved: {pickup_name}")

    items = order.items.all()
    default_dim = 10
    default_weight = 0.5
    length = max([getattr(item.product, 'length', default_dim) or default_dim for item in items], default=default_dim)
    breadth = max([getattr(item.product, 'breadth', default_dim) or default_dim for item in items], default=default_dim)
    height = max([getattr(item.product, 'height', default_dim) or default_dim for item in items], default=default_dim)
    weight = sum([(getattr(item.product, 'weight', default_weight) or default_weight) * item.quantity for item in items]) or default_weight
    logger.debug(f"[DEBUG] Shipping metrics — L:{length}, B:{breadth}, H:{height}, W:{weight}")

    payload = {
        "order_id": str(order.id),
        "order_date": order.created_at.strftime("%Y-%m-%d"),
        "pickup_location": pickup_name,
        "channel_id": "",
        "billing_customer_name": user_profile.name,
        "billing_last_name": user_profile.last_name or "",
        "billing_address": billing_address,
        "billing_city": user_profile.city,
        "billing_pincode": str(user_profile.coustmer_pincode),
        "billing_state": user_profile.state,
        "billing_country": "India",
        "billing_email": user_profile.email,
        "billing_phone": user_profile.phone,
        "shipping_is_billing": True,
        "order_items": [],
        "payment_method": "Prepaid" if order.payment_method.lower() != "cod" else "COD",
        "shipping_charges": float(order.shipping_cost),
        "sub_total": float(order.total_amount - order.shipping_cost),
        "length": length,
        "breadth": breadth,
        "height": height,
        "weight": weight,
    }

    for item in items:
        product = item.product
        payload["order_items"].append({
            "name": product.product_name,
            "sku": str(product.uid),
            "units": item.quantity,
            "selling_price": float(item.price),
        })

    logger.debug(f"[DEBUG] Final payload for Shiprocket:\n{json.dumps(payload, indent=2)}")

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            "https://apiv2.shiprocket.in/v1/external/orders/create/adhoc",
            json=payload,
            headers=headers
        )
        response.raise_for_status()
    except requests.RequestException as e:
        logger.exception(f"[ERROR] Request to Shiprocket failed: {str(e)}")
        raise Exception(f"Shiprocket request failed: {str(e)}")

    logger.debug(f"[DEBUG] Shiprocket response status: {response.status_code}")
    logger.debug(f"[DEBUG] Shiprocket response body: {response.text}")

    try:
        data = response.json()
    except Exception as e:
        logger.error(f"[ERROR] Failed to parse Shiprocket response JSON: {e}")
        raise Exception("Invalid Shiprocket response format")

    if data.get("status") != 200 and not data.get("shipment_id"):
        logger.error(f"[ERROR] Shiprocket rejected the order: {data}")
        raise Exception(f"Shiprocket order creation failed: {data}")

    # --- Save initial response
    order.shiprocket_order_id = data.get("order_id")
    order.shipment_id = data.get("shipment_id")
    order.awb_code = data.get("awb_code")
    order.selected_courier = data.get("courier_name")
    order.save()

    # ✅ Manually assign AWB if not received
    if not order.awb_code and order.shipment_id:
        logger.debug(f"[DEBUG] AWB not returned. Trying to assign AWB manually for shipment ID {order.shipment_id}")
        try:
            awb_code, courier_name = assign_awb(order.shipment_id, token)
            order.awb_code = awb_code
            order.selected_courier = courier_name
            order.save()
            logger.info(f"[SUCCESS] AWB manually assigned: {awb_code} via {courier_name}")
        except Exception as e:
            logger.error(f"[ERROR] Manual AWB assignment failed: {e}")

    logger.info(f"[SUCCESS] Shiprocket order created for Order {order.id}")
    return order.shipment_id, order.shiprocket_order_id


from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
import json
import logging

logger = logging.getLogger(__name__)

from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def process_cart_items(cart_items, profile):
    total_shipping = Decimal('0')
    shipping_breakdown = []
    all_couriers = []

    for item in cart_items:
        product = item.product
        try:
            logger.debug(f"[DEBUG] Calculating shipping for product: {product.product_name}")
            result = calculate_shipping_rate(product, profile)

            logger.debug(f"[DEBUG] Shipping rate result: {result}")
            best = result if isinstance(result, dict) and 'freight_charge' in result else None
        except Exception as e:
            logger.exception(f"[EXCEPTION] Error calculating shipping rate for {product.product_name}: {e}")
            best = None

        # Fallback if no shipping rate or API failure
        freight = Decimal(str(best.get('freight_charge'))) if best and best.get('freight_charge') else Decimal('120')
        carrier = best.get('carrier_name', 'Default') if best else 'Default'
        days = best.get('estimated_delivery_days') if best else None

        if not best:
            logger.warning(f"[WARN] Default freight used for {product.product_name}")

        total_shipping += freight

        shipping_breakdown.append({
            'product': product.product_name,
            'cost': float(freight),
            'provider': carrier,
            'estimated_delivery_days': days,
        })

        if days is not None:
            all_couriers.append({
                'carrier_name': carrier,
                'freight_charge': float(freight),
                'estimated_delivery_days': int(days),
            })

    return total_shipping, shipping_breakdown, all_couriers


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from decimal import Decimal
import json
import logging

from .models import SavedCart, Order, OrderItem


from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse
from .models import SavedCart
from .models import SubOrder
import json
import logging

logger = logging.getLogger(__name__)

SHIPROCKET_EMAIL = "work.kavleen@gmail.com"
SHIPROCKET_PASSWORD = "x@9yRW1Qw4TF#p$P"
from django.shortcuts import render
from django.http import JsonResponse
from .models import SavedCart
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from decimal import Decimal
import json
import logging

logger = logging.getLogger(__name__)

import json
from decimal import Decimal
from django.shortcuts import render
from django.http import JsonResponse

import logging

from decimal import Decimal
import json
from django.shortcuts import render
from django.http import JsonResponse
import logging
from decimal import Decimal
import json
from django.shortcuts import render
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)
import json
import logging
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .models import SavedCart
# from .utils import calculate_shipping_rate, get_shiprocket_token, split_and_create_orders
from accounts.tasks import send_confirmation_emails_task  # ✅ Import Celery task

logger = logging.getLogger(__name__)

def checkout(request):
    user = request.user
    profile = getattr(user, 'profile', None)
    logger.debug(f"[DEBUG] Checkout view accessed. Method: {request.method}, User: {user.username}")

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            logger.debug(f"[DEBUG] Received POST data: {data}")
        except Exception as e:
            logger.error(f"[ERROR] Failed to parse JSON body: {e}")
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

        # Validate required fields
        required_fields = ['name', 'email', 'address', 'paymentMethod']
        missing_fields = [f for f in required_fields if not data.get(f)]
        if missing_fields:
            logger.debug(f"[DEBUG] Missing fields: {missing_fields}")
            return JsonResponse({'success': False, 'error': f"Missing fields: {', '.join(missing_fields)}"}, status=400)

        # Validate profile completeness
        if not profile or not all([profile.address, profile.city, profile.state, profile.coustmer_pincode]):
            logger.warning("[WARN] Incomplete shipping address in profile.")
            return JsonResponse({'success': False, 'error': 'Incomplete shipping address in profile.'}, status=400)

        # Get saved cart
        try:
            saved_cart = SavedCart.objects.get(user=user)
            cart_items = saved_cart.get_items()
            logger.debug(f"[DEBUG] Cart retrieved with {len(cart_items)} items.")
        except SavedCart.DoesNotExist:
            logger.warning("[WARN] No saved cart found for user.")
            return JsonResponse({'success': False, 'error': 'No saved cart found for user'}, status=400)

        # Get Shiprocket token if prepaid
        token = None
        if data['paymentMethod'].lower() == 'prepaid':
            try:
                token = get_shiprocket_token()
                logger.debug("[DEBUG] Shiprocket token obtained.")
            except Exception as e:
                logger.error(f"[ERROR] Shiprocket token fetch failed: {e}")
                return JsonResponse({'success': False, 'error': 'Failed to authenticate with Shiprocket'}, status=500)

        # Parse total shipping from frontend
        try:
            total_shipping = Decimal(data.get('totalShipping', '0.00'))
            logger.debug(f"[DEBUG] Shipping override received: ₹{total_shipping}")
        except (ValueError, TypeError):
            logger.error("[ERROR] Invalid totalShipping value received.")
            return JsonResponse({'success': False, 'error': 'Invalid shipping amount received.'}, status=400)

        # Create Order(s)
        try:
            logger.debug("[DEBUG] Calling split_and_create_orders...")
            orders = split_and_create_orders(
                user=user,
                cart_items=cart_items,
                data=data,
                profile=profile,
                shipping_breakdown=None,
                shiprocket_token=token,
                base_order=None
            )
            logger.debug(f"[DEBUG] Orders created: {[o.id for o in orders]}")
        except Exception as e:
            logger.exception(f"[ERROR] Order creation failed: {e}")
            return JsonResponse({'success': False, 'error': 'Order creation failed'}, status=500)

        # Clear cart
        saved_cart.items.all().delete()
        logger.debug("[DEBUG] Cart cleared after order creation.")

        # ✅ Asynchronously send confirmation emails via Celery
        for order in orders:
            for suborder in order.suborders.all():
                send_confirmation_emails_task.delay(suborder.id)
                logger.debug(f"[DEBUG] Enqueued confirmation email task for SubOrder {suborder.id}")

        return JsonResponse({'success': True, 'orderIds': [order.id for order in orders]})

    # GET request: Render checkout summary
    try:
        saved_cart = SavedCart.objects.get(user=user)
        cart_items = saved_cart.get_items()
        logger.debug(f"[DEBUG] Retrieved {len(cart_items)} cart items for GET summary.")
    except SavedCart.DoesNotExist:
        cart_items = []
        logger.debug("[DEBUG] No saved cart for GET summary.")

    shipping_breakdown = []
    shipping_total = Decimal('0.00')
    subtotal = Decimal('0.00')
    sellers_set = set()

    for item in cart_items:
        product = item.product
        quantity = item.quantity
        sellers_set.add(product.user)

        item_total_price = Decimal(item.get_total_price())
        subtotal += item_total_price
        logger.debug(f"[DEBUG] Item: {product.product_name}, Qty: {quantity}, Item Total: ₹{item_total_price}")

        shipping_response = calculate_shipping_rate(product, profile)

        if shipping_response.get('success'):
            freight_charge = shipping_response['freight_charge']
            shipping_cost = freight_charge * quantity
            shipping_total += shipping_cost
            logger.debug(f"[DEBUG] Shipping for {product.product_name}: ₹{shipping_cost} via {shipping_response['carrier_name']}")

            shipping_breakdown.append({
                "product": product.product_name,
                "provider": shipping_response['carrier_name'],
                "cost": float(round(shipping_cost, 2)),
                "estimated_delivery_days": shipping_response.get("estimated_delivery_days"),
            })
        else:
            logger.warning(f"[WARN] Shipping unavailable for {product.product_name}: {shipping_response.get('message')}")
            shipping_breakdown.append({
                "product": product.product_name,
                "provider": "N/A",
                "cost": 0,
                "estimated_delivery_days": None,
            })

    platform_fee = Decimal('10.00') * len(sellers_set)
    grand_total = subtotal + shipping_total + platform_fee

    logger.debug(f"[DEBUG] Subtotal: ₹{subtotal}, Shipping: ₹{shipping_total}, Platform Fee: ₹{platform_fee}, Grand Total: ₹{grand_total}")

    return render(request, 'checkout.html', {
        "cart_items": cart_items,
        "shipping_breakdown": shipping_breakdown,
        "shipping": float(round(shipping_total, 2)),
        "subtotal": float(round(subtotal, 2)),
        "platform_fee": float(round(platform_fee, 2)),
        "total": float(round(grand_total, 2)),
        "user_name": profile.name if profile else user.get_full_name(),
        "user_email": user.email,
        "user_phone": profile.phone if profile else '',
        "user_address": profile.address if profile else '',
    })

# @csrf_exempt


# # logger = logging.getLogger(__name__)
# @login_required
# def checkout(request):
#     user = request.user
#     profile = getattr(user, 'profile', None)
#     logger.debug(f"[DEBUG] Checkout request received. Method: {request.method}, User: {user.username}")

#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             logger.debug(f"[DEBUG] POST data: {data}")
#         except Exception as e:
#             logger.error(f"[ERROR] Failed to parse JSON: {e}")
#             return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

#         # Basic form validation
#         required_fields = ['name', 'email', 'address', 'paymentMethod']
#         missing_fields = [f for f in required_fields if not data.get(f)]
#         if missing_fields:
#             return JsonResponse({'success': False, 'error': f"Missing fields: {', '.join(missing_fields)}"}, status=400)

#         # Check profile fields
#         if not profile or not all([profile.address, profile.city, profile.state, profile.coustmer_pincode]):
#             return JsonResponse({'success': False, 'error': 'Incomplete shipping address in profile.'}, status=400)

#         # Retrieve cart
#         try:
#             saved_cart = SavedCart.objects.get(user=user)
#             cart_items = saved_cart.get_items()
#         except SavedCart.DoesNotExist:
#             return JsonResponse({'success': False, 'error': 'No saved cart found for user'}, status=400)

#         # Get Shiprocket token if needed
#         token = None
#         if data['paymentMethod'].lower() == 'prepaid':
#             try:
#                 token = get_shiprocket_token()
#                 logger.debug("[DEBUG] Shiprocket token obtained successfully.")
#             except Exception as e:
#                 logger.error(f"[ERROR] Shiprocket authentication failed: {e}")
#                 return JsonResponse({'success': False, 'error': 'Failed to authenticate with Shiprocket'}, status=500)

#         # Parse shipping from frontend
#         try:
#             total_shipping = Decimal(data.get('totalShipping', '0.00'))
#             logger.debug(f"[DEBUG] Shipping override received: {total_shipping}")
#         except (ValueError, TypeError):
#             logger.error("[ERROR] Invalid totalShipping value received from frontend.")
#             return JsonResponse({'success': False, 'error': 'Invalid shipping amount received.'}, status=400)

#         # Create orders
#         try:
#             orders = split_and_create_orders(user, cart_items, data, profile, token, total_shipping_override=total_shipping)
#         except Exception as e:
#             logger.exception(f"[ERROR] Order creation failed: {e}")
#             return JsonResponse({'success': False, 'error': 'Order creation failed'}, status=500)

#         # Clear cart
#         saved_cart.items.all().delete()

#         # Send confirmation email(s)
#         for order in orders:
#             try:
#                 send_confirmation_emails(order)
#             except Exception as e:
#                 logger.warning(f"[WARN] Failed to send confirmation email for Order {order.id}: {e}")

#         return JsonResponse({'success': True, 'orderIds': [order.id for order in orders]})

#     # GET method: render checkout summary
#     try:
#         saved_cart = SavedCart.objects.get(user=user)
#         cart_items = saved_cart.get_items()
#     except SavedCart.DoesNotExist:
#         cart_items = []

#     shipping_breakdown = []
#     shipping_total = Decimal('0.00')
#     subtotal = Decimal('0.00')

#     for item in cart_items:
#         product = item.product
#         quantity = item.quantity

#         item_total_price = Decimal(item.get_total_price())  # ✅ includes quantity
#         subtotal += item_total_price

#         # Shipping calculation
#         shipping_response = calculate_shipping_rate(product, profile)

#         if shipping_response.get('success'):
#             freight_charge = shipping_response['freight_charge']
#             shipping_cost = freight_charge * quantity  # ✅ multiplied by quantity
#             shipping_total += shipping_cost

#             shipping_breakdown.append({
#                 "product": product.product_name,
#                 "provider": shipping_response['carrier_name'],
#                 "cost": float(round(shipping_cost, 2)),
#                 "estimated_delivery_days": shipping_response.get("estimated_delivery_days"),
#             })
#         else:
#             logger.warning(f"[WARN] Shipping unavailable for {product.product_name}: {shipping_response.get('message')}")
#             shipping_breakdown.append({
#                 "product": product.product_name,
#                 "provider": "N/A",
#                 "cost": 0,
#                 "estimated_delivery_days": None,
#             })

#     total = subtotal + shipping_total

#     return render(request, 'checkout.html', {
#         "cart_items": cart_items,
#         "shipping_breakdown": shipping_breakdown,
#         "shipping": float(round(shipping_total, 2)),
#         "subtotal": float(round(subtotal, 2)),
#         "total": float(round(total, 2)),
#         "user_name": profile.name if profile else user.get_full_name(),
#         "user_email": user.email,
#         "user_phone": profile.phone if profile else '',
#         "user_address": profile.address if profile else '',
#     })

from django.contrib import messages
from django.views.decorators.http import require_POST


# views.py

from django.core.mail import send_mail
from django.conf import settings

def send_order_status_email(to_email, status, order):
    subject = ''
    message = ''
    
    if status == "Shipped":
        subject = "Your order has been shipped!"
        message = f"Dear {order.name},\n\nYour order #{order.id} has been marked as shipped. It will be delivered soon.\n\nThank you for shopping with us!"
    
    elif status == "Cancelled":
        subject = "Your order has been cancelled"
        message = f"Dear {order.name},\n\nYour order #{order.id} has been cancelled. If payment was made, a refund will be processed.\n\nWe're sorry for the inconvenience."

    elif status == "Refunded":
        subject = "Refund Initiated"
        message = f"Dear {order.name},\n\nA refund for your order #{order.id} has been initiated. Please check your payment method for the refund status.\n\nThank you."

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [to_email],
        fail_silently=True,
    )

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Order



from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseBadRequest
from django.contrib import messages
from .models import Order, SubOrder




from decimal import Decimal, ROUND_HALF_UP
import razorpay

from decimal import Decimal, ROUND_HALF_UP
import razorpay

import razorpay

import requests
from requests.auth import HTTPBasicAuth

import requests
from requests.auth import HTTPBasicAuth
from decimal import Decimal, ROUND_HALF_UP

RAZORPAY_KEY_ID = "rzp_test_4t8nCdN7uI0xEP"
RAZORPAY_KEY_SECRET = "6PWff6o8IE8dtouN2DMfBquc"


import requests
from decimal import Decimal

from django.conf import settings
from decimal import Decimal
import logging

logger = logging.getLogger(__name__)

def create_shiprocket_order_for_suborder(suborder, token):
    import requests
    from django.core.exceptions import ObjectDoesNotExist
    from django.utils.timezone import now

    logger.debug(f"[ENTRY] Creating Shiprocket order for SubOrder ID: {suborder.id}")

    # --- Buyer Info ---
    buyer_profile = suborder.main_order.user.profile
    billing_address_parts = [
        buyer_profile.house_number,
        buyer_profile.street,
        buyer_profile.locality,
        buyer_profile.address,
    ]
    billing_address = ", ".join(part for part in billing_address_parts if part)

    required_fields = {
        "name": buyer_profile.name,
        "phone": buyer_profile.phone,
        "pincode": buyer_profile.coustmer_pincode,
        "city": buyer_profile.city,
        "state": buyer_profile.state,
        "email": buyer_profile.email,
        "address": billing_address,
    }
    missing_fields = [field for field, value in required_fields.items() if not value]
    if missing_fields:
        logger.error(f"[ERROR] Missing buyer profile fields: {missing_fields}")
        raise Exception(f"Missing required profile fields: {', '.join(missing_fields)}")

    # --- Seller Info ---
    try:
        seller_profile = suborder.seller.profile
    except ObjectDoesNotExist:
        logger.error(f"[ERROR] Seller profile missing for seller ID {suborder.seller.id}")
        raise Exception("Seller profile not found.")

    seller_address_parts = [
        seller_profile.house_number,
        seller_profile.street,
        seller_profile.locality,
        seller_profile.address,
    ]
    seller_full_address = ", ".join(part for part in seller_address_parts if part)

    required_seller_fields = {
        "phone": seller_profile.phone,
        "city": seller_profile.city,
        "state": seller_profile.state,
        "address": seller_full_address,
    }
    missing_seller_fields = [f for f, val in required_seller_fields.items() if not val]
    if missing_seller_fields:
        logger.error(f"[ERROR] Missing seller profile fields: {missing_seller_fields}")
        raise Exception(f"Missing seller fields: {', '.join(missing_seller_fields)}")

    # --- Pickup Location ---
    pickup_name = seller_profile.custom_pickup_name
    if not pickup_name:
        logger.debug(f"[DEBUG] Creating new pickup location for seller {suborder.seller}")
        pickup_name = create_shiprocket_pickup_location(suborder.seller, token)
        seller_profile.custom_pickup_name = pickup_name
        seller_profile.save()
        logger.debug(f"[DEBUG] Saved new pickup location: {pickup_name}")

    # --- Order Items ---
    items = []
    default_dim = 10
    default_weight = 0.5
    length = breadth = height = default_dim
    weight = 0

    for item in suborder.items.all():
        product = item.product
        if not product:
            continue
        items.append({
            "name": product.product_name,
            "sku": str(product.uid),
            "units": item.quantity,
            "selling_price": float(item.price),
        })
        length = max(length, product.length or default_dim)
        breadth = max(breadth, product.breadth or default_dim)
        height = max(height, product.height or default_dim)
        weight += (product.weight or default_weight) * item.quantity

    if not items:
        logger.error(f"[ERROR] SubOrder {suborder.id} has no valid items.")
        raise Exception("No valid items in suborder.")

    # --- Build Payload ---
    payload = {
        "order_id": f"SO-{suborder.id}",
        "order_date": suborder.created_at.strftime("%Y-%m-%d"),
        "pickup_location": pickup_name,
        "channel_id": "",
        "comment": "Order from multi-vendor platform",
        "billing_customer_name": buyer_profile.name,
        "billing_last_name": buyer_profile.last_name or "",
        "billing_address": billing_address,
        "billing_city": buyer_profile.city,
        "billing_pincode": str(buyer_profile.coustmer_pincode),
        "billing_state": buyer_profile.state,
        "billing_country": "India",
        "billing_email": buyer_profile.email,
        "billing_phone": buyer_profile.phone,
        "shipping_is_billing": True,
        "order_items": items,
        "payment_method": "Prepaid" if suborder.main_order.payment_method.lower() != "cod" else "COD",
        "sub_total": float(suborder.total_amount),
        "length": length,
        "breadth": breadth,
        "height": height,
        "weight": weight or default_weight,
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    logger.debug(f"[Shiprocket] Payload for SubOrder {suborder.id}: {payload}")

    # --- API Request ---
    try:
        response = requests.post(
            "https://apiv2.shiprocket.in/v1/external/orders/create/adhoc",
            json=payload,
            headers=headers
        )
        response.raise_for_status()
    except requests.RequestException as e:
        logger.exception(f"[ERROR] Request failed: {e}")
        raise Exception("Failed to connect to Shiprocket.")

    try:
        data = response.json()
    except Exception as e:
        logger.error(f"[ERROR] Invalid JSON response: {e}")
        raise Exception("Invalid Shiprocket response format")

    logger.debug(f"[Shiprocket] Response for SubOrder {suborder.id}: {data}")

    # --- Final Check ---
    if not data.get("shipment_id"):
        logger.error(f"[ERROR] Shiprocket error: {data}")
        raise Exception(f"Shiprocket rejected the order: {data}")

    # ✅ Save data to suborder
    suborder.shiprocket_order_id = data.get("order_id")
    suborder.shipment_id = data.get("shipment_id")
    suborder.awb_code = data.get("awb_code")
    suborder.selected_courier = data.get("courier_name")
    suborder.save()

    logger.info(f"[SUCCESS] Shiprocket order created for SubOrder {suborder.id}")
    return suborder.shipment_id, suborder.shiprocket_order_id

from collections import defaultdict
from decimal import Decimal
import logging

# logger = logging.getLogger(__name__)
import logging
from collections import defaultdict
from decimal import Decimal
from .models import Order, SubOrder, OrderItem
# from accounts.views import create_shiprocket_order_for_suborder, assign_awb

logger = logging.getLogger(__name__)
from decimal import Decimal
from collections import defaultdict

def split_and_create_orders(user, cart_items, data=None, profile=None, shipping_breakdown=None, shiprocket_token=None, base_order=None):
    PLATFORM_FEE = Decimal("10.00")  # Flat fee per seller/suborder

    items_by_seller = defaultdict(list)
    shipping_map = {}

    # Build product UID → shipping info mapping
    if shipping_breakdown:
        for item in shipping_breakdown:
            pid = item.get("product_id")
            if pid:
                shipping_map[str(pid)] = item

    # Group cart items by seller
    for item in cart_items:
        items_by_seller[item.product.user].append(item)

    # Compute subtotal and shipping cost for the whole order
    subtotal = sum(Decimal(item.get_price()) for item in cart_items)
    total_shipping = sum(
        Decimal(str(shipping_map.get(str(item.product.uid), {}).get("cost", "120")))
        for item in cart_items
    )
    total_platform_fee = PLATFORM_FEE * len(items_by_seller)
    total_amount = subtotal + total_shipping + total_platform_fee

    # Use existing order if provided (e.g. Razorpay created earlier)
    if base_order:
        main_order = base_order
        main_order.total_amount = total_amount
        main_order.shipping_cost = total_shipping
        main_order.save()
    else:
        if not data or not profile:
            raise ValueError("Missing data/profile for new order creation.")

        main_order = Order.objects.create(
            user=user,
            name=data.get('name') or profile.name or user.get_full_name(),
            email=data.get('email') or profile.email or user.email,
            phone=data.get('phone') or profile.phone or '',
            address=', '.join(filter(None, [
                profile.house_number,
                profile.street,
                profile.locality,
                profile.city,
                profile.state,
                str(profile.coustmer_pincode) if profile.coustmer_pincode else ''
            ])),
            payment_method=data.get('paymentMethod'),
            transaction_id=data.get('transactionId', ''),
            total_amount=total_amount,
            shipping_cost=total_shipping,
        )

    suborders_created = []

    for seller, seller_items in items_by_seller.items():
        seller_profile = getattr(seller, 'profile', None)
        if not seller_profile:
            logger.warning(f"[WARNING] Seller {seller.username} has no profile. Skipping.")
            continue

        # ✅ Calculate per seller pricing
        sub_total = sum(Decimal(item.get_price()) for item in seller_items)
        sub_shipping = sum(
            Decimal(str(shipping_map.get(str(item.product.uid), {}).get("cost", "120")))
            for item in seller_items
        )
        shiprocket_deduction = sub_shipping
        platform_fee = PLATFORM_FEE
        total = sub_total + sub_shipping + platform_fee
        seller_payout = sub_total  # Only product price — not including shipping or fees

        # ✅ Create SubOrder with fee breakdown
        suborder = SubOrder.objects.create(
            main_order=main_order,
            seller=seller,
            shipping_cost=sub_shipping,
            total_amount=total,
            shiprocket_deduction=shiprocket_deduction,
            platform_fee=platform_fee,
            seller_payout=seller_payout,
        )

        for item in seller_items:
            OrderItem.objects.create(
                order=main_order,
                suborder=suborder,
                product=item.product,
                quantity=item.quantity,
                price=Decimal(item.get_price()),
                seller_name=seller_profile.name or seller.username,
                seller_email=seller.email,
                seller_phone=seller_profile.phone or "",
            )

        # ✅ Shiprocket integration
        if shiprocket_token:
            try:
                logger.debug(f"[DEBUG] Creating Shiprocket order for SubOrder ID {suborder.id}")
                shipment_id, sr_order_id = create_shiprocket_order_for_suborder(suborder, shiprocket_token)
                awb_code, final_courier = assign_awb(shipment_id, shiprocket_token)

                suborder.shiprocket_order_id = sr_order_id
                suborder.shipment_id = shipment_id
                suborder.awb_code = awb_code
                suborder.selected_courier = final_courier
                suborder.save()

                # Set top-level Order tracking info
                if not main_order.awb_code:
                    main_order.shiprocket_order_id = sr_order_id
                    main_order.shipment_id = shipment_id
                    main_order.awb_code = awb_code
                    main_order.selected_courier = final_courier
                    main_order.delivery_status_snapshot = "Pending"
                    main_order.save()

            except Exception as e:
                logger.error(f"[ERROR] Shiprocket integration failed for SubOrder {suborder.id}: {e}")

        suborders_created.append(suborder)

    return [main_order] + suborders_created



def create_shiprocket_pickup_location(seller_user, token):
    import requests

    profile = getattr(seller_user, 'profile', None)

    if not profile:
        raise Exception(f"Seller profile not found for user {seller_user.username}")

    # Build full address (Shiprocket requires House No / Flat No / Road No)
    full_address = ', '.join(filter(None, [
        profile.house_number,
        profile.street,
        profile.locality
    ]))

    # Validate required fields
    missing_fields = []
    if not profile.name:
        missing_fields.append("name")
    if not full_address:
        missing_fields.append("full_address (house number, street, locality)")
    if not profile.city:
        missing_fields.append("city")
    if not profile.state:
        missing_fields.append("state")
    if not profile.phone:
        missing_fields.append("phone")
    if not profile.coustmer_pincode:
        missing_fields.append("coustmer_pincode")

    if missing_fields:
        raise Exception(
            f"Missing required fields in seller profile for Shiprocket pickup: {', '.join(missing_fields)}"
        )

    pickup_location_name = profile.custom_pickup_name or f"{profile.name}_pickup"

    payload = {
        "pickup_location": pickup_location_name,
        "name": profile.name,
        "email": seller_user.email,
        "phone": profile.phone,
        "address": full_address,  # ✅ FIXED HERE
        "address_2": "",
        "city": profile.city,
        "state": profile.state,
        "country": "India",
        "pin_code": str(profile.coustmer_pincode),
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://apiv2.shiprocket.in/v1/external/settings/company/addpickup",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        profile.shiprocket_pickup_name = pickup_location_name
        profile.save()
        return pickup_location_name
    else:
        raise Exception(f"Failed to create pickup location: {response.status_code} - {response.text}")




def track_order_view(request):
    order = None
    tracking_info = {}
    order_number = request.GET.get('order_number')

    if order_number:
        try:
            order = Order.objects.get(id=order_number)

            if order.awb_code:
                token = get_shiprocket_token()  # your function
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.get(
                    f"https://apiv2.shiprocket.in/v1/external/courier/track/awb/{order.awb_code}",
                    headers=headers
                )
                tracking_info = response.json()

        except Order.DoesNotExist:
            order = None
            tracking_info = {}

    return render(request, "home/track.html", {
        "order": order,
        "tracking_info": tracking_info,
        "order_number": order_number,
    })

from django.utils.timezone import make_aware


# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import logging

from .models import SubOrder
import requests
from .models import SubOrder
from django.utils.timezone import now


logger = logging.getLogger(__name__)
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

WEBHOOK_TOKEN = "theDIYwebhook2025SECRET"  # You can also move this to settings.py



@csrf_exempt
@csrf_exempt
def shiprocket_webhook(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Method not allowed"}, status=405)

    received_token = request.headers.get('X-SR-Webhook-Token')
    if received_token != WEBHOOK_TOKEN:
        return JsonResponse({"error": "Invalid webhook token"}, status=403)

    try:
        data = json.loads(request.body)
        shipment_id = data.get("shipment_id")
        status = data.get("current_status", "").lower()

        if not shipment_id:
            return JsonResponse({"error": "Missing shipment_id"}, status=400)

        suborder = SubOrder.objects.filter(shipment_id=shipment_id).first()
        if not suborder:
            return JsonResponse({"error": "SubOrder not found"}, status=404)

        # 🔄 Optional: Call your internal status sync
        sync_shiprocket_status(suborder)

        # ✅ Auto-refund logic for return
        if suborder.is_return_requested and not suborder.is_refunded:
            if status in ["return delivered", "rto delivered"]:
                suborder.is_return_picked = True
                suborder.status = "Return Picked"
                suborder.save()

                # 🔁 Trigger Razorpay refund
                refund_after_pickup(suborder)

        return JsonResponse({"success": True, "suborder_id": suborder.id})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
import requests
from django.http import JsonResponse
from .models import SubOrder

SHIPROCKET_EMAIL="work.kavleen@gmail.com"
SHIPROCKET_PASSWORD="x@9yRW1Qw4TF#p$P"
RAZORPAY_KEY_ID = "rzp_test_4t8nCdN7uI0xEP"
RAZORPAY_KEY_SECRET = "6PWff6o8IE8dtouN2DMfBquc"

def get_shiprocket_token():
    """Get authentication token from Shiprocket"""
    url = "https://apiv2.shiprocket.in/v1/external/auth/login"
    payload = {
        "email": SHIPROCKET_EMAIL,
        "password": SHIPROCKET_PASSWORD
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data.get("token")
        else:
            print(f"[ERROR] Shiprocket auth failed: {response.status_code} | {response.text}")
            return None
    except Exception as e:
        print(f"[ERROR] Shiprocket auth exception: {e}")
        return None

def get_payment_details(payment_id):
    """Get payment details from Razorpay"""
    url = f"https://api.razorpay.com/v1/payments/{payment_id}"
    auth = HTTPBasicAuth(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[ERROR] Razorpay payment fetch failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"[ERROR] Razorpay payment fetch exception: {e}")
        return None



@require_POST
def update_order_status(request, suborder_id):
    """Update order status"""
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    print("[DEBUG] update_order_status triggered")
    print("[DEBUG] POST data:", request.POST)

    suborder = get_object_or_404(SubOrder, id=suborder_id)
    action = request.POST.get("action")

    if not action:
        messages.error(request, "No action provided.")
        return HttpResponseBadRequest("Missing action")

    if action == "ready_to_ship":
        success = notify_shiprocket_order_ready(suborder)
        if success:
            suborder.status = "Ready to Ship"
            suborder.save()
            messages.success(request, f"SubOrder {suborder.id} marked as Ready to Ship.")
        else:
            messages.error(request, f"Failed to notify Shiprocket for SubOrder {suborder.id}")

    elif action == "cancel":
        success = cancel_shiprocket_order(suborder)
        if success:
            suborder.status = "Cancelled"
            suborder.save()
            messages.success(request, f"SubOrder {suborder.id} cancelled.")
        else:
            messages.error(request, f"Failed to cancel SubOrder {suborder.id} on Shiprocket.")

        # Refund logic — only refund if *all* suborders are cancelled
        order = suborder.main_order
        all_cancelled = all(sub.status == "Cancelled" for sub in order.suborders.all())

        if all_cancelled and order.is_paid and order.razorpay_payment_id:
            print(f"[DEBUG] Attempting refund for Order ID: {order.id} with Payment ID: {order.razorpay_payment_id}")
            refund_success = trigger_refund(order)
            if refund_success:
                messages.success(request, f"Refund triggered for Order {order.id}")
            else:
                messages.error(request, f"Refund failed for Order {order.id}")

    else:
        messages.error(request, f"Invalid action: {action}")
        return redirect("sellerdashboard")

    return redirect("sellerdashboard")

def notify_shiprocket_order_ready(suborder):
    """Notify Shiprocket that order is ready to ship"""
    token = get_shiprocket_token()
    if not token:
        return False

    shipment_id = suborder.shipment_id

    print(f"[DEBUG] Attempting to mark shipment_id {shipment_id} as Ready to Ship")

    url = "https://apiv2.shiprocket.in/v1/external/orders/ready-to-ship"
    payload = {
        "shipment_id": shipment_id,
        "status": "ready_to_ship"
    }
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        print("[DEBUG] Payload to Shiprocket:", payload)
        response = requests.post(url, json=payload, headers=headers)
        print("[Shiprocket] Ready-to-ship response status:", response.status_code)
        print("[Shiprocket] Ready-to-ship response body:", response.text)
        return response.status_code == 200
    except Exception as e:
        print(f"[ERROR] Exception during ready-to-ship request: {e}")
        return False

def cancel_shiprocket_order(suborder):
    """Cancel order on Shiprocket"""
    token = get_shiprocket_token()
    if not token:
        return False

    shipment_id = suborder.shipment_id

    print(f"[DEBUG] Attempting to cancel Shiprocket shipment_id: {shipment_id}")

    url = f"https://apiv2.shiprocket.in/v1/external/orders/cancel/{shipment_id}"
    headers = {
        "Authorization": f"Bearer {token}",
    }

    try:
        response = requests.get(url, headers=headers)
        print("[Shiprocket] Cancel response status:", response.status_code)
        print("[Shiprocket] Cancel response body:", response.text)
        return response.status_code == 200
    except Exception as e:
        print(f"[ERROR] Exception during Shiprocket cancel request: {e}")
        return False

def trigger_refund(order):
    """Trigger refund through Razorpay"""
    try:
        if not order.razorpay_payment_id:
            print(f"[ERROR] No Razorpay Payment ID found for Order ID: {order.id}")
            return False

        # Prepare amount in paisa
        raw_amount = order.total_amount
        print(f"[DEBUG] Raw total_amount: {raw_amount} (type: {type(raw_amount)})")

        amount_in_paisa = int((Decimal(str(raw_amount)) * 100).quantize(Decimal('1'), rounding=ROUND_HALF_UP))
        print(f"[DEBUG] Final amount_in_paisa: {amount_in_paisa} (type: {type(amount_in_paisa)})")

        # Fetch payment details from Razorpay to verify status
        payment_data = get_payment_details(order.razorpay_payment_id)
        if not payment_data:
            print("[ERROR] Could not fetch payment details from Razorpay.")
            return False

        if payment_data.get("status") != "captured":
            print(f"[ERROR] Payment not captured. Status: {payment_data.get('status')}")
            return False

        captured_amount = payment_data.get("amount", 0)
        if amount_in_paisa > captured_amount:
            print(f"[ERROR] Refund amount {amount_in_paisa} > paid amount {captured_amount}")
            return False

        # Razorpay refund endpoint
        url = f"https://api.razorpay.com/v1/payments/{order.razorpay_payment_id}/refund"
        payload = {
            "amount": amount_in_paisa
        }
        auth = HTTPBasicAuth(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET)

        print(f"[Razorpay] Initiating raw refund request: {payload}")
        response = requests.post(url, json=payload, auth=auth)

        print(f"[Razorpay] HTTP {response.status_code} | Response: {response.text}")

        if response.status_code == 200:
            refund_data = response.json()
            order.refund_status = "Refunded"
            order.save()
            print(f"[Razorpay] Refund successful: {refund_data}")
            return True
        else:
            error_desc = response.json().get("error", {}).get("description", "Unknown error")
            print(f"[Razorpay] Refund failed: {error_desc}")
            return False

    except Exception as e:
        print(f"[Razorpay] Refund exception for Order ID {order.id}: {str(e)}")
        return False

@require_POST
def print_manifest(request):
    """Print manifest for shipment"""
    shipment_id = request.POST.get("shipment_id")
    if not shipment_id:
        return JsonResponse({"error": "Missing shipment_id"}, status=400)

    token = get_shiprocket_token()
    if not token:
        return JsonResponse({"error": "Unable to authenticate with Shiprocket"}, status=500)

    url = "https://apiv2.shiprocket.in/v1/external/manifests/print"

    payload = {
        "shipment_id": shipment_id
    }
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            pdf_url = response.json().get("manifest_url")
            return JsonResponse({"manifest_url": pdf_url})
        else:
            return JsonResponse({"error": response.json()}, status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_POST
def generate_label(request):
    """Generate shipping label"""
    shipment_id = request.POST.get("shipment_id")
    if not shipment_id:
        return JsonResponse({"error": "Missing shipment_id"}, status=400)

    token = get_shiprocket_token()
    if not token:
        return JsonResponse({"error": "Unable to authenticate with Shiprocket"}, status=500)

    url = "https://apiv2.shiprocket.in/v1/external/courier/generate/label"

    payload = {
        "shipment_id": shipment_id
    }
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            pdf_url = response.json().get("label_url")
            return JsonResponse({"label_url": pdf_url})
        else:
            return JsonResponse({"error": response.json()}, status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

@require_POST
def print_invoice(request):
    """Print invoice for shipment"""
    shipment_id = request.POST.get("shipment_id")
    if not shipment_id:
        return JsonResponse({"error": "Missing shipment_id"}, status=400)

    token = get_shiprocket_token()
    if not token:
        return JsonResponse({"error": "Unable to authenticate with Shiprocket"}, status=500)

    url = "https://apiv2.shiprocket.in/v1/external/orders/print/invoice"

    payload = {
        "shipment_id": shipment_id
    }
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            pdf_url = response.json().get("invoice_url")
            return JsonResponse({"invoice_url": pdf_url})
        else:
            return JsonResponse({"error": response.json()}, status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def generate_pickup(request):
    """Generate pickup for shipment"""
    shipment_id = request.GET.get("shipment_id")

    if not shipment_id:
        return JsonResponse({"error": "Missing shipment_id"}, status=400)

    try:
        suborder = SubOrder.objects.get(shipment_id=shipment_id)
    except SubOrder.DoesNotExist:
        return JsonResponse({"error": "SubOrder not found"}, status=404)

    token = get_shiprocket_token()
    if not token:
        return JsonResponse({"error": "Unable to authenticate with Shiprocket"}, status=500)

    url = "https://apiv2.shiprocket.in/v1/external/courier/generate/pickup"
    payload = {"shipment_id": shipment_id}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            return JsonResponse({"success": True, "pickup_generated": True})
        else:
            return JsonResponse({"error": response.text}, status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def sync_shiprocket_status(suborder):
    """Sync delivery status from Shiprocket"""
    print(f"[SYNC] Syncing delivery status for SubOrder {suborder.id}")
    if not suborder.shipment_id:
        print(f"[SYNC] No shipment_id for SubOrder {suborder.id}")
        return

    token = get_shiprocket_token()
    if not token:
        return

    url = f"https://apiv2.shiprocket.in/v1/external/courier/track/shipment/{suborder.shipment_id}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if "tracking_data" not in data:
            print(f"[SYNC] No tracking data found: {data}")
            return

        status = data["tracking_data"].get("shipment_status")
        current_status = data["tracking_data"].get("current_status")
        status_date = data["tracking_data"].get("current_status_time")

        # Map Shiprocket status to internal status
        status_map = {
            "DELIVERED": "Delivered",
            "IN TRANSIT": "Shipped",
            "PICKUP SCHEDULED": "Ready to Ship",
        }

        mapped_status = status_map.get(status, None)
        if mapped_status and suborder.status != mapped_status:
            suborder.status = mapped_status
            if mapped_status == "Delivered":
                suborder.is_delivered = True
                suborder.delivery_date = now()
            suborder.delivery_status_snapshot = f"{current_status} @ {status_date}"
            suborder.save()
            print(f"[SYNC] SubOrder {suborder.id} updated to {mapped_status}")
        else:
            print(f"[SYNC] SubOrder {suborder.id} is already {suborder.status}")
    except Exception as e:
        print(f"[SYNC] Exception: {e}")

def update_order_delivery_status(order):
    """Update order delivery status using AWB code"""
    if not order.awb_code:
        return

    token = get_shiprocket_token()
    if not token:
        return

    headers = {'Authorization': f'Bearer {token}'}
    url = f"https://apiv2.shiprocket.in/v1/external/courier/track/awb/{order.awb_code}"

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            tracking_data = data.get("tracking_data", {})

            if tracking_data.get("shipment_status") == "Delivered":
                delivered_event = next(
                    (e for e in tracking_data.get("track_status", []) if e["status"] == "Delivered"),
                    None
                )

                if delivered_event:
                    delivered_datetime = make_aware(datetime.strptime(delivered_event["date"], "%Y-%m-%d %H:%M:%S"))

                    order.is_delivered = True
                    order.delivery_date = delivered_datetime
                    order.delivery_status_snapshot = delivered_event
                    order.status = "Delivered"
                    order.save()
    except Exception as e:
        print(f"[ERROR] Delivery status update exception: {e}")

def get_tracking_status(awb_code):
    """Get tracking status using AWB code"""
    token = get_shiprocket_token()
    if not token:
        return {"error": "Unable to authenticate with Shiprocket."}

    url = f"https://apiv2.shiprocket.in/v1/external/courier/track/awb/{awb_code}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        return {"error": "Tracking info not available."}
    except Exception as e:
        return {"error": f"Tracking error: {str(e)}"}

def assign_awb(shipment_id, token):
    """Assign AWB code to shipment"""
    url = "https://apiv2.shiprocket.in/v1/external/courier/assign/awb"
    payload = {"shipment_id": shipment_id}
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            awb_code = data.get("awb_code")
            courier_name = data.get("courier_name")
            return awb_code, courier_name
        else:
            raise Exception(f"Failed to assign AWB: {response.status_code} | {response.text}")
    except Exception as e:
        raise Exception(f"AWB assignment exception: {str(e)}")


from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from datetime import timedelta
from accounts.models import SubOrder  # adjust import path


# from .emails import notify_seller_of_return  # or wherever you placed the function

@login_required
def request_return(request, suborder_id):
    suborder = get_object_or_404(SubOrder, id=suborder_id, main_order__user=request.user)

    if suborder.status != "Delivered":
        messages.error(request, "This order is not delivered yet.")
        return redirect("order_detail", suborder.main_order.id)

    if suborder.return_requested_at:
        messages.warning(request, "Return already requested.")
        return redirect("order_detail", suborder.main_order.id)

    delivered_at = suborder.main_order.delivery_date
    if not delivered_at or timezone.now() > delivered_at + timedelta(hours=24):
        messages.error(request, "Return window (24 hrs) has expired.")
        return redirect("order_detail", suborder.main_order.id)

    # ✅ Save return request
    suborder.is_return_requested = True
    suborder.return_requested_at = timezone.now()
    suborder.save()

    # ✅ Send email to seller
    notify_seller_of_return(suborder)

    messages.success(request, "Return request submitted. Seller will be notified.")
    return redirect("order_detail", suborder.main_order.id)


# from .utils import get_shiprocket_token  # You already use this
import requests
from django.conf import settings

def approve_return_and_create_reverse_pickup(request, suborder_id):
    suborder = get_object_or_404(SubOrder, id=suborder_id)
    
    # Ensure return is requested
    if not suborder.is_return_requested or suborder.is_return_approved:
        return JsonResponse({"error": "Invalid return request"}, status=400)

    # Build API payload
    token = get_shiprocket_token()
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    user_profile = suborder.main_order.user.profile  # buyer
    seller_profile = suborder.seller.profile  # seller
    
    order_item = suborder.items.first()
    product = order_item.product

    payload = {
        "order_id": f"RET-{suborder.id}",
        "order_date": str(timezone.now().date()),
        "pickup_location": seller_profile.custom_pickup_name or seller_profile.name,
        "channel_id": "",
        "comment": "Return requested by user",
        "billing_customer_name": user_profile.name,
        "billing_last_name": user_profile.last_name or "",
        "billing_address": user_profile.address,
        "billing_city": user_profile.city,
        "billing_pincode": user_profile.coustmer_pincode,
        "billing_state": user_profile.state,
        "billing_country": "India",
        "billing_email": user_profile.email,
        "billing_phone": user_profile.phone,
        "shipping_is_billing": True,
        "order_items": [
            {
                "name": product.product_name,
                "sku": product.slug,
                "units": order_item.quantity,
                "selling_price": float(order_item.price),
            }
        ],
        "payment_method": "Prepaid",
        "sub_total": float(suborder.total_amount),
        "length": product.length,
        "breadth": product.breadth,
        "height": product.height,
        "weight": product.weight,
        "assign_awb": 1
    }

    response = requests.post(
        "https://apiv2.shiprocket.in/v1/external/orders/create/return",
        headers=headers,
        json=payload
    )

    data = response.json()
    if response.status_code == 200 and "shipment_id" in data:
        suborder.is_return_approved = True
        suborder.shiprocket_order_id = data["order_id"]
        suborder.shipment_id = data["shipment_id"]
        suborder.awb_code = data.get("awb_code")
        suborder.status = "Return Created"
        suborder.save()
        return JsonResponse({"success": True, "awb": data.get("awb_code")})
    else:
        return JsonResponse({"error": data.get("message", "API Error")}, status=400)



import razorpay
from django.conf import settings

def refund_after_pickup(suborder):
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment_id = suborder.main_order.razorpay_payment_id
    amount = int(suborder.total_amount * 100)  # in paisa

    try:
        refund = client.payment.refund(payment_id, {"amount": amount})
        suborder.is_refunded = True
        suborder.status = "Refunded"
        suborder.save()
        return refund
    except Exception as e:
        print("Refund error:", str(e))
        return None


from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def notify_seller_of_return(suborder):
    seller = suborder.seller
    order = suborder.main_order
    profile = seller.profile

    subject = f"🔁 Return Requested - Order #{order.id}"
    recipient = seller.email
    context = {
        "seller_name": profile.name or seller.username,
        "order_id": order.id,
        "suborder_id": suborder.id,
        "product_list": suborder.items.all(),
        "customer_name": order.name,
        "customer_email": order.email,
    }

    message = render_to_string("emails/return_notification.txt", context)
    html_message = render_to_string("emails/return_notification.html", context)

    send_mail(
        subject,
        message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[recipient],
        html_message=html_message,
        fail_silently=False,
    )
