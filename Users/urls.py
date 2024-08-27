from django.urls import path
from Users.views import RegisterAPIView, AuthAPIView

urlpatterns = [
    path('registration/', RegisterAPIView.as_view(), name='register'),
    path('authorization/', AuthAPIView.as_view(), name='auth'),
]
