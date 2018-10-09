from django.urls import path
from rest_framework import routers

from flats.views import FlatViewSet

router = routers.SimpleRouter()
router.register(r'flats', FlatViewSet)
urlpatterns = router.urls
