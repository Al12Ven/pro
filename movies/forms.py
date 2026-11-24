from django import forms
from .models import Review, Movie

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'text', 'score']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Напишите ваш отзыв...'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }

# Новая форма для главной страницы с выбором фильма
class HomeReviewForm(forms.ModelForm):
    movie = forms.ModelChoiceField(
        queryset=Movie.objects.all(),
        label="Выберите фильм",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Review
        fields = ['movie', 'author', 'text', 'score']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Напишите ваш отзыв...'}),
            'score': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 10}),
        }