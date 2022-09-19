from rest_framework import generics
from django.contrib.auth.models import User

from .serializer import UserSerializer

class UserCreateView(generics.CreateAPIView):
    """
    Class-based view to list the deck collection of the current user
    or to create a new deck for the current user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = []
