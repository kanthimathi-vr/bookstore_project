from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
    HomePageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('book/add/', BookCreateView.as_view(), name='book-add'),
    path('book/<int:pk>/edit/', BookUpdateView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
