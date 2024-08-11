from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Director, Movie, Review
from rest_framework import status
from django.forms import model_to_dict
from .serializers import DirectorSerializer,  MovieSerializer, ReviewSerializer
# Create your views here.

@api_view(['GET'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Director not found !'})
    data = DirectorSerializer(director).data
    return Response(data=data)


@api_view(http_method_names=["GET"])
def director_list_api_view(request):
    ## step 1: Collect all movies(QuerySet)
    MovieApp = Director.objects.all()

    ## step 2: Reformat products to list of Dictonaries
    list_ = DirectorSerializer(instance = MovieApp, many = True).data
    ## step 3: Return Response/ MovieApp = Director.
    directors = Director.objects.all()
#    data = DirectorSerializer(directors, many=True).data
    # Добавляем количество фильмов для каждого режиссера
    for director_data in list_:
        director = Director.objects.get(id=director_data['id'])
        director_data['movies_count'] = director.movies.count()
    return Response(data = list_, status = status.HTTP_200_OK)


@api_view(['GET'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found!'})

    data = DirectorSerializer(movie).data
    return Response(data=data)

#w

@api_view(['GET'])
def movie_list_api_view(request):
    MovieApp = Movie.objects.all()
    list = MovieSerializer(instance=MovieApp, many=True).data
    return Response(data=list, status=status.HTTP_200_OK)


    # movies = Movie.objects.all()
    # serializer = MovieSerializer(MovieApp, many=True)
    # return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found!'})

    data = ReviewSerializer(review).data
    return Response(data=data)


@api_view(['GET'])
def review_list_api_view(request):
    MovieApp = Review.objects.all()
    serializer = ReviewSerializer(instance=MovieApp, many=True).data
    return Response(data=serializer, status=status.HTTP_200_OK)