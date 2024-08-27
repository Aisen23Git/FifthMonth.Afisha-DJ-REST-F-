# from MovieApp import views
# from django.urls import path
#
# urlpatterns = [
#     path('', views.DirectorListCreateAPIView.as_view()),
#     path('<int:id>/', views.director_detail_api_view),
#     path('categories/', views.DirectorListAPIview.as_view()),  # get -> list, post -> create;
#     path('categories/<int:id>/',
#          views.DirectorDetailAPIView.as_view()),  # get->retrieve, put -> update, delete -> destroy
#     path('tags/', views.TagModelViewSet.as_view({
#         'get': 'list', 'post': 'create'
#     })),
#     path('tags/<int:id>/', views.TagModelViewSet.as_view({
#         'get': 'retrieve','put':'update', 'delete': 'destroy'
#     }))
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from MovieApp import views

router = DefaultRouter()
router.register(r'tags', views.TagModelViewSet, basename='tag')

urlpatterns = [
    path('directors/', views.DirectorListCreateAPIView.as_view(), name='director-list-create'),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view(), name='director-detail'),

    path('movies/', views.MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view(), name='movie-detail'),

    path('reviews/', views.ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view(), name='review-detail'),

    path('', include(router.urls)),
]
