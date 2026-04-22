from appname import views     
from django.urls import path , include 
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from allauth.account.views import ConfirmEmailView
from .views import CustomPasswordResetView
from .views import CustomPasswordResetConfirmView
from .views import (
    CreateSellerPaymentView,
   
    # other views...
)
from .views import SellerPaymentCallbackView

# from .views import CustomPasswordResetConfirmView
# from .views import CreateOrderView
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
def redirect_user_to_profile(request):
    return redirect("profile")
from django.shortcuts import redirect
urlpatterns = [
   path('api/categories/', views.get_categories, name='get_categories'),
path('user_login',views.user_login,name="user_login"),
path('sign',views.sign,name="sign"),
path('remove_cart', views.remove_cart, name="remove_cart"),
path('get_price/', views.get_price, name='get_price'),
path('product/<uuid:product_uid>/', views.product_detail, name='product_detail'),

# path('user', views.user, name='user'),
path('update_quantity/<int:cart_id>/', views.update_quantity, name='update_quantity'),
path('user/', views.redirect_user_to_profile, name='redirect_user_to_profile'),
 path('logout/', views.custom_logout, name='logout'),
 path('api/addresses/', views.get_addresses, name='get_addresses'),
# path('create-order/', views.CreateOrderView.as_view(), name='create_order'),
path('reset_password/', CustomPasswordResetView.as_view(), name='password_reset'),

    
   path('apply-promo-code/', views.apply_promo_code, name='apply_promo_code'),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), 
         name='password_reset_done'),
path('reset/<uidb64>/<token>/',
     CustomPasswordResetConfirmView.as_view(template_name='reset_password_confirm.html'),
     name='password_reset_confirm'),




    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), 
         name='password_reset_complete'),

path('user_main', views.user_main, name='user_main'),
path('checkout/', views.checkout, name='checkout'),
    path('api/create-product/', views.create_product, name='create-product'),
path('logout/', views.custom_logout, name='logout'),


  path('api/products/', views.get_products, name='get_products'),
 path('activate-email/<str:token>/', views.activate_email, name='activate_email'),
    path("profile/", views.profile_view, name="profile"),
    path("dashboard_view/", views.dashboard_view, name="dashboard_view"),
path("create-payment/", views.CreatePaymentView.as_view(), name="create-payment"),

# path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path("payment-callback/", views.PaymentCallbackView.as_view(), name="payment_callback"),
 path('edit-product/<uuid:product_id>/', views.edit_product, name='edit_product'),
# path('product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
path('remove_product/<uuid:product_id>/', views.remove_product, name='remove_product'),

    path('create-seller-payment/', CreateSellerPaymentView.as_view(), name='create_seller_payment'),
    path('seller/payment/callback/', SellerPaymentCallbackView.as_view(), name='seller_payment_callback'),
path('sellerdashboard/', views.sellerdashboard, name='sellerdashboard'),



 re_path(
        r"^accounts/confirm-email/(?P<key>[-:\w]+)/$",
        ConfirmEmailView.as_view(),
        name="account_confirm_email",
    ),
 

]


