# from django.shortcuts import render
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Director, Movie, Review
# from rest_framework import status
# from django.forms import model_to_dict
# from .serializers import DirectorSerializer,  MovieSerializer, ReviewSerializer
# # Create your views here.
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_api_view(request, id):
#     try:
#         director = Director.objects.get(id=id, is_active=True)
#     except Director.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Director not found !'})
#     if request.method == 'GET':
#         data = DirectorSerializer(director).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         director.name = request.data.get('name')
#         director.category_id = request.data.get('category_id')
#         director.save()
#         return Response(data=DirectorSerializer(director).data, status = status.HTTP_201_CREATED)
#         # director.name = name
#         # director.category_id = category_id
#
#     elif request.method == 'DELETE':
#         director.is_active = False
#         director.save()
#         return Response(status = status.HTTP_204_NO_CONTENT)
#
# #================================================================
# # @api_view(http_method_names=["GET", "POST"])
# # def director_list_create_api_view(request):
# #     if request.method == 'GET':
# #         ## step 1: Collect all movies(QuerySet)
# #         MovieApp = Director.objects.select_related(
# #             'movies'
# #         ).prefetch_related(
# #             'tags',
# #             'all_reviews'
# #         ).all()
# #
# #         ## step 2: Reformat products to list of Dictonaries
# #         list_ = DirectorSerializer(instance = MovieApp, many = True).data
# #         ## step 3: Return Response/ MovieApp = Director.
# #         director = Director.objects.all()
# #     #    data = DirectorSerializer(directors, many=True).data
# #         # Добавляем количество фильмов для каждого режиссера
# #         for director_data in list_:
# #             director = Director.objects.get(id=director_data['id'])
# #             director_data['movies_count'] = director.movies.count()
# #         return Response(data = list_, status = status.HTTP_200_OK)
# #     elif request.method =='POST':
# #         #step 1: Receive data from RequestBody
# #         title = request.data.get('title')
# #         description = request.data.get('description')
# #         duration = request.data.get('duration')
# #         is_active = request.data.get('is_active')
# #         created = request.data.get('created')
# #         updated = request.data.get('updated')
# #         print(title, description,duration, is_active, created, updated)
# #         #step 2: Create movie by this data
# #         Movie = Director.objects.create(
# #             title=title,
# #             description=description,
# #             duration=duration,
# #             is_active=is_active
# #         )
# #         #step 3: Return part of movie
# #         return Response(data=DirectorSerializer(Movie).data,status=status.HTTP_201_CREATED)
# #====================================================================
#
# @api_view(http_method_names=["GET", "POST"])
# def director_list_create_api_view(request):
#     if request.method == 'GET':
#         ## step 1: Collect all movies(QuerySet)
#         MovieApp = Director.objects.select_related(
#             'name',
#             'category_id'
#         ).filter(is_active=True)
#
#         ## step 2: Reformat products to list of Dictonaries
#         list_ = DirectorSerializer(instance = MovieApp, many = True).data
#         ## step 3: Return Response/ MovieApp = Director.
#         director = Director.objects.all()
#     #    data = DirectorSerializer(directors, many=True).data
#         # Добавляем количество фильмов для каждого режиссера
#         for director_data in list_:
#             director = Director.objects.get(id=director_data['id'])
#             director_data['movies_count'] = director.movies.count()
#         return Response(data = list_, status = status.HTTP_200_OK)
#     elif request.method =='POST':
#         #step 1: Receive data from RequestBody
#         name = request.data.get('name')
#         category_id = request.data.get('category_id')
#         print(name, category_id)
#         #step 2: Create movie by this data
#         director = Director.objects.create(
#             title=name,
#             category_id=category_id
#         )
#         print(director.category_id)
#         #step 3: Return part of movie
#         return Response(data=DirectorSerializer(Director).data,status=status.HTTP_201_CREATED)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail_api_view(request, id):
#     # try:
#     #     movie = Movie.objects.get(id=id)
#     # except Movie.DoesNotExist:
#         # return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Movie not found!'})
#
#     # data = DirectorSerializer(movie).data
#     # return Response(data=data)
#
#     try:
#         movie = Movie.objects.get(id=id, is_active=True)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Movie not found !'})
#     if request.method == 'GET':
#         data = DirectorSerializer(movie).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         Movie.title = request.data.get('title')
#         Movie.description = request.data.get('description')
#         Movie.duration = request.data.get('duration')
#         Movie.is_active = request.data.get('is_active')
#         Movie.created = request.data.get('created')
#         Movie.updated = request.data.get('updated')
#         Movie.tags.set(request.data.get('tags'))
#         Movie.save()
#         return Response(data=DirectorSerializer(movie).data, status=status.HTTP_201_CREATED)
#         # director.name = name
#         # director.category_id = category_id
#
#     elif request.method == 'DELETE':
#         Movie.is_active = False
#         Movie.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# #w
#
# @api_view(['GET', 'POST'])
# def movie_list_create_api_view(request):
#
#     if request.method == 'GET':
#         ## step 1: Collect all movies(QuerySet)
#         MovieApp = Movie.objects.all(
#             'movies'
#         ).prefetch_related(
#             'tags',
#             'description'
#         ).filter(is_active=True)
#
#         ## step 2: Reformat products to list of Dictonaries
#         list = MovieSerializer(instance = MovieApp, many = True).data
#         ## step 3: Return Response/ MovieApp = Director.
#         director = Movie.objects.all()
#     #    data = DirectorSerializer(directors, many=True).data
#         # Добавляем количество фильмов для каждого режиссера
#         # for director_data in list:
#         #     director = Director.objects.get(id=director_data['id'])
#         #     director_data['movies_count'] = director.movies.count()
#         # return Response(data = list, status = status.HTTP_200_OK)
#     elif request.method =='POST':
#         #step 1: Receive data from RequestBody
#         title = request.data.get('title')
#         description = request.data.get('description')
#         duration = request.data.get('duration')
#         is_active = request.data.get('is_active')
#         created = request.data.get('created')
#         updated = request.data.get('updated')
#         # Movie.tags.set(request.data.get('tags'))
#         Movie.save()
#         #print(title, description,duration, is_active, created, updated,tags)
#         #step 2: Create movie by this data
#         movie = Movie.objects.create(
#             title =title,
#             description = description,
#             duration = duration,
#             is_active = is_active,
#             created = created,
#             updated = updated,
#             # tags = tags
#         )
#         print(movie)
#         #step 3: Return part of movie
#         return Response(data=MovieSerializer(Movie).data,status=status.HTTP_201_CREATED)
#         # return Response(data=list, status=status.HTTP_200_OK)
#
#     # movies = Movie.objects.all()
#     # serializer = MovieSerializer(MovieApp, many=True)
#     # return Response(data=serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_api_view(request, id):
#     # try:
#     #     review = Review.objects.get(id=id)
#     # except Review.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'Review not found!'})
#
#
#     try:
#         review = Review.objects.get(id=id, is_active=True)
#     except Review.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Review not found !'})
#     if request.method == 'GET':
#         data = ReviewSerializer(review).data
#         return Response(data=data)
#     elif request.method == 'PUT':
#         Review.text = request.data.get('text')
#         Review.movie = request.data.get('movie')
#         Review.stars = request.data.get('stars')
#         Review.review_is_active = request.data.get('is_active')
#         Review.review_created = request.data.get('created')
#         Review.review_updated = request.data.get('updated')
#
#         Review.save()
#         return Response(data=ReviewSerializer(review).data, status=status.HTTP_201_CREATED)
#         # director.name = name
#         # director.category_id = category_id
#
#     elif request.method == 'DELETE':
#         review.is_active = False
#         Review.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET','POST'])
# def review_list_create_api_view(request):
#     MovieApp = Review.objects.all()
#     serializer = ReviewSerializer(instance=MovieApp, many=True).data
#
#
#     if request.method == 'GET':
#         ## step 1: Collect all movies(QuerySet)
#         MovieApp = Review.objects.all(
#             'text'
#         ).prefetch_related(
#             'movies',
#             'stars'
#         ).all()
#
#         ## step 2: Reformat products to list of Dictonaries
#         serializer = ReviewSerializer(instance = MovieApp, many = True).data
#         ## step 3: Return Response/ MovieApp = Director.
#         director = Director.objects.all()
#     #    data = DirectorSerializer(directors, many=True).data
#         # Добавляем количество фильмов для каждого режиссера
#         for director_data in serializer:
#             director = Director.objects.get(id=director_data['id'])
#             director_data['movies_count'] = director.movies.count()
#         return Response(data = serializer, status = status.HTTP_200_OK)
#     elif request.method =='POST':
#         #step 1: Receive data from RequestBody
#         text = request.data.get('text')
#         movies = request.data.get('movies')
#         stars = request.data.get('stars')
#         review_is_active = request.data.get('review_is_active')
#         review_created = request.data.get('review_created')
#         review_updated = request.data.get('review_updated')
#
#         print(text, movies,stars, review_is_active, review_created, review_updated )
#         #step 2: Create movie by this data
#         review = Review.objects.create(
#             text=text,
#             movies=movies,
#             stars=stars,
#         )
#         print(review)
#         #step 3: Return part of movie
#         return Response(data=ReviewSerializer(Review).data,status=status.HTTP_201_CREATED)
#         #return Response(data=serializer, status=status.HTTP_200_OK)
#===========================================================================================

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Director, Movie, Review, SearchTag
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, TagSerializer


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'total': data,
        })


class DirectorListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = CustomPagination


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'


class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer
    pagination_class = CustomPagination


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.filter(is_active=True)
    serializer_class = MovieSerializer
    lookup_field = 'id'


class ReviewListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.filter(review_is_active=True)
    serializer_class = ReviewSerializer
    lookup_field = 'id'


class TagModelViewSet(ModelViewSet):
    queryset = SearchTag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPagination
    lookup_field = 'id'
