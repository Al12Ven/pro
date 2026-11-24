from django.contrib import admin
from .models import Genre, Movie, Review

# Inline для отзывов — позволяет редактировать отзывы прямо на странице фильма
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    fields = ('author', 'text', 'score', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
   
    list_display = ('id', 'title', 'year', 'genre', 'display_rating', 'created_at')
    list_filter = ('genre', 'year', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('year', 'genre')
    ordering = ('-year', '-created_at')
    list_per_page = 20
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'year', 'genre', 'poster')
        }),
        ('Описание', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ReviewInline]
    
    
    @admin.display(description='Рейтинг', ordering='created_at')
    def display_rating(self, obj):
        """Безопасно форматируем рейтинг в строку перед отдачей в админку"""
        rating = obj.get_average_rating()
        return f"⭐ {rating:.1f}"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'author', 'score', 'created_at')
    list_filter = ('score', 'created_at')
    search_fields = ('author', 'text', 'movie__title')
    ordering = ('-created_at',)