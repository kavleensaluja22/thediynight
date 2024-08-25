import uuid
from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.contrib.auth.models import User

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

class ProductImage(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk and self.image:
            filename = f'{uuid4()}.{self.image.name.split(".")[-1]}'
            self.image.name = filename
        super().save(*args, **kwargs)

class Product(models.Model):
    uid = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.IntegerField()
    product_description = models.TextField()
    color_variants = models.ManyToManyField(ColorVariant, related_name="products", blank=True)
    size_variants = models.ManyToManyField(SizeVariant, related_name="products", blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    def get_product_price_by_size(self, size):
        return self.price + self.size_variants.get(size_name=size).price

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category_image = models.ImageField(upload_to='categories/', blank=True, null=True, default='path/to/default/image.jpg')

    def __str__(self):
        return self.category_name




class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    media = models.FileField(upload_to='review_media/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review by {self.user.username} on {self.product.product_name}'