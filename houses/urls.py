from rest_framework import routers

from houses.views import HouseViewSet

router = routers.SimpleRouter()
router.register(r'houses', HouseViewSet)
urlpatterns = router.urls
