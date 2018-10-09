from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from prices.serializers import PricesSerializer


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def upload_prices(request):
    serializer = PricesSerializer(data=request.FILES['schema'])
    print(serializer.is_valid())
    return Response({"message": "OK"})
