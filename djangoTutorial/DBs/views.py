from DBs.serializers import PersonSerializer, CarSerializer, UserSerializer
from DBs.models import Person, Car, User
from rest_framework.viewsets import ModelViewSet


class PersonViewSets(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class CarViewSets(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class UserViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
