from rest_framework import serializers
from DBs.models import Person, Car


class PersonSerializer(serializers.ModelSerializer):

    owned_car_name = serializers.CharField(source='owned.name', read_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
