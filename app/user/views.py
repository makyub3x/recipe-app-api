""" Views for the User API """

from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """ Create a user in the system  """
    serializer_class = UserSerializer