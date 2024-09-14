
from django.urls import path , include

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('tr', views.tr, name='tr'),
    path('submit_review/<uuid:product_uid>/', views.submit_review, name='submit_review'),  # Changed to uuid
    path('get_reviews/<uuid:product_uid>/', views.get_reviews, name='get_reviews'),        # Changed to uuid
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('prodd/<slug:product_slug>/', views.prodd, name="prodd"),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('send_confirmation_emails/', views.send_confirmation_emails, name='send_confirmation_emails'),
    # Other URLs...
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('accounts/',include('allauth.urls')),
    

]
