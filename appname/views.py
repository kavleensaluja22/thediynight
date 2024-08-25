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


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
import uuid 

def sign(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken. ')
            return HttpResponseRedirect(request.path_info)
        
        user_obj=User.objects.create(first_name=first_name,last_name=last_name, email=email, username=email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An Email has been sent on your mail  ')
        return HttpResponseRedirect(request.path_info)


    return render(request, "user/sign.html")



def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found')
            return HttpResponseRedirect(request.path_info)
        
        if not user_obj[0].ProFile.is_email_verified:
            messages.warning(request, 'Account not verified')
            return HttpResponseRedirect(request.path_info)

        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)  # Using auth_login to avoid conflict
            return redirect('/')
        else:
            messages.warning(request, 'Invalid Credentials')
            return HttpResponseRedirect(request.path_info)

    return render(request, "user/login.html")

def searchMatch(query, item):
    return True



def activate_email(request, email_token):
    print(f"Token received: {email_token}")
    try:
        user_profile = ProFile.objects.get(email_token=email_token)
        print(f"User profile found: {user_profile}")
        user_profile.is_email_verified = True
        user_profile.save()
        return redirect('home')  # Ensure 'home' URL name is correctly defined
    except ProFile.DoesNotExist:
        print("Token not found")
        return HttpResponse('Invalid Email Token', status=404)
    
    

def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user 
    cart , _ = Cart.objects.get_or_create(user = user , is_paid = False)
    cart_items = CartItems.objects.create(cart=cart , product=product)

    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        CartItems.size_variant=size_variant 
        CartItems.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    

def remove_cart(request , cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        CartItems.delete()

    except Exception as e :
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def cart(request):
#     # context ={'cart' : Cart.objects.get(is_paid=False , user = request.user)}
#     # if request.method =='POST':
#     return render(request , 'home/cart.html')


from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from accounts.models import Product, SizeVariant, ColorVariant


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

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from accounts.models import Product, Review
from accounts.forms import ReviewForm

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


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, SizeVariant, ColorVariant
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id=None, uid=None):
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    elif uid:
        product = get_object_or_404(Product, uid=uid)
    else:
        product = get_object_or_404(Product, id=product_id)
        size_name = request.GET.get('size')
        color_name = request.GET.get('color')
        quantity = int(request.GET.get('quantity', 1))

        size = SizeVariant.objects.get(size_name=size_name) if size_name else None
        color = ColorVariant.objects.get(color_name=color_name) if color_name else None

        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            size=size,
            color=color
         )
        cart_item.quantity += quantity
        cart_item.save()

        return redirect('cart')

@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'home/cart.html', {'cart_items': cart_items})

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
def user(request):
    return render(request,'home/user.html')