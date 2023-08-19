from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ..models import Book


class BookTests(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = get_user_model().objects.create_user(
            username="leopoldbloom",
            email="leopoldbloom@example.com",
            password="secret",
        )

        self.book = Book.objects.create(
            title="A good title",
            subtitle="A tale of wonderful things",
            author=self.user,
        )

        self.book2 = Book.objects.create(
            title="A good second title",
            subtitle="Nice subtitle for a second book",
            author=self.user,
        )

    def test___str__(self):
        assert self.book.__str__() == self.book.title
        assert str(self.book) == self.book.title

    def test_book_content(self):
        self.assertEqual(f"{self.book.title}", "A good title")
        self.assertEqual(f"{self.book.author}", "leopoldbloom")
        self.assertEqual(f"{self.book.subtitle}", "A tale of wonderful things")

    """
    def test_get_absolute_url(self):
        self.assertEqual(
            self.book.get_absolute_url(), f"/books/{self.book.id}/"
        )
    """

    def test_book_detail_view(self):
        self.client.login(email="leopoldbloom@example.com", password="secret")
        response = self.client.get(f"/api/v1/{self.book.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A good title")


class BookListViewTest(TestCase):
    def setUp(self):
        url = reverse("booklist")
        self.response = self.client.get(url)

        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe@example.com",
            password="secret",
        )

        self.book = Book.objects.create(
            title="A good title",
            subtitle="A tale of wonderful things",
            # slug="a-good-title",
            author=self.user,
        )

    def test_view_url_exists_at_desired_location(self):
        # response = self.client.get("/books/")
        self.assertEqual(self.response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.assertEqual(self.response.status_code, 200)


"""
class SitemapTests(TestCase):
    def setUp(self):
        # url = reverse("sitemap")
        url = "/sitemap.xml"
        self.response = self.client.get(url)

    def test_view_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)


class RSSFeedTests(TestCase):
    def setUp(self):
        url = reverse("book_feed")
        self.response = self.client.get(url)

    def test_feed_url_exists_at_desired_location(self):
        self.assertEqual(self.response.status_code, 200)
"""
