from django.urls import path

from . import views
urlpatterns = [
    path('orders/add-to-wishlist/', views.AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('orders/remove-from-wishlist/', views.RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),
    path('orders/check-wishlist/', views.CheckWishlistView.as_view(), name='check_wishlist'),
    path('orders/add-to-cart/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('orders/remove-from-cart/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('orders/check-cart/', views.CheckCartView.as_view(), name='check_cart'),
]
