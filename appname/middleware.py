# appname/middleware.py
from django.utils.deprecation import MiddlewareMixin
from .models import Cart, CartItems

class SaveCartOnLogoutMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.user.is_authenticated and request.session.get('cart'):
            cart_items = request.session.get('cart')
            try:
                # Get or create a cart for the user
                user_cart, created = Cart.objects.get_or_create(user=request.user)
                
                # Clear existing cart items
                CartItems.objects.filter(cart=user_cart).delete()

                # Add cart items from the session to the database
                for item in cart_items:
                    CartItems.objects.create(
                        cart=user_cart,
                        product_id=item['product_id'],
                        color_variant_id=item['color_id'],
                        size_variant_id=item['size_id'],
                        quantity=item['quantity']
                    )
                
                # Clear the cart session
                request.session['cart'] = []
            except Exception as e:
                print(f"Error saving cart on logout: {e}")

        return response
