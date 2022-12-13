from accounts.tests.factories import UserFactory
from django.test import TestCase

from .factories import BookFactory


# from ..models import Book


class BookTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.book = BookFactory()

    def test__str__(self):
        assert self.book.__str__() == self.book.title
        assert str(self.book) == self.book.title
