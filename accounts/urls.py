
from django.urls import path , include

from django.conf.urls.static import static
from django.conf import settings

from .views import CreateProductView
from . import views
# from .views import GetShippingCostView

urlpatterns = [
    path('',views.home,name="home"),
    
     path('cart/', views.cart_view, name='cart'),
    path('tr',views.tr,name="tr"),
    path('submit_review/<uuid:product_uid>/', views.submit_review, name='submit_review'),
    path('get-reviews/<uuid:product_uid>/', views.get_reviews, name='get_reviews'),
path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),

    path('prodd/<slug:product_slug>/',views.prodd,name="prodd"),

    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('delete_review/<int:review_id>/',views.delete_review, name='delete_review'),
   path('remove-item/', views.remove_item, name='remove_item'),
    path('calculate_shipping_rate/', views.calculate_shipping_rate, name='calculate_shipping_rate'),
    path('update-quantity/', views.update_quantity, name='update_quantity'),
    path('update-size/', views.update_size, name='update_size'),
    path('update-color/', views.update_color, name='update_color'),
  
 path('api/cart-summary/', views.cart_summary_api, name='cart_summary_api'),
# path("get-shipping/", GetShippingCostView.as_view(), name="get_shipping"),

path('checkout/', views.checkout, name='checkout'),
 path('search/', views.search_products, name='search_products'),
#  path('api/search-products/', views.api_search_products, name='api_search_products'),
    path("save-cart/", views.save_cart, name="save_cart"),
    path("load-cart-on-login/", views.load_cart, name="load_cart"),
       path('api/categories/', views.get_categories, name='get_categories'),
      path('create-product/', CreateProductView.as_view(), name='create_product'),

] 


