from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view #type:ignore

@api_view(['GET'])
def getData(request):
    person={'name':'Rushab risal','age':23}
    return Response(person)