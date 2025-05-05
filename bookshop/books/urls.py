from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book_order_success/', views.book_order_success, name='book_order_success'),
    path('books/', views.books, name='books'),
]