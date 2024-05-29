from django import forms
from .models import Book2

class BookForm(forms.ModelForm):
    content = forms.JSONField(required=False)
    
    class Meta:
        model = Book2
        fields = '__all__'