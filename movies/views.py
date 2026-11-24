from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .forms import ReviewForm

def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {'movies': movies})

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()
    form = ReviewForm()
    
    # Получаем средний рейтинг (мы написали метод в модели)
    avg_rating = movie.get_average_rating()
    
    return render(request, 'movies/detail.html', {
        'movie': movie,
        'reviews': reviews,
        'form': form,
        'avg_rating': avg_rating
    })

def add_review(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie # Привязываем отзыв к фильму
            review.save()
            return redirect('detail', pk=pk)
    return redirect('detail', pk=pk)