from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from ..models import Contacts
from ..serialisers import  ContactDetailSerializer

class ContactDetailView(APIView):
    permission_classes = [IsAuthenticated] 
   
    def get(self, request, contact_id):
        try:
            contact = Contacts.objects.get(pk=contact_id)
            result = ContactDetailSerializer(contact)
            if contact.is_registered :
                result.data['email'] = contact.email

            
        except Contacts.DoesNotExist:
            return Response({'status': False, 'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
        




