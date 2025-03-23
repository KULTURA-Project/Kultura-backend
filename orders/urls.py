from django.urls import path
from . import views

urlpatterns = [
    # Cart URLs
    path('cart/add/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/remove/', views.RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/update/', views.UpdateCartItemView.as_view(), name='update_cart_item'),

    # Wishlist URLs
    path('wishlist/add/', views.AddToWishlistView.as_view(), name='add_to_wishlist'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/remove/', views.RemoveFromWishlistView.as_view(), name='remove_from_wishlist'),

    # Order URLs
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('create/', views.CreateOrderView.as_view(), name='create_order'),
      path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/ship/', views.ShipOrderView.as_view(), name='ship_order'),
    path('orders/<int:pk>/cancel/', views.CancelOrderView.as_view(), name='cancel_order'),

    # Coupon URLs
    path('coupons/apply/', views.ApplyCouponView.as_view(), name='apply_coupon'),

    # Checkout/Shipping URLs
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('checkout/payment/', views.ProcessPaymentView.as_view(), name='process_payment'),
]
