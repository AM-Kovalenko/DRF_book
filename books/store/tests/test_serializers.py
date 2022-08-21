import json

from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Book
from store.serializers import BooksSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        self.user = User.objects.create(username='test_user_name')
        self.client.force_login(self.user)
        book_1 = Book.objects.create(name='Test book1', price=25, author_name='Author 1', owner=self.user)
        book_2 = Book.objects.create(name='Test book2', price=30, author_name='Author 2', owner=self.user)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book1',
                'price': '25.00',
                'author_name': 'Author 1',
                'owner': self.user
            },
            {
                'id': book_2.id,
                'name': 'Test book2',
                'price': '30.00',
                'author_name': 'Author 2',
                'owner': self.user
            },
        ]

        # self.assertEqual(expected_data, data)
