from django.http import HttpResponse
from rest_framework import generics
from .models import Book 
from .serializers import BookSerializer


class BookView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
BookViewAll = BookView.as_view() 


def home(request):
    return HttpResponse("Hello, world!")
