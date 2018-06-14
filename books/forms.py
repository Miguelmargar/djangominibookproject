from django import forms
from .models import Book

#this links the model Book and creates a form, so if you add or delete anything in models Book it will change here too - it lists the model fields
class AddBookForm(forms.ModelForm): # AddBookForm class is linked with the model  Book with forms.ModelForm and model=Book
    class Meta:
        model=Book
        fields=["name", "author", "isbn", "notes", "image"]
        
