from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse , HttpResponseRedirect 
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout 

from django.shortcuts import get_object_or_404
from accounts.models import Category
from accounts.models import Product, ColorVariant, SizeVariant


# Create your views here.

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'home/home.html', {'products': products, 'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category_detail.html', context)

def tr(request):
    return render(request, "tr.html")

from django.shortcuts import render, HttpResponse
from .models import Product
def prodd(request, product_slug):
    try:
        # Fetch the product using the slug
        product = Product.objects.get(slug=product_slug)
        
        # Fetch similar products from the same category, excluding the current one
        similar_products = Product.objects.filter(category=product.category).exclude(uid=product.uid)

        # Add product and similar products to the context
        context = {
            'product': product,
            'similar_products': similar_products,
            'product_id': product.uid,  # Use 'uid' instead of 'id'
        }

        # Render the template with the context
        return render(request, "home/prodd.html", context)
    
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")


    except Product.DoesNotExist:
        # Return 404 if the product is not found
        return HttpResponseNotFound("Product not found")
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm

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
    product = get_object_or_404(Product, uid=product_uid)  # Changed to uid
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
def delete_review(request, review_id):
    if request.method == 'POST':
        review = get_object_or_404(Review, id=review_id)
        if review.user == request.user or request.user.is_superuser:
            review.delete()
            return JsonResponse({'message': 'Review deleted successfully'})
        return JsonResponse({'message': 'Permission denied'}, status=403)
    return JsonResponse({'message': 'Invalid request method'}, status=405)



from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from .models import Order, OrderItem
import json

@csrf_exempt
def checkout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.create(
            user=request.user,
            name=data['name'],
            email=data['email'],
            address=data['address'],
            city=data['city'],
            country=data['country'],
            payment_method=data['paymentMethod'],
            transaction_id=data.get('transactionId', ''),
            total_amount=data['totalAmount']
        )
        for item in data['items'].values():
            OrderItem.objects.create(
                order=order,
                product_name=item['name'],
                quantity=item['quantity'],
                price=item['price']
            )
        send_confirmation_emails(order)
        return JsonResponse({'success': True, 'orderId': order.id})
    return render(request, 'checkout.html')

def send_confirmation_emails(order):
    customer_email = order.email
    merchant_email = 'thediynight@gmail.com'
    customer_subject = 'Order Confirmation'
    customer_message = f'Thank you for your order! Your order ID is {order.id}. Total amount: Rs. {order.total_amount}'
    merchant_subject = 'New Order Received'
    merchant_message = f'New order received! Order ID: {order.id}. Customer: {order.name}. Total amount: Rs. {order.total_amount}'
    send_mail(customer_subject, customer_message, 'noreply@example.com', [customer_email])
    send_mail(merchant_subject, merchant_message, 'noreply@example.com', [merchant_email])

def success(request):
    return redirect(request, 'home/home.html')