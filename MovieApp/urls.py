from MovieApp import views
from django.urls import path

urlpatterns = [
    path('', views.DirectorListCreateAPIView.as_view()),
    path('<int:id>/', views.director_detail_api_view),
    path('categories/', views.DirectorListAPIview.as_view()),  # get -> list, post -> create;
    path('categories/<int:id>/',
         views.DirectorDetailAPIView.as_view()),  # get->retrieve, put -> update, delete -> destroy
    path('tags/', views.TagModelViewSet.as_view({
        'get': 'list', 'post': 'create'
    })),
    path('tags/<int:id>/', views.TagModelViewSet.as_view({
        'get': 'retrieve','put':'update', 'delete': 'destroy'
    }))
]
