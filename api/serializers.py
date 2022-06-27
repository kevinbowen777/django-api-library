from books.models import Book
from django.contrib.auth import get_user_model  # noqa:F401
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "title", "subtitle", "author", "isbn")
