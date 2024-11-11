from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .models import Session
from .views import MovieViewSet, HallViewSet, SessionViewSet, BookingViewSet, RegisterView

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/movies/', MovieViewSet.as_view(), name='get-all-movies'),
    path('api/halls/', HallViewSet.as_view(), name='get-all-halls'),
    path('api/session/', SessionViewSet.as_view(), name='get-all-session'),
    path('api/bookings/', BookingViewSet.as_view(), name='get-all-bookings'),
]