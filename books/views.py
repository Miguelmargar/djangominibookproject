from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddBookForm
from accounts.forms import UserLoginForm

# Create your views here.

def get_index(request):
    form = UserLoginForm()
    return render(request, "books/index.html", {'form':form})
    
def add_book(request):
    form = AddBookForm()
    return render(request, "books/add_book.html", {"form": form})