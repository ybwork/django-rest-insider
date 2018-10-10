from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from prices.serializers import PricesSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
# @parser_classes((FileUploadParser,))
def upload_prices(request):
    serializer = PricesSerializer(data=request.data)

    if serializer.is_valid():
        response = {'message': 'ok'}
        status = 200
    else:
        response = serializer.errors
        status = 400

    return Response(response, status=status)
