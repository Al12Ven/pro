from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'score']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Напишите ваш отзыв...'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }