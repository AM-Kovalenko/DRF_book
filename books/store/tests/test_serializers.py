import json

from django.contrib.auth.models import User
from django.db.models import Count, Case, When, Avg
from django.test import TestCase


from store.models import Book, UserBookRelation
from store.serializers import BooksSerializer


class BookSerializersTestCase(TestCase):
    def test_ok(self):
        # self.user = User.objects.create(username='test_user_name')
        # self.client.force_login(self.user)

        user1 = User.objects.create(username='user1')
        user2 = User.objects.create(username='user2')
        user3 = User.objects.create(username='user3')

        book_1 = Book.objects.create(name='Test book1', price=25, author_name='Author 1')
        book_2 = Book.objects.create(name='Test book2', price=30, author_name='Author 2')

        UserBookRelation.objects.create(user=user1, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=user2, book=book_1, like=True, rate=5)
        UserBookRelation.objects.create(user=user3, book=book_1, like=True, rate=4)

        UserBookRelation.objects.create(user=user1, book=book_2, like=True, rate=2)
        UserBookRelation.objects.create(user=user2, book=book_2, like=True, rate=1)
        UserBookRelation.objects.create(user=user3, book=book_2, like=False)

        books = Book.objects.all().annotate(
            annotated_likes=Count(Case(When(userbookrelation__like=True, then=1))),
            rating=Avg('userbookrelation__rate')
            ).order_by('id')
        data = BooksSerializer(books, many=True).data
        # data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'Test book1',
                'price': '25.00',
                'author_name': 'Author 1',
                'annotated_likes': 3,
                'rating': '4.67'
            },
            {
                'id': book_2.id,
                'name': 'Test book2',
                'price': '30.00',
                'author_name': 'Author 2',
                'annotated_likes': 2,
                'rating': '1.50'
            },
        ]

        self.assertEqual(expected_data, data)
