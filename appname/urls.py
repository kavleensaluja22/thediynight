from appname import views 
from django.urls import path , include 
 


urlpatterns = [
path('user_login',views.user_login,name="user_login"),
path('sign',views.sign,name="sign"),
# path('send_email_to_client',views.send_email_to_client,name="send_email_to_client"),

path('activate_email/<str:email_token>/', views.activate_email, name='activate_email'),
path('add_to_cart', views.add_to_cart, name="add_to_cart"),

path('remove_cart', views.remove_cart, name="remove_cart"),
path('get_price/', views.get_price, name='get_price'),
path('product/<uuid:product_uid>/', views.product_detail, name='product_detail'),
path('add_to_cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),

path('cart/', views.cart, name='cart'),
path('track', views.track, name='track'),
path('user', views.user, name='user'),
path('update_quantity/<int:cart_id>/', views.update_quantity, name='update_quantity'),

]
