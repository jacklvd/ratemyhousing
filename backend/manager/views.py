from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer
from .models import Person
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

# This class allows us to add more fields into the response
# when a user log in. By default, only the token is required
class CustomAuthToken(ObtainAuthToken):
    # This function allows us to include first_name, job_title
    # in the Response when a user logs into their account
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            display = {
                'token': token.key,
                'first_name': user.first_name,
                'job_title': user.person.job_title
            }

            return Response(display, status=status.HTTP_200_OK)

        return Response({"status":"bad request"}, status=status.HTTP_400_BAD_REQUEST)

# For the sign-in page
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # display all users (only useful for testing)
    @action(detail=False, methods=['get'])
    def users(self, request):
        users = User.objects.all()

        display = []

        for user in users:

            if user.is_superuser:
                continue

            job_title = user.person.job_title

            user_info = {
                "id": user.id,
                "first_name": user.first_name,
                "job_title": job_title,
                "username": user.username,
                "email": user.email,
            }

            display.append(user_info)

        return Response(display, status=status.HTTP_200_OK)

    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated])
    def log_out(self, request):
        request.user.auth_token.delete()
        return Response({"status":"sucessfully logged out"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def create_account(self, request):
        serializer = UserSerializer(data=request.data)

        # this line is required before acessing serialized data
        if serializer.is_valid():

            # skim thru request data and make sure it has a
            # name, job_title, username, email, and password field

            req_first_name = serializer.validated_data.get('first_name')
            try:
                job_title = request.data['job_title']
            except:
                return Response({"status":"required fields missing"}, status=status.HTTP_400_BAD_REQUEST)

            req_username = serializer.validated_data.get('username')
            req_email = serializer.validated_data.get('email')
            req_password = serializer.validated_data.get('password')

            # check that these fields are not None
            if req_first_name and req_username and req_email and req_password:

                # create new user using request data
                first_name = serializer.validated_data['first_name']
                username = serializer.validated_data['username']
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                user = User.objects.create_user(
                        first_name = first_name,
                        username = username,
                        email = email,
                        password = password
                    )

                person = Person.objects.create(
                        user = user,
                        job_title = job_title
                )

                return Response({"status":"user successfully created"}, status=status.HTTP_200_OK)

            return Response({"status":"required fields missing"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"status":"bad request"}, status=status.HTTP_400_BAD_REQUEST)

# TODO: Create API for search bar

# TODO: create Google Map api
class Rental:
    pass