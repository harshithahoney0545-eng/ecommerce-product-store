from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),

    path('products/', views.product_list, name='product_list'),

    path('product/<int:id>/', views.product_detail, name='product_detail'),

    path('wishlist/add/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),

     path('search/', views.search, name='search'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('surprise/', views.surprise_me, name='surprise_me'),

    

path('api/update/<int:id>/', views.api_update_product, name='api_update_product'),

path('api/delete/<int:id>/', views.api_delete_product, name='api_delete_product'),

]