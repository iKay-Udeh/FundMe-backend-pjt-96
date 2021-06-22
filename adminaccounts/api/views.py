from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

#from adminaccounts.models import AdminAccount

from .serializers import AdminAccountSerializer

@api_view(['POST', ])

def registration_view(request):
    serializer = AdminAccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        admin_account = serializer.save()
        data['response'] = 'successful'
        data['email'] = admin_account.email
        data['username'] = admin_account.username
    else:
        data = serializer.errors
    return Response(data)