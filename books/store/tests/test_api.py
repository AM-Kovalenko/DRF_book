from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BooksSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book1', price=25, author_name='Author 1')
        self.book_2 = Book.objects.create(name='Test book2', price=30, author_name='Author 2')
        self.book_3 = Book.objects.create(name='Test book2 Author 1', price=50, author_name='Author 3')

    def test_get(self):
        url = reverse('book-list')  # для списка книг 'book-list', для конкртной книги 'book-detail
        print(url)
        response = self.client.get(url)
        print(response.data)
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'Author 1'})
        serializer_data = BooksSerializer([self.book_1, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_ordering(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'ordering': 'price'})
        serializer_data = BooksSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
