import bs4
import requests

from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from rest_framework.response import Response


class NextBusViewSet(viewsets.GenericViewSet):
    """ Abstracts the NextBus API through REST Framework.

    This allows us to crate RESTful resources which represent the entities
    which are provided by the NextBus API.

    Visit http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf for
    documentation on the NextBus API itself.

    """

    endpoint = 'http://webservices.nextbus.com/service/publicXMLFeed'
    require_agency = True
    tag_name = None

    def __init__(self, *args, **kwargs):
        if not isinstance(self.tag_name, basestring):
            raise ValueError(
                'self.command must be a string on {0}.'.format(
                    self.__class__.__name__
                )
            )

        self.retrieve_command = self.tag_name + 'Config'
        self.list_command = self.tag_name + 'List'

        return super(NextBusViewSet, self).__init__(*args, **kwargs)

    def get_url(self, request, pk=None):
        """ Get the API URL for the given resource.

        This will return a URL for the given NextBus API command. If an agency
        filter is provided, then it will also include the agency.

        A `pk` argument can be optionally provided. When provided, the URL will
        represent a detail view for an object with the given primary key.
        
        """

        if not pk:
            command = self.list_command
        else:
            command = self.retrieve_command

        url = self.endpoint + '?command=' + command
        agency = self.get_agency(request)

        if agency:
            url += '&a=' + agency

        if pk:
            url += '&r=' + pk

        print(url)

        return url

    def parse_xml(self, xml, pk=None):
        """ Parses NextBus XML data into a BeatifulSoup object.
        
        If pk is truthy, this this will return a single object. Otherwise, it
        will return a list of items.

        """

        tree = bs4.BeautifulSoup(xml, 'xml')

        if not getattr(tree, 'body'):
            raise ValueError('Unexpected response received.')

        if pk:
            results = tree.body.find(self.tag_name)
        else:
            results = tree.find_all(self.tag_name)

        return results

    def get_agency(self, request):
        if not 'agency' in request.GET:
            if self.require_agency is False:
                return None

            raise ParseError('The `agency` filter is required.')

        return request.GET.get('agency')

    def get_response(self, request, pk=None):
        url = self.get_url(request, pk)
        nextbus_request = requests.get(url)

        results = self.parse_xml(nextbus_request.text, pk)

        # This is a list view if there's no pk since POST is not allowed.
        many = pk is None
        serializer = self.get_serializer(results, many=many)

        return Response(
            serializer.data,
            status=nextbus_request.status_code
        )

class NextBusListMixin(object):
    """ Provides NextBus list views. """

    def list(self, request):
        return self.get_response(request)


class NextBusDetailMixin(object):
    """ Provides NextBus detail views.
    
    """

    def retrieve(self, request, pk=None):
        return self.get_response(request, pk)