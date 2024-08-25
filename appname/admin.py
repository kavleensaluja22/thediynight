from django.contrib import admin

# Register your models here.
from .models import ProFile
from .models import CartItems
from .models import Cart
from .models import Coupon

# Register your models here.

admin.site.register(ProFile)
admin.site.register(CartItems)
admin.site.register(Cart)
admin.site.register(Coupon)

