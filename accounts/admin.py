from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ProductImage, Product, SizeVariant, ColorVariant, Category

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
    list_display = ('product_name', 'category', 'price')
    prepopulated_fields = {'slug': ('product_name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug')
    prepopulated_fields = {'slug': ('category_name',)}

@admin.register(ColorVariant)
class ColorVariantAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'price')

    def response_add(self, request, obj, post_url_continue=None):
        if "_popup" in request.GET:
            return HttpResponseRedirect(reverse('admin:accounts_colorvariant_changelist') + "?_popup=1&_to_field=id")
        return super().response_add(request, obj, post_url_continue)

@admin.register(SizeVariant)
class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ('size_name', 'price')

    def response_add(self, request, obj, post_url_continue=None):
        if "_popup" in request.GET:
            return HttpResponseRedirect(reverse('admin:accounts_sizevariant_changelist') + "?_popup=1&_to_field=id")
        return super().response_add(request, obj, post_url_continue)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')



from .models import Review

admin.site.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'text', 'created_at']
    search_fields = ['product__product_name', 'user__username']