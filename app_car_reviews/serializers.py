from rest_framework import serializers
from .models import Country, Manufacturer, Car, Reviews


class CommentCountSerializer(serializers.Serializer):
    car = serializers.IntegerField()
    comment = serializers.IntegerField()
    car__manufacturer_id = serializers.IntegerField()


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ['name', 'manufacturers']


class CarSerializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Car
        depth = 1
        fields = ['name', 'manufacturer', 'release_year', 'end_year', 'reviews']


class Car2Serializer(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['name', 'reviews']


class ReviewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['author_email', 'car', 'date_of_creation', 'comment']


class ManufacturerSerializer(serializers.ModelSerializer):
    cars = Car2Serializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        depth = 1
        fields = ['name', 'country', 'cars']
