import bs4
import requests

from rest_framework import viewsets
from rest_framework.response import Response


class NextBusViewSet(viewsets.ViewSet):
    """ Abstracts the NextBus API through REST Framework.

    This allows us to crate RESTful resources which represent the entities
    which are provided by the NextBus API.

    Visit http://www.nextbus.com/xmlFeedDocs/NextBusXMLFeed.pdf for
    documentation on the NextBus API itself.

    """

    endpoint = 'http://webservices.nextbus.com/service/publicXMLFeed'
    command = None

    def get_url(self, request):
        """ Get the API URL for the given resource. """

        if not isinstance(self.command, basestring):
            raise ValueError('self.command must be a string.')

        return self.endpoint + '?command=' + self.command

    def parse_tree(self, tree):
        """ Convert a BeautifulSoup object into a dictionary. """

        raise NotImplementedError(
            'parse_tree is abstract and must be overridden from {0}.'.format(
                self.__class__.__name__
            )
        )

    def parse_xml(self, xml):
        """ Parses NextBus XML data into a BeatifulSoup object. """

        soup = bs4.BeautifulSoup(xml)

        if not getattr(soup, 'body'):
            raise ValueError('Unexpected response received.')

        return self.parse_tree(soup.body)

    def list(self, request):
        nextbus_request = requests.get(self.get_url(request))

        return Response(
            self.parse_xml(nextbus_request.text),
            status=nextbus_request.status_code
        )

