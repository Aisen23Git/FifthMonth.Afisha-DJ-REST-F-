from rest_framework import serializers
from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        #fields = '__all__'
        #fields = 'id name rating __str__'.split()
        #exclude = 'id'.split()
        fields = 'id name rating'.split()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'movie', 'stars', 'director']