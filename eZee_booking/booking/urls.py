from django.urls import path
from .views import home, review,booking

urlpatterns = [
    path('', home, name = 'home'),
    path('bookings', booking, name = 'booking'),
    path('review', review, name = 'review'),
]