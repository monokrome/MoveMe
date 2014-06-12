from rest_framework import routers

from .resources.agency import AgencyViewSet
from .resources.route import RouteViewSet
from .resources.schedule import ScheduleViewSet
from .resources.message import MessageViewSet
from .resources.vehicle import VehicleViewSet
from .resources.departure import DepartureViewSet
from .resources.user import UserViewSet


router = routers.DefaultRouter()

resources = {
    'agency': AgencyViewSet,
    'route': RouteViewSet,
    'schedule': ScheduleViewSet,
    'message': MessageViewSet,
    'vehicle': VehicleViewSet,
    'departure': DepartureViewSet,
    'user': UserViewSet,
}

for name in resources:
    resource = resources[name]
    router.register(name, resource, base_name=name)

urlpatterns = router.urls

