from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ProductImage, Product, SizeVariant, ColorVariant, Category
from .models import PromoCode
from .models import SellerProfile
from .models import ProductView


# admin.py

from django.contrib import admin
from .models import Product, Category, ColorVariant, SizeVariant, ProductImage, Order, OrderItem, Review, ProductCustomizationField, SavedCart, SavedCartItem, OrderCustomization


# Product Admin
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ColorVariantInline(admin.TabularInline):
    model = Product.color_variants.through
    extra = 1

class SizeVariantInline(admin.TabularInline):
    model = Product.size_variants.through
    extra = 1

@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
        ColorVariantInline,
        SizeVariantInline,
    ]
    list_display = ('product_name', 'uid', 'category', 'price', 'seller_name')  # added uid and seller_name
    prepopulated_fields = {'slug': ('product_name',)}

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}

# ColorVariant Admin
@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'price')

    def response_add(self, request, obj, post_url_continue=None):
        if "_popup" in request.GET:
            return HttpResponseRedirect(reverse('admin:accounts_colorvariant_changelist') + "?_popup=1&_to_field=id")
        return super().response_add(request, obj, post_url_continue)

# SizeVariant Admin
@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ('size_name', 'price')

    def response_add(self, request, obj, post_url_continue=None):
        if "_popup" in request.GET:
            return HttpResponseRedirect(reverse('admin:accounts_sizevariant_changelist') + "?_popup=1&_to_field=id")
        return super().response_add(request, obj, post_url_continue)

# ProductImage Admin
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')

# Review Admin
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'text', 'created_at', 'media']
    search_fields = ['product__product_name', 'user__username']

# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'total_amount', 'created_at')
    search_fields = ('name', 'email', 'transaction_id')
    list_filter = ('created_at', 'payment_method')

# OrderItem Admin
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity', 'price', 'seller_name', 'seller_email', 'seller_phone')

    def product_name(self, obj):
        return obj.product.product_name  # Access product_name from the related Product

    product_name.admin_order_field = 'product__product_name'  # Allow ordering by product_name
    product_name.short_description = 'Product Name'

# Other Model Registrations
admin.site.register(SavedCart)
admin.site.register(SavedCartItem)
admin.site.register(OrderCustomization)
admin.site.register(ProductCustomizationField)
admin.site.register (PromoCode)

admin.site.register (ProductView)

admin.site.register (SellerProfile)