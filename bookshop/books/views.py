from django.shortcuts import render, redirect
from .models import Book
from .forms import BookOrderForm

def book_list(request):
    books = Book.objects.all()

    if request.method == 'POST':
        form = BookOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_order_success')  # Redirect to a success page
    else:
        form = BookOrderForm()

    return render(request, 'books/book_list.html', {'books': books, 'form': form})

def book_order_success(request):
    return render(request, 'books/book_order_success.html')

def books(request):
    books = Book.objects.all()
    book_titles = ", ".join([book.title for book in books])
    return HttpResponse(f"Books: {book_titles}")