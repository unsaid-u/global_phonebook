from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Contacts
from ..serialisers import  ContactSerializer

class SpamView(APIView):
    permission_classes = [IsAuthenticated] 
    def put(self, request, contact_id):

        try:
            contact = Contacts.objects.get(pk=contact_id)
        except Contacts.DoesNotExist:
            return Response({'status': False, 'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)

        contact.is_spam = True
        contact.save()

        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)   



