from rest_framework import routers

from .resources.agency import AgencyViewSet
from .resources.route import RouteViewSet
from .resources.schedule import ScheduleViewSet
from .resources.message import MessageViewSet


router = routers.DefaultRouter()

router.register('agency', AgencyViewSet, base_name='agency')
router.register('route', RouteViewSet, base_name='route')
router.register('schedule', ScheduleViewSet, base_name='schedule')
router.register('message', MessageViewSet, base_name='message')


urlpatterns = router.urls

