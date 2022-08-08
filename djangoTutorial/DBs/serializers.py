from rest_framework import serializers
from DBs.models import Person, Car


class PersonSerializer(serializers.ModelSerializer):

    owned = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Person
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
