from django.contrib import admin
from django.urls import path, include, HomeView, DishDetailView, add_review, add_to_cart, OrderCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),
    path('', HomeView.as_view(), name='home'),
    path('dish/<int:pk>/', DishDetailView.as_view(), name='dish_detail'),
    path('dish/<int:dish_id>/review/', add_review, name='add_review'),
    path('cart/add/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('order/', OrderCreateView.as_view(), name='order_form'),
]