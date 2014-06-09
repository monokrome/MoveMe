from rest_framework import routers
from .resources.agency import AgencyViewSet
from .resources.route import RouteViewSet

router = routers.DefaultRouter()

router.register('agency', AgencyViewSet, base_name='agency')
router.register('route', RouteViewSet, base_name='route')

urlpatterns = router.urls

