from .models import *
from rest_framework import serializers

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']





class RoomImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ['room_image']


class RoomListSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_status', 'room_type', 'room_price','room_images' ]


class RoomDetailSerializer(serializers.ModelSerializer):
    room_images = RoomImageSerializers(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ['room_number', 'room_status', 'room_type', 'room_price', 'all_inclusive',
                  'room_description', 'room_images']


class ReviewSerializer(serializers.ModelSerializer):
    user_name = UserProfileSimpleSerializer()

    class Meta:
        model = Review
        fields = ['user_name', 'text', 'parent', 'stars']


class HotelListSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    get_count_people = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id', 'hotel_name', 'city', 'address', 'hotel_stars', 'hotel_images', 'avg_rating',
                  'get_count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_people(self, obj):
        return obj.get_count_people()

class CountryDetailSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['country_name', 'hotels']




class HotelDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    owner = UserProfileSimpleSerializer()
    created_date = serializers.DateField(format('%d-%m-%Y'))
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    rooms = RoomListSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name','hotel_descriptions','country', 'city','hotel_images' ,
                  'hotel_video','owner','address', 'hotel_stars', 'created_date', 'rooms', 'reviews']



class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['hotel_name','hotel_descriptions','country', 'city',
                  'hotel_video','owner','address', 'hotel_stars', 'created_date']



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'