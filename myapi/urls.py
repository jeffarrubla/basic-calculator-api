from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('calculations', views.CalculationsViewSet, basename='calculations')

urlpatterns = [
	path('', include(router.urls))
]