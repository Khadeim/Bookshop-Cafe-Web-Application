from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),            # Shows list of all orders 
    path('create/', views.create_order, name='create_order'),  # New order form
    path('my-orders/', views.my_orders, name='order_history'),        # Logged-in user's order history
]