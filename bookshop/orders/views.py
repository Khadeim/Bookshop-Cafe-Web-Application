from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from .models import Order
from django.http import HttpResponse

def orders(request):
    orders = Order.objects.all()
    order_details = ", ".join([f"Order {order.id} by {order.customer_name}" for order in orders])
    return HttpResponse(f"Orders: {order_details}")

@login_required
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Link the order to the logged-in user
            order.save()
            form.save_m2m()  # Save fields like books and menu items
            return redirect('book_order_success')  
    else:
        form = OrderForm()

    return render(request, 'orders/create_order.html', {'form': form})