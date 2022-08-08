from DBs.serializers import PersonSerializer, CarSerializer
from DBs.models import Person, Car
from rest_framework.viewsets import ModelViewSet


class PersonViewSets(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CarViewSets(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
