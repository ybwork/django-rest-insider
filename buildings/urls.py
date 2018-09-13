from rest_framework.routers import SimpleRouter

from buildings.views import BuildingViewSet

router = SimpleRouter()
router.register(r'buildings', BuildingViewSet)
urlpatterns = router.urls