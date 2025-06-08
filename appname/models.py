from django.db import models
from django.contrib.auth.models import User 
from base.models import BaseModel
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from base.emails import send_verification_email
import uuid 
from django.db import models
from accounts.models import Product
from accounts.models import Product, ColorVariant, SizeVariant  # Import models from accounts

class ProFile(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define a primary key
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    kyc_verified = models.BooleanField(default=False) 
    coustmer_pincode = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    last_password_reset = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.user.username

    
  


class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=50)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=300)

from django.conf import settings
from django.db import models

def get_default_product():
    from accounts.models import Product
    try:
        return Product.objects.first().uid  # Ensure a valid product is assigned
    except AttributeError:
        return uuid.uuid4() 

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=get_default_product)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(SizeVariant, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(ColorVariant, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    color_variant = models.ForeignKey(ColorVariant, on_delete=models.SET_NULL, null=True, blank=True)
    size_variant = models.ForeignKey(SizeVariant, on_delete=models.SET_NULL, null=True, blank=True)


    def get_product_price(self):
        price = [self.product.price]

        if self.color_variant:
            color_variant_price = self.color_variant.price 
            price.append(color_variant_price)
        if self.size_variant:
            size_variant_price = self.size_variant.price 
            price.append(size_variant_price)
        return sum(price)
    





 # Import Product, ColorVariant, SizeVariant
from django.db import models
from django.contrib.auth.models import User
class Address(models.Model):
    profile = models.ForeignKey(ProFile, on_delete=models.CASCADE, null=True, blank=True, related_name="addresses")  
    name = models.CharField(max_length=100)  # e.g., Home, Work
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)  # Track the default address

    def save(self, *args, **kwargs):
        # Ensure only one default address exists per profile
        if self.is_default:
            Address.objects.filter(profile=self.profile).update(is_default=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.city}"
    

from django.db import models
from django.contrib.auth.models import User

class Phone(models.Model):
    user = models.ForeignKey(User, related_name='phones', on_delete=models.CASCADE)
    number = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=[
        ('mobile', 'Mobile'),
        ('home', 'Home'),
        ('work', 'Work')
    ])

    def __str__(self):
        return f"{self.number} ({self.get_type_display()})"
    
def load_cart_from_db(request):
    if request.user.is_authenticated:
        # Fetch all cart items from the database for this user
        cart_items = Cart.objects.filter(user=request.user)
        
        session_cart = []
        for item in cart_items:
            session_cart.append({
                'product_id': item.product.id,
                'quantity': item.quantity,
                'size_id': item.size.id if item.size else None,
                'color_id': item.color.id if item.color else None,
            })
        
        # Store the cart items in the session
        request.session['cart'] = session_cart



from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

class SellerPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    razorpay_order_id = models.CharField(max_length=255)
    razorpay_payment_id = models.CharField(max_length=255)
    amount = models.DecimalField(default=Decimal('3.00'), max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, default='paid')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"SellerPayment: {self.user.username} - {self.amount} - {self.status}"