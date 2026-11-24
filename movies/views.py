from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Movie
from .forms import ReviewForm

def list(request):
    """Главная страница — только список фильмов"""
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies': movies})

def detail(request, pk):
    """Страница фильма с отзывами и формой"""
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()
    avg_rating = movie.get_average_rating()
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            messages.success(request, '✅ Спасибо за ваш отзыв!')
            return redirect('detail', pk=pk)
        else:
            messages.error(request, '❌ Пожалуйста, исправьте ошибки в форме.')
    
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form,
        'avg_rating': avg_rating
    })

def add_review(request, pk):
    """Отдельный view для добавления отзыва"""
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.save()
            messages.success(request, '✅ Отзыв добавлен!')
            return redirect('detail', pk=pk)
    return redirect('detail', pk=pk)