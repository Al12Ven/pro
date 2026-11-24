from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название фильма")
    description = models.TextField(verbose_name="Описание")
    year = models.IntegerField(verbose_name="Год выпуска")
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name="Жанр")
    
   
    poster = models.ImageField(upload_to='posters/', verbose_name="Постер фильма")
    
    created_at = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['-year'] # Сначала новые

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def get_average_rating(self):
        """Считает средний рейтинг из отзывов"""
        reviews = self.reviews.all()
        if reviews:
            total = sum([review.score for review in reviews])
            return round(total / len(reviews), 1)
        return 0.0

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews', verbose_name="Фильм")
    author = models.CharField(max_length=100, verbose_name="Имя автора")
    text = models.TextField(verbose_name="Текст отзыва")
    score = models.IntegerField(choices=[(i, i) for i in range(1, 11)], verbose_name="Оценка (1-10)")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Отзыв от {self.author} к {self.movie.title}"