from django.urls import path
from rest_framework import routers

from companies.views import CompanyViewSet, CompanyBuildingsListView

router = routers.SimpleRouter()
router.register(r'companies', CompanyViewSet)
urlpatterns = router.urls

urlpatterns.append(path('company/<int:id>/buildings/', CompanyBuildingsListView.as_view()))
