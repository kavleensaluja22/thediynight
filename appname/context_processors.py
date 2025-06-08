from accounts.models import SavedCart

def cart_count_processor(request):
    if request.user.is_authenticated:
        try:
            saved_cart = SavedCart.objects.get(user=request.user)
            count = sum(item.quantity for item in saved_cart.items.all())
            return {'cart_count': count}
        except SavedCart.DoesNotExist:
            return {'cart_count': 0}
    return {'cart_count': 0}
