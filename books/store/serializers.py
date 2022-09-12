from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.models import Book, UserBookRelation


class BooksSerializer(ModelSerializer):
    # likes_count = serializers.SerializerMethodField()
    annotated_likes = serializers.IntegerField(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, read_only=True)

    class Meta:
        model = Book
        # fields= '__all__'
        fields = ('id', 'name', 'price', 'author_name', 'annotated_likes', 'rating') # remove:  'likes_count',

    # def get_likes_count(self, instance):
    #     return UserBookRelation.objects.filter(book=instance, like=True).count()




class UserBookRelationSerializer(ModelSerializer):
    class Meta:
        model = UserBookRelation
        fields = ('book', 'like', 'in_bookmarks', 'rate')
