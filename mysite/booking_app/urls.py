from django.urls import path, include
from pytz import country_names

from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'review', ReviewViewSet, basename='reviews')
router.register(r'booking', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path('hotels/', HotelListAPIView.as_view(), name='hotel_list'),
    path('hotels/<int:pk>/', HotelDetailAPIView.as_view(), name='hotel_detail'),
    path('rooms', RoomListAPIView.as_view(), name='room_list'),
    path('rooms/<int:pk>', RoomDetailAPIView.as_view(), name='room_detail'),
    path('hotel/create/',HotelCreateAPIView.as_view(), name='hotel_create'),
    path('country/', CountryListAPIVew.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIew.as_view(), name='country_detail'),
    path('user/', UserProfileListAPIVew.as_view(), name='user_list')
]
