
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


# def cartt(request):

#     return render(request, 'cart.html')

@login_required
def cart_view(request):
    user = request.user
    cart, created = SavedCart.objects.get_or_create(user=user)
    cart_items = []
    total = 0
    cart_quantity = sum(item.quantity for item in cart.items.all())

    for item in cart.items.select_related('product', 'color_variant', 'size_variant'):
        product = item.product
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
        }

        cart_items.append(item_data)
        total += item.get_price()

    context = {
        'cart_items': cart_items,
        'total': total,
        'cart_count': cart_quantity,  
    }

    return render(request, 'cart.html', context)



@require_POST
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

    return JsonResponse({'success': True})
    

@require_POST
@login_required
def update_quantity(request):
    item_id = request.POST.get('item_id')
    quantity = request.POST.get('quantity')

    # Validate item_id and quantity
    if not item_id or not item_id.isdigit():
        return JsonResponse({'error': 'Invalid item ID'}, status=400)
    
    if not quantity or not quantity.isdigit() or int(quantity) <= 0:
        return JsonResponse({'error': 'Invalid quantity'}, status=400)

    # Proceed safely with type casting
    item = get_object_or_404(SavedCartItem, id=int(item_id), cart__user=request.user)
    item.quantity = int(quantity)
    item.save()

    return JsonResponse({'success': True, 'new_quantity': item.quantity})

@require_POST
@login_required
@csrf_exempt
def update_size(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("item_id")
        new_size = data.get("size")

        try:
            item = SavedCartItem.objects.get(id=item_id)
            size_variant = SizeVariant.objects.filter(size_name=new_size).first()
            item.size_variant = size_variant
            item.save()

            updated_price = item.get_price()

            return JsonResponse({"success": True, "updated_price": updated_price})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

    
@require_POST
@login_required
@csrf_exempt
def update_color(request):
    if request.method == "POST":
        data = json.loads(request.body)
        item_id = data.get("item_id")
        new_color = data.get("color")

        try:
            item = SavedCartItem.objects.get(id=item_id)
            color_variant = ColorVariant.objects.filter(color_name=new_color).first()
            item.color_variant = color_variant
            item.save()

            updated_price = item.get_price()

            return JsonResponse({"success": True, "updated_price": updated_price})
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



def tr(request):
    return render(request, "tr.html")

def prodd(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        similar_products = Product.objects.filter(category=product.category).exclude(uid=product.uid)

        context = {
            'product': product,
            'similar_products': similar_products,
            'product_id': product.uid,
            'seller_name': product.seller_name,
            'seller_phone': product.seller_phone,  # ← add this line
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





def send_confirmation_emails(order):
    customer_email = order.email
    merchant_email = settings.EMAIL_HOST_USER

    order_items = order.items.all()

    # ---------------------
    # Build customer item lines
    item_lines = "\n".join([
        f"- {item.product.product_name} (x{item.quantity}) @ Rs. {item.price}"
        for item in order_items
    ])
    total = f"\nTotal Amount: Rs. {order.total_amount}\nOrder ID: {order.id}"

    # ---------------------
    # Email to Customer
    customer_subject = '🛒 Your Order Confirmation - TheDIYNight'
    customer_message = f"""Hi {order.name},

Thank you for your order from TheDIYNight! 🎉

Here’s what you ordered:
{item_lines}
{total}

We’ll notify you when your order is shipped.

Best,
TheDIYNight Team
"""

    send_mail(
        subject=customer_subject,
        message=customer_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[customer_email],
        fail_silently=False
    )

    # ---------------------
    # Group items by seller from Product model
    seller_items = defaultdict(list)
    for item in order_items:
        product = item.product
        seller_key = (product.seller_name or "Unknown Seller", product.seller_email)
        seller_items[seller_key].append(item)

    # ---------------------
    # Email to Merchant (admin)
    seller_lines = ""
    for (seller_name, seller_email), items in seller_items.items():
        seller_lines += f"\n\nSeller: {seller_name or 'N/A'} | Email: {seller_email}\n"
        for item in items:
            seller_lines += f"- {item.product.product_name} (x{item.quantity}) @ Rs. {item.price}\n"

    merchant_subject = '📦 New Order Received'
    merchant_message = f"""Hello,

You have received a new order.

Customer: {order.name}
Email: {order.email}
Phone: {order.phone}
Address: {order.address}

Order Details by Seller:{seller_lines}
{total}

Login to your admin panel to view full details.
"""

    send_mail(
        subject=merchant_subject,
        message=merchant_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[merchant_email],
        fail_silently=False
    )

    # ---------------------
    # Email to each Seller
    for (seller_name, seller_email), items in seller_items.items():
        if not seller_email:
            continue

        seller_item_lines = "\n".join([
            f"- {item.product.product_name} (x{item.quantity}) @ Rs. {item.price}"
            for item in items
        ])
        seller_subject = "🛍️ New Order for Your Product - TheDIYNight"
        seller_message = f"""Hello {seller_name or "Seller"},

One of your products has been ordered!

Customer: {order.name}
Email: {order.email}
Phone: {order.phone}
Address: {order.address}

Ordered Items:
{seller_item_lines}
Order ID: {order.id}

Please prepare your item(s) for shipment.

Best,
TheDIYNight Team
"""

        send_mail(
            subject=seller_subject,
            message=seller_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[seller_email],
            fail_silently=False
        )

# views.py


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





@method_decorator(csrf_exempt, name='dispatch')
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

def get_shiprocket_token():
    url = "https://apiv2.shiprocket.in/v1/external/auth/login"
    payload = {
        "email": settings.SHIPROCKET_EMAIL,
        "password": settings.SHIPROCKET_PASSWORD
    }
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

    if response.status_code == 200:
        return response.json().get("token")
    else:
        raise Exception(f"Shiprocket Auth Error: {response.text}")

def calculate_shipping_rate(product, user_profile):
    try:
        token = get_shiprocket_token()

        actual_weight = product.weight
        volumetric_weight = (product.length * product.breadth * product.height) / 5000
        chargeable_weight = max(actual_weight, volumetric_weight)

        url = "https://apiv2.shiprocket.in/v1/external/courier/serviceability/"
        payload = {
            "pickup_postcode": str(product.pincode),
            "delivery_postcode": str(user_profile.coustmer_pincode),
            "cod": 0,
            "weight": chargeable_weight
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(url, params=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return {"success": True, "rates": data.get("data", [])}
        else:
            return {"success": False, "message": "Shiprocket API error", "details": response.json()}

    except Exception as e:
        return {"success": False, "message": str(e)}
    
def choose_best_courier(couriers):
    # Filter out any courier entries missing these fields just in case
    filtered = [
        c for c in couriers 
        if 'freight_charge' in c and 'estimated_delivery_days' in c
    ]

    # Sort couriers first by price (freight_charge), then by delivery days (estimated_delivery_days)
    sorted_couriers = sorted(
        filtered, 
        key=lambda x: (float(x['freight_charge']), int(x['estimated_delivery_days']))
    )

    # Return the best courier option (lowest price + fastest)
    if sorted_couriers:
        return sorted_couriers[0]
    else:
        return None

# utils.py or views.py (helper)
import requests
from django.conf import settings
import json

def get_shiprocket_token():
    import requests
    from django.conf import settings

    url = "https://apiv2.shiprocket.in/v1/external/auth/login"
    payload = {
        "email": settings.SHIPROCKET_EMAIL,
        "password": settings.SHIPROCKET_PASSWORD
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("token")
    else:
        raise Exception(f"Shiprocket Authentication Failed: {response.text}")

def choose_best_courier(couriers):
    filtered = [
        c for c in couriers 
        if c.get('freight_charge') is not None and c.get('estimated_delivery_days') is not None
    ]
    if not filtered:
        return None

    def sort_key(c):
        try:
            return (float(c['freight_charge']), int(c['estimated_delivery_days']))
        except (ValueError, TypeError):
            return (9999, 99)

    return sorted(filtered, key=sort_key)[0]



    
def calculate_shipping_rate(product_uid, user):
    from accounts.models import Product
    from appname.models import ProFile
    import requests

    try:
        print(f"[DEBUG] Calculating shipping for Product UID: {product_uid}, User: {user}")

        token = get_shiprocket_token()
        print(f"[DEBUG] Shiprocket Token: {token}")

        product = Product.objects.get(uid=product_uid)
        customer_profile = ProFile.objects.get(user=user)
        seller_profile = ProFile.objects.get(user=product.user)

        delivery_pincode = str(customer_profile.coustmer_pincode)
        pickup_pincode = str(product.pincode)
        print(f"[DEBUG] Pickup Pincode: {pickup_pincode}, Delivery Pincode: {delivery_pincode}")

        actual_weight = product.weight
        volumetric_weight = (product.length * product.breadth * product.height) / 5000
        chargeable_weight = round(max(actual_weight, volumetric_weight), 2)

        print(f"[DEBUG] Actual Weight: {actual_weight}, Volumetric Weight: {volumetric_weight}, Chargeable Weight: {chargeable_weight}")

        params = {
            "pickup_postcode": pickup_pincode,
            "delivery_postcode": delivery_pincode,
            "cod": 0,
            "weight": chargeable_weight,
            "length": round(product.length, 2),
            "breadth": round(product.breadth, 2),
            "height": round(product.height, 2),
        }

        print(f"[DEBUG] Params for Shiprocket: {params}")

        headers = {
            "Authorization": f"Bearer {token}"
        }

        url = "https://apiv2.shiprocket.in/v1/external/courier/serviceability/"
        response = requests.get(url, headers=headers, params=params)

        print(f"[DEBUG] Shiprocket API Status: {response.status_code}, Response: {response.text}")

        if response.status_code == 200:
            data = response.json()
            rates = data.get("data", [])

            if isinstance(rates, dict):
                rates = [rates]

            return {"success": True, "rates": rates}

        return {"success": False, "message": "Shiprocket API error", "details": response.text}

    except Product.DoesNotExist:
        print("[ERROR] Product not found")
        return {"success": False, "message": "Product not found"}
    except ProFile.DoesNotExist:
        print("[ERROR] Profile not found")
        return {"success": False, "message": "Profile not found"}
    except Exception as e:
        print(f"[ERROR] Exception in calculate_shipping_rate: {e}")
        return {"success": False, "message": str(e)}




class GetShippingCostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        address = request.data.get("address", {})
        delivery_pincode = address.get("pincode")

        if not delivery_pincode:
            return JsonResponse({"error": "Delivery pincode required."}, status=400)

        cart_items = SavedCartItem.objects.filter(cart__user=user)
        shipping_data = []

        for item in cart_items:
            product = item.product
            pickup_pincode = product.pickup_pincode or "133001"  # fallback/default

            # Weight calculations
            actual_weight = float(product.weight or 0.5) * item.quantity
            length = float(product.length or 1)
            breadth = float(product.breadth or 1)
            height = float(product.height or 1)
            volumetric_weight = ((length * breadth * height) / 5000) * item.quantity

            chargeable_weight = max(actual_weight, volumetric_weight)
            chargeable_weight = max(0.5, round(chargeable_weight, 2))

            payload = {
                "pickup_postcode": pickup_pincode,
                "delivery_postcode": delivery_pincode,
                "cod": 0,
                "weight": chargeable_weight,
                "length": length,
                "breadth": breadth,
                "height": height,
            }

            # Get token
            token_response = requests.post(
                "https://sr-auth.shiprocket.in/v1/external/auth/login",
                json={
                    "email": settings.SHIPROCKET_EMAIL,
                    "password": settings.SHIPROCKET_PASSWORD,
                },
            )
            if token_response.status_code != 200:
                return JsonResponse({"error": "Authentication failed with Shiprocket"}, status=500)

            token = token_response.json().get("token")

            # Get shipping rates
            headers = {"Authorization": f"Bearer {token}"}
            rate_response = requests.post(
                "https://apiv2.shiprocket.in/v1/external/courier/serviceability/",
                json=payload,
                headers=headers,
            )

            if rate_response.status_code != 200:
                return JsonResponse({"error": "Failed to fetch shipping rates"}, status=500)

            rate_data = rate_response.json()
            courier_options = rate_data.get("data", {}).get("available_courier_companies", [])

            # Get cheapest rate
            cheapest = min(
                (c for c in courier_options if c.get("rate")),
                key=lambda x: x["rate"],
                default=None,
            )

            if cheapest:
                shipping_data.append({
                    "product": product.name,
                    "pickup_pincode": pickup_pincode,
                    "delivery_pincode": delivery_pincode,
                    "chargeable_weight": chargeable_weight,
                    "freight_charge": cheapest["rate"],
                    "courier_name": cheapest["courier_name"],
                    "estimated_delivery_days": cheapest["estimated_delivery_days"],
                })

        return JsonResponse({"shipping": shipping_data})

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

@csrf_exempt  # Remove this if you handle CSRF properly in your frontend
def checkout(request):
    user = request.user
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({'success': False, 'error': 'Invalid JSON'}, status=400)

        print(f"[DEBUG] POST Data Received: {data}")

        # Validate required fields
        required_fields = ['name', 'email', 'address', 'paymentMethod']
        missing_fields = [f for f in required_fields if not data.get(f)]
        if missing_fields:
            return JsonResponse({'success': False, 'error': f'Missing fields: {", ".join(missing_fields)}'}, status=400)

        try:
            saved_cart = SavedCart.objects.get(user=user)
            cart_items = saved_cart.get_items()
            print(f"[DEBUG] Cart Items fetched for POST: {len(cart_items)}")
        except SavedCart.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'No saved cart found for user'}, status=400)

        subtotal = sum(Decimal(item.get_price()) for item in cart_items)
        total_shipping = Decimal('0')
        shipping_breakdown = []
        courier_candidates = []

        for item in cart_items:
            print(f"[DEBUG] Calculating shipping for product: {item.product.product_name} (UID: {item.product.uid})")
            shipping_result = calculate_shipping_rate(product_uid=item.product.uid, user=user)
            print(f"[DEBUG] Shipping result: {shipping_result}")

            if shipping_result.get('success') and isinstance(shipping_result.get('rates'), list) and shipping_result['rates']:
                best_courier = choose_best_courier(shipping_result['rates'])
                if best_courier:
                    shipping_cost = Decimal(str(best_courier.get('freight_charge', '120')))
                    provider = best_courier.get('carrier_name', 'Unknown')
                    est_delivery = best_courier.get('estimated_delivery_days', None)
                    print(f"[DEBUG] Selected shipping cost: {shipping_cost} by {provider}")
                else:
                    shipping_cost = Decimal('120')
                    provider = "Default (No Valid Couriers)"
                    est_delivery = None
                    print("[DEBUG] No valid courier found, using default cost 120")
            else:
                shipping_cost = Decimal('120')
                provider = "Default (Error)"
                est_delivery = None
                print("[DEBUG] Shipping API error or no rates, using default cost 120")

            total_shipping += shipping_cost
            shipping_breakdown.append({
                'product': item.product.product_name,
                'cost': float(shipping_cost),
                'provider': provider,
                'estimated_delivery_days': est_delivery
            })

            if est_delivery is not None:
                courier_candidates.append({
                    'carrier_name': provider,
                    'total_shipping': shipping_cost,
                    'estimated_delivery_days': est_delivery
                })

        if courier_candidates:
            courier_candidates.sort(key=lambda c: (c['estimated_delivery_days'], c['total_shipping']))
            chosen_courier = courier_candidates[0]
            selected_courier_name = chosen_courier['carrier_name']
            estimated_delivery = chosen_courier['estimated_delivery_days']
            print(f"[DEBUG] Chosen courier for order: {selected_courier_name} with delivery {estimated_delivery} days")
        else:
            selected_courier_name = "Default"
            estimated_delivery = None
            print("[DEBUG] No valid courier candidates found, using default courier")

        total_amount = subtotal + total_shipping
        print(f"[DEBUG] Total amount (subtotal + shipping): {total_amount}")

        order = Order.objects.create(
            user=user,
            name=data['name'],
            email=data['email'],
            phone=data.get('phone', ''),
            address=data['address'],
            payment_method=data['paymentMethod'],
            transaction_id=data.get('transactionId', ''),
            total_amount=total_amount,
            shipping_cost=total_shipping,
            selected_courier=selected_courier_name,
            estimated_delivery=estimated_delivery,
        )
        print(f"[DEBUG] Order created with ID: {order.id}")

        for item in cart_items:
            product = item.product
            print(f"[DEBUG] Creating OrderItem for product: {product.product_name}, quantity: {item.quantity}, price: {item.get_price()}")
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item.quantity,
                price=Decimal(item.get_price()),
                seller_name=getattr(product, 'seller_name', ''),
                seller_email=getattr(product, 'seller_email', ''),
                seller_phone=getattr(product, 'seller_phone', ''),
            )

        print("[DEBUG] Clearing saved cart items after order creation")
        saved_cart.items.all().delete()

        send_confirmation_emails(order)
        print(f"[DEBUG] Confirmation emails sent for order ID: {order.id}")

        return JsonResponse({'success': True, 'orderId': order.id})

    # GET request - show checkout page
    try:
        saved_cart = SavedCart.objects.get(user=user)
        cart_items = saved_cart.get_items()
        print(f"[DEBUG] Cart Items fetched for GET: {len(cart_items)}")
    except SavedCart.DoesNotExist:
        cart_items = []
        print("[DEBUG] No saved cart found for user (GET)")

    subtotal = sum(Decimal(item.get_price()) for item in cart_items)
    total_shipping = Decimal('0')
    shipping_breakdown = []
    courier_candidates = []

    for item in cart_items:
        try:
            print(f"[DEBUG] Starting shipping calculation for product: {item.product.product_name} (UID: {item.product.uid})")
            shipping_result = calculate_shipping_rate(product_uid=item.product.uid, user=user)
            print(f"[DEBUG] Shipping result: {shipping_result}")

            if shipping_result.get('success') and isinstance(shipping_result.get('rates'), list) and shipping_result['rates']:
                best_courier = choose_best_courier(shipping_result['rates'])
                if best_courier:
                    shipping_cost = Decimal(str(best_courier.get('freight_charge', '120')))
                    provider = best_courier.get('carrier_name', 'Unknown')
                    est_delivery = best_courier.get('estimated_delivery_days', None)
                    print(f"[DEBUG] Best courier: {provider} with ₹{shipping_cost}, delivery in {est_delivery} days")
                else:
                    shipping_cost = Decimal('120')
                    provider = "Default (No Valid Couriers)"
                    est_delivery = None
                    print("[DEBUG] No valid courier found, using default cost ₹120")
            else:
                shipping_cost = Decimal('120')
                provider = "Default (Error)"
                est_delivery = None
                print("[DEBUG] API error or no rates returned, using default shipping ₹120")

            total_shipping += shipping_cost
            shipping_breakdown.append({
                'product': item.product.product_name,
                'cost': float(shipping_cost),
                'provider': provider,
                'estimated_delivery_days': est_delivery,
            })

            if est_delivery is not None:
                courier_candidates.append({
                    'carrier_name': provider,
                    'total_shipping': shipping_cost,
                    'estimated_delivery_days': est_delivery
                })

        except Exception as e:
            print(f"[ERROR] Exception during shipping calculation for {item.product.product_name}: {e}")
            shipping_cost = Decimal('120')
            total_shipping += shipping_cost
            shipping_breakdown.append({
                'product': item.product.product_name,
                'cost': float(shipping_cost),
                'provider': 'Default (Exception)',
                'estimated_delivery_days': None
            })

    if courier_candidates:
        courier_candidates.sort(key=lambda c: (c['estimated_delivery_days'], c['total_shipping']))
        chosen_courier = courier_candidates[0]
        selected_courier_name = chosen_courier['carrier_name']
        estimated_delivery = chosen_courier['estimated_delivery_days']
    else:
        selected_courier_name = "Default"
        estimated_delivery = None

    total = subtotal + total_shipping
    print(f"[DEBUG] Total Shipping: ₹{total_shipping}")
    print(f"[DEBUG] Total Order Amount (subtotal + shipping): ₹{total}")

    # Optional: Prefill user info if you have profile data
    profile = getattr(user, 'profile', None)  # change as per your profile model name

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'subtotal': float(round(subtotal, 2)),
        'shipping': float(round(total_shipping, 2)),
        'total': float(round(total, 2)),
        'shipping_breakdown': shipping_breakdown,
        'selected_courier': selected_courier_name,
        'estimated_delivery': estimated_delivery,
        'user_name': profile.name if profile and hasattr(profile, 'name') else user.get_full_name(),
        'user_email': user.email,
        'user_phone': profile.phone if profile and hasattr(profile, 'phone') else '',
        'user_address': profile.address if profile and hasattr(profile, 'address') else '',
    })
