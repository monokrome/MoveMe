from rest_framework import routers
from .resources.agency import AgencyViewSet

router = routers.DefaultRouter()

router.register(
    'agency',
    AgencyViewSet,
    base_name='agency'
)

urlpatterns = router.urls

