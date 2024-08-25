
from django.urls import path , include

from django.conf.urls.static import static
from django.conf import settings


from . import views


urlpatterns = [
    path('',views.home,name="home"),
    # path('prod', views.prod, name='prod'),
    path('tr',views.tr,name="tr"),
    path('submit_review/',views.submit_review,name="submit_review"),
    path('prodd/<slug:product_slug>/',views.prodd,name="prodd"),
    # path('categories/', views.category, name='category'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('delete_review/<int:review_id>/',views.delete_review, name='delete_review'),
    # path('search',views.search,name="search")
] 


