from rest_framework import serializers
from DBs.models import Person, Car


class PersonSerializer(serializers.ModelSerializer):

    owned = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='car-detail'
    )

    class Meta:
        model = Person
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
