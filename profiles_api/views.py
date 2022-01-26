from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEst API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = {
            'Uses HTTP methos as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your aplication logic',
            'Is mapped manually to URLs',
        }


        return Response({'message': 'Pollo!', 'an_apiview': an_apiview})