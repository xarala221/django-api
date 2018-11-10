from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class ListBooksView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer