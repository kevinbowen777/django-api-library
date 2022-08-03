from books.models import Book
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .serializers import BookSerializer, UserSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_class = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
