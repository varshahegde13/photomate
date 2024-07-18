from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import PhotographerViewSet, EventViewSet, BookingViewset

router = DefaultRouter()
router.register(r'photographer',PhotographerViewSet)
router.register(r'event',EventViewSet)
router.register(r'bookings',BookingViewset)

urlpatterns = [
    path('', include(router.urls)),
]
