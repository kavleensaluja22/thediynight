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
        product = Product.objects.get(slug=product_slug)
        similar_products = Product.objects.filter(category=product.category).exclude(pk=product.pk)
        
        context = {
            'product': product,
            'similar_products': similar_products,
        }

        return render(request, "home/prodd.html", context)
    
    except Product.DoesNotExist:
        return HttpResponseNotFound("Product not found")

from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, Review
from .forms import ReviewForm

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Product, Review

@login_required
def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = get_object_or_404(Product, uid=form.cleaned_data['product_uid'])
            review.save()
            data = {
                'message': 'Review submitted successfully',
                'review': {
                    'id': review.id,
                    'rating': review.rating,
                    'text': review.text,
                    'media': review.media.url if review.media else '',
                    'user': request.user.id
                }
            }
            return JsonResponse(data)
        else:
            return JsonResponse({'message': 'Invalid form data'}, status=400)
    return JsonResponse({'message': 'Invalid request method'}, status=405)

def delete_review(request, review_id):
    if request.method == 'POST':
        review = get_object_or_404(Review, id=review_id, user=request.user)
        review.delete()
        return JsonResponse({'message': 'Review deleted successfully'})
    return JsonResponse({'message': 'Invalid request method'}, status=405)