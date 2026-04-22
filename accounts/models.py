import uuid
from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.contrib.auth.models import User
from uuid import uuid4
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from uuid import uuid4
from django.db import models
from uuid import uuid4
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.size_name


class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return self.color_name
    
from django.utils.text import slugify

def generate_unique_slug(name):
    base_slug = slugify(name)
    slug = base_slug
    counter = 1
    while Product.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    return slug



class Product(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")  # seller
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)

    # Shipping specs
    weight = models.FloatField(help_text="Weight in kilograms")
    length = models.FloatField(help_text="Length in cm")
    breadth = models.FloatField(help_text="Breadth in cm")
    height = models.FloatField(help_text="Height in cm")
    price = models.IntegerField()
    pincode = models.IntegerField()
    product_description = models.TextField()

    # Variants
    color_variants = models.ManyToManyField('ColorVariant', related_name="products", blank=True)
    size_variants = models.ManyToManyField('SizeVariant', related_name="products", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    def get_product_price_by_size_and_color(self, size_name=None, color_name=None):
        total_price = self.price
        if size_name:
            try:
                size_variant = self.size_variants.get(size_name=size_name)
                total_price += size_variant.price
            except SizeVariant.DoesNotExist:
                pass
        if color_name:
            try:
                color_variant = self.color_variants.get(color_name=color_name)
                total_price += color_variant.price
            except ColorVariant.DoesNotExist:
                pass
        return total_price

    def get_star_rating(self):
        views = ProductView.objects.filter(product=self)
        total_views = views.count()
        if total_views == 0:
            return 0
        return min(5, total_views // 10)

    def get_main_image_url(self):
        main_image = self.product_images.filter(is_main=True).first()
        if main_image and main_image.image:
            return main_image.image.url
        return '/static/images/default_product.jpg'


class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    is_main = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk and self.image:
            filename = f'{uuid4()}.{self.image.name.split(".")[-1]}'
            self.image.name = filename

        if not self.is_main:
            if not self.product.product_images.filter(is_main=True).exists():
                self.is_main = True

        super().save(*args, **kwargs)

        if self.is_main:
            ProductImage.objects.filter(product=self.product).exclude(pk=self.pk).update(is_main=False)



class ProductView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'product')  # Ensures each user can only view the product once per time




class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category_image = models.ImageField(upload_to='categories/', blank=True, null=True, default='path/to/default/image.jpg')

    def __str__(self):
        return self.category_name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)




from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField()
    media = models.FileField(upload_to='review_media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.product.product_name}'
    
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    payment_method = models.CharField(max_length=20)
    transaction_id = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    # Razorpay payment fields
    razorpay_order_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=255, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    refund_status = models.CharField(max_length=20, null=True, blank=True)

    # Shipping tracking summary (copied from SubOrder)
    selected_courier = models.CharField(max_length=255, blank=True, null=True)
    shiprocket_order_id = models.CharField(max_length=100, blank=True, null=True)
    shipment_id = models.CharField(max_length=100, blank=True, null=True)
    awb_code = models.CharField(max_length=100, blank=True, null=True)
    estimated_delivery = models.IntegerField(null=True, blank=True)  # in days
    is_delivered = models.BooleanField(default=False)
    delivery_date = models.DateTimeField(null=True, blank=True)
    delivery_status_snapshot = models.TextField(null=True, blank=True)

    # Order status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"Order {self.id} by {self.name}"



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)  # Link to Product
    quantity = models.PositiveIntegerField()
    suborder = models.ForeignKey("SubOrder", on_delete=models.CASCADE, related_name="items", null=True, blank=True) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller_name = models.CharField(max_length=255, blank=True, null=True)
    seller_email = models.EmailField(blank=True, null=True)
    seller_phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        product_name = self.product.product_name if self.product else "Unknown Product"
        order_id = self.order.id if self.order else "Unknown Order"
        return f"{self.quantity} x {product_name} in Order {order_id}"



# models.py

from django.db import models
from django.contrib.auth.models import User

class SavedCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def get_items(self):
        return self.items.all()

    def __str__(self):
        return f"{self.user.username}'s Saved Cart"


class SavedCartItem(models.Model):
    cart = models.ForeignKey(SavedCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('accounts.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    color_variant = models.ForeignKey('accounts.ColorVariant', on_delete=models.SET_NULL, null=True, blank=True)
    size_variant = models.ForeignKey('accounts.SizeVariant', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.URLField(blank=True, null=True)  # Optional image URL

    def __str__(self):
        return f"{self.product.product_name} ({self.quantity})"

    def get_price(self):
        base_price = self.product.price
        size_price = self.size_variant.price if self.size_variant else 0
        color_price = self.color_variant.price if self.color_variant else 0
        return base_price + size_price + color_price

    def get_total_price(self):
       return self.get_price() * self.quantity
 



from django.db import models

class ProductCustomizationField(models.Model):
    FIELD_TYPE_CHOICES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('song_name', 'Song Name'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='customization_fields')
    label = models.CharField(max_length=255)  # e.g., "Enter your name", "Upload image"
    field_type = models.CharField(max_length=20, choices=FIELD_TYPE_CHOICES)
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.product_name} - {self.label}"

class OrderCustomization(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE, related_name='customizations')
    field_label = models.CharField(max_length=255)  # Store label like "Enter Name"
    value = models.TextField(blank=True, null=True)  # Can be URL for image or text or song name

    def __str__(self):
        return f"{self.field_label}: {self.value}"


class PromoCode(models.Model):
    code = models.CharField(max_length=20, unique=True)  # Promo code (e.g., 'DISCOUNT5')
    discount_percentage = models.IntegerField()  # Discount amount (e.g., 5 for 5% discount)
    is_used = models.BooleanField(default=False)  # To track if the promo code has been used globally
    used_by = models.ManyToManyField(User, blank=True)  # Track users who have used this promo code

    def __str__(self):
        return self.code

    def can_be_used_by_user(self, user):
        """ Check if the user has already used this promo code """
        return user not in self.used_by.all() and not self.is_used
    

from django.db import models
from django.contrib.auth.models import User

# class SellerProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     aadhar_number = models.CharField(max_length=12)
#     pan_number = models.CharField(max_length=10)
#     is_kyc_verified = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

from django.utils import timezone
from datetime import timedelta

class SubOrder(models.Model):
    main_order = models.ForeignKey(Order, related_name='suborders', on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    shiprocket_order_id = models.CharField(max_length=100, blank=True, null=True)
    shipment_id = models.CharField(max_length=100, blank=True, null=True)
    awb_code = models.CharField(max_length=100, blank=True, null=True)
    selected_courier = models.CharField(max_length=100, blank=True, null=True)

    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # 💰 Financial fields
    seller_payout = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    shiprocket_deduction = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    platform_fee = models.DecimalField(max_digits=10, decimal_places=2, default=10.00)  # ₹10 platform fee
    is_return_requested = models.BooleanField(default=False)
    return_requested_at = models.DateTimeField(null=True, blank=True)
    is_return_approved = models.BooleanField(default=False)
    is_return_picked = models.BooleanField(default=False)
    is_refunded = models.BooleanField(default=False)

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Ready to Ship", "Ready to Ship"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return f"SubOrder {self.id} for {self.seller.username}"
    
    def is_return_eligible(self):
        if self.status != 'delivered':
           return False
        if self.return_requested_at:
           return False
        if self.delivered_at:  # assuming you have this field
            return timezone.now() <= self.delivered_at + timedelta(hours=24)
        return False
