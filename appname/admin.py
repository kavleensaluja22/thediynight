from django.contrib import admin

# Register your models here.
from .models import ProFile
from .models import CartItems
from .models import Cart
from .models import Address, Phone 

from .models import Coupon
# from .models import UserProfile

# Register your models here.

from django.contrib import admin
from .models import ProFile

@admin.register(ProFile)
class ProFileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'email', 'name', 'is_seller', 'kyc_verified',
        'phone', 'city', 'state', 'coustmer_pincode', 'custom_pickup_name'
    )
    list_filter = ('is_seller', 'kyc_verified', 'state', 'city')
    search_fields = ('user__username', 'email', 'name', 'phone', 'city', 'state')
    
    fieldsets = (
        ('User Info', {
            'fields': ('user', 'email', 'is_seller', 'kyc_verified', 'profile_image')
        }),
        ('Personal Details', {
            'fields': (
                'name', 'last_name', 'phone', 'address', 'city', 'state', 
                'coustmer_pincode', 'house_number', 'street', 'locality'
            )
        }),
        ('Shiprocket Pickup', {
            'fields': ('custom_pickup_name',)
        }),
        ('Verification', {
            'fields': ('is_email_verified', 'email_token', 'last_password_reset')
        }),
    )

admin.site.register(CartItems)
admin.site.register(Cart)
admin.site.register(Coupon)



admin.site.register(Address)


admin.site.register(Phone)
# admin.site.register(UserProfile)
