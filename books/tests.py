from django.test import TestCase

from .models import Book


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python & Django",
            author="William S. Vincent",
            isbn="1093633948",
        )

    def test_title_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.title}"
        self.assertEqual(expected_object_name, "Django for APIs")

    def test_subtitle_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.subtitle}"
        self.assertEqual(
            expected_object_name, "Build web APIs with Python & Django"
        )

    def test_author_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.author}"
        self.assertEqual(expected_object_name, "William S. Vincent")

    def test_isbn_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f"{book.isbn}"
        self.assertEqual(expected_object_name, "1093633948")
