from django.urls import path
from .views import ListBooksView


urlpatterns = [
    path('', ListBooksView.as_view(), name="songs-all")
]