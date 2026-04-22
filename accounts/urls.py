
from django.urls import path , include

from django.conf.urls.static import static
from django.conf import settings
from .views import shiprocket_webhook
from .views import CreateProductView
from . import views
# from .views import GetShippingCostView

urlpatterns = [
    path('',views.home,name="home"),
 path('track/', views.track_order_view, name='track'),

  path(' update_order_delivery_status', views. update_order_delivery_status, name=' update_order_delivery_status'),
     path('create_shiprocket_pickup_location', views.create_shiprocket_pickup_location, name='create_shiprocket_pickup_location'),
  path("assign-awb/", views.assign_awb_view, name="assign_awb"),


     path('cart/', views.cart_view, name='cart'),

    path('submit_review/<uuid:product_uid>/', views.submit_review, name='submit_review'),
    path('get-reviews/<uuid:product_uid>/', views.get_reviews, name='get_reviews'),
path('delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
 path('split_and_create_orders',views.split_and_create_orders,name="split_and_create_orders"),
 path('create_shiprocket_order',views.create_shiprocket_order,name="create_shiprocket_order"),
    path('prodd/<slug:product_slug>/',views.prodd,name="prodd"),
path('process_cart_items', views.process_cart_items, name='process_cart_items'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('delete_review/<int:review_id>/',views.delete_review, name='delete_review'),
   path('remove-item/', views.remove_item, name='remove_item'),
    path('calculate_shipping_rate/', views.calculate_shipping_rate, name='calculate_shipping_rate'),
    path('update-quantity/', views.update_quantity, name='update_quantity'),
    path('update-size/', views.update_size, name='update_size'),
    path('update-color/', views.update_color, name='update_color'),
path('request-return/<int:suborder_id>/', views.request_return, name='request_return'),
path('approve-return/<int:suborder_id>/', views.approve_return_and_create_reverse_pickup, name='approve_return'),
 path('api/cart-summary/', views.cart_summary_api, name='cart_summary_api'),

path('notify_shiprocket_order_ready', views.notify_shiprocket_order_ready, name='notify_shiprocket_order_ready'),
path("shiprocket/webhook/", shiprocket_webhook, name="shiprocket_webhook"),
path('checkout/', views.checkout, name='checkout'),
 path('search/', views.search_products, name='search_products'),

    path("save-cart/", views.save_cart, name="save_cart"),
    path("load-cart-on-login/", views.load_cart, name="load_cart"),
  path("trigger_refund/<int:order_id>/", views.trigger_refund, name="trigger_refund"),
path('generate_pickup/', views.generate_pickup, name='generate_pickup'),


       path('update-order-status/<int:suborder_id>/', views.update_order_status, name='update_order_status'),


    path("cancel_shiprocket_order", views.cancel_shiprocket_order, name="cancel_shiprocket_order"),
    path("create_shiprocket_order_for_suborder", views.create_shiprocket_order_for_suborder, name="create_shiprocket_order_for_suborder"),
    
 

    #  path('seller-dashboard/', views.seller_dashboard, name='seller_dashboard'),
       path('api/categories/', views.get_categories, name='get_categories'),
          path('print_manifest/', views.print_manifest, name='print_manifest'),
path('generate_label/', views.generate_label, name='generate_label'),
path('print_invoice/', views.print_invoice, name='print_invoice'),



] 

