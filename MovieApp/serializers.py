# from rest_framework import serializers
# from .models import Director, Movie, Review
#
#
# class DirectorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Director
#         #fields = '__all__'
#         #fields = 'id name rating __str__'.split()
#         #exclude = 'id'.split()
#         fields = 'id name rating'.split()
#
#
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ['id', 'title', 'description', 'duration', 'director', 'average_rating']
#
#     def get_average_rating(self, obj):
#         return obj.average_rating()
#
# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'text', 'movie', 'stars', 'director']
#         depth = 1
#         # fields = 'id title text price rating __str__'.split()
#         # exclude = 'id'.split()
#         # fields = ['id', 'title', 'rating']

#======================================================================================

from rest_framework import serializers
from .models import Director, Movie, Review, STAR_CHOICES, Category


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name', 'category']

    def validate_name(self, value):
        if not value or len(value) < 1:
            raise serializers.ValidationError("Name is required and cannot be empty.")
        return value

    def validate_category(self, value):
        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Category does not exist.")
        return value

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'genre', 'tags', 'is_active', 'created', 'updated']

    def validate_title(self, value):
        if not value or len(value) < 1:
            raise serializers.ValidationError("Title is required and cannot be empty.")
        return value

    def validate_duration(self, value):
        if value <= 0:
            raise serializers.ValidationError("Duration must be greater than zero.")
        return value

    def validate_director(self, value):
        if not Director.objects.filter(id=value).exists():
            raise serializers.ValidationError("Director does not exist.")
        return value

    def validate_genre(self, value):
        if value and not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Genre does not exist.")
        return value

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'movie', 'stars', 'review_is_active', 'review_created', 'review_updated']

    def validate_text(self, value):
        if not value or len(value) < 1:
            raise serializers.ValidationError("Review text is required and cannot be empty.")
        return value

    def validate_movie(self, value):
        if not Movie.objects.filter(id=value).exists():
            raise serializers.ValidationError("Movie does not exist.")
        return value

    def validate_stars(self, value):
        if value not in dict(STAR_CHOICES).keys():
            raise serializers.ValidationError("Invalid number of stars.")
        return value