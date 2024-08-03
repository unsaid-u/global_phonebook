from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..serialiser import UserSerializer
from ..models import User

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Requires JWT authentication

    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)  
        except User.DoesNotExist:
            return Response({'status': False, 'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        serializer.data['id'] = user.id 
        return Response(serializer.data, status=status.HTTP_200_OK) 