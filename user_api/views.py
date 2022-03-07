from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        token= Token.objects.create(user=user)
        data = serializer.data
        data['token'] = token.key
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "created successfully", "details": data}, status=status.HTTP_201_CREATED, headers=headers)
  
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)
    
class LoginView(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = LoginSerializer

        def post(self, request, format=None):
            # data = request.data
            serializer = self.get_serializer(data=request.data)
            username = data.get('username', None)
            password = data.get('password', None)
            token= Token.objects.create(user=user)
            data = serializer.data
            data['token'] = token.key
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                 return Response(status=status.HTTP_404_NOT_FOUND)