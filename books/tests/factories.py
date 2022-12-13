from accounts.tests.factories import UserFactory
import factory
import factory.fuzzy
import pytest

from ..models import Book


@pytest.fixture
def book():
    return BookFactory()


class BookFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText(length=12, prefix="The Book of ")
    subtitle = factory.fuzzy.FuzzyText(length=15, prefix="Stories about ")
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = Book
