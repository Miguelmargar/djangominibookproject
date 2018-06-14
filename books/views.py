from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddBookForm
from accounts.forms import UserLoginForm
from .models import Book

# Create your views here.

def book_list(request):
    if request.user.is_authenticated:
        books = Book.objects.filter(owner=request.user)
    else:
        books = []
    return render(request, 'books/list_books.html', {'books': books})

def get_index(request):

    if request.user.is_authenticated:
        books= Book.objects.filter(owner=request.user)
        return render(request, "books/index.html", {"books":books})

    books = []
    form = UserLoginForm()
    return render(request, 'books/index.html', {'form': form})
    
def add_book(request):
    if request.method=="POST":
        form = AddBookForm(request.POST, request.FILES) #this gets the info from the form
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect("/")
    else:
        form = AddBookForm()
        
    return render(request, "books/add_book.html", {"form": form})