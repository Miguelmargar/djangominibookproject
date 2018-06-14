from django import forms
from .models import Book

#this links the model Book and creates a form, so if you add or delete anything in models Book it will change here too - it lists the model fields
class AddBookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=["name", "author", "isbn", "notes", "image"]
        
