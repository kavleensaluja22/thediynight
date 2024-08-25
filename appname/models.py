from django.db import models
from django.contrib.auth.models import User 
from base.models import BaseModel
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from base.emails import send_account_activation_email
import uuid 
from django.db import models
from accounts.models import Product
from accounts.models import Product, ColorVariant, SizeVariant  # Import models from accounts

class ProFile(BaseModel):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="ProFile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100 , null=True , blank=True)
    Profile_image = models.ImageField(upload_to = 'ProFile' , default='default.jpg' )

    def get_cart_count(self):
        return CartItems.objects.filter(cart__is_paid = False , cart__user = self.user ).count
    

class Coupon(BaseModel):
    coupon_code = models.CharField(max_length=50)
    is_expired = models.BooleanField(default=False)
    discount_price = models.IntegerField(default=100)
    minimum_amount = models.IntegerField(default=300)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.ForeignKey(SizeVariant, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(ColorVariant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.product_name}"

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
    
from base.emails import send_account_activation_email  # Assume this is a utility function to send email

@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    if created:
        email_token = str(uuid.uuid4())
        ProFile.objects.create(user=instance, email_token=email_token)
        email = instance.email
        send_account_activation_email(email, email_token)




 # Import Product, ColorVariant, SizeVariant
