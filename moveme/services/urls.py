from rest_framework import routers

from .resources.agency import AgencyViewSet
from .resources.route import RouteViewSet
from .resources.schedule import ScheduleViewSet
from .resources.message import MessageViewSet
from .resources.vehicle import VehicleViewSet
from .resources.departure import DepartureViewSet


router = routers.DefaultRouter()

router.register('agency', AgencyViewSet, base_name='agency')
router.register('route', RouteViewSet, base_name='route')
router.register('schedule', ScheduleViewSet, base_name='schedule')
router.register('message', MessageViewSet, base_name='message')
router.register('vehicle', VehicleViewSet, base_name='vehicle')
router.register('departure', DepartureViewSet, base_name='departure')


urlpatterns = router.urls

