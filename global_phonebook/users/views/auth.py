
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from ..serialiser import UserSerializer, TokenResponseSerializer, LoginResponseSerializer
from ..models import User

class RegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response = TokenResponseSerializer({
                'status': True,
                'token': str(refresh.access_token),
            })

            return Response(response.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = TokenResponseSerializer({
                'status': False,
                'error': str(e),
            })
            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                response = LoginResponseSerializer({
                    'status': False,
                    'error': 'Wrong password',
                })
                return Response(response.data, status=status.HTTP_401_UNAUTHORIZED)


            refresh = RefreshToken.for_user(user)
            response = LoginResponseSerializer({
                'status': True,
                'token': str(refresh.access_token),
            })

            return Response(response.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = LoginResponseSerializer({
                'status': False,
                'error': str(e),
            })
            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]  # Requires JWT authentication

    def get(self, request, user_id):
        try:
            user = User.objects.get(pk=user_id)  
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        serializer.data['id'] = user.id 
        return Response(serializer.data, status=status.HTTP_200_OK)