from django.http import HttpResponse
from .models import Order

def orders(request):
    orders = Order.objects.all()
    order_details = ", ".join([f"Order {order.id} by {order.customer_name}" for order in orders])
    return HttpResponse(f"Orders: {order_details}")