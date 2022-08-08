from rest_framework import routers
from django.urls import path
from DBs import views


router = routers.SimpleRouter()
router.register('person', views.PersonViewSets)
router.register('car', views.CarViewSets)
router.register('user', views.UserViewSets)
urlpatterns = [
]

urlpatterns += router.urls
