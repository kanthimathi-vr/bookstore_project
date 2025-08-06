from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Book

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "home.html"


# 🔍 Book ListView with search, pagination, and ordering
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        queryset = Book.objects.all()
        search_query = self.request.GET.get('q')
        order_by = self.request.GET.get('order_by', 'title')  # default to title

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset.order_by(order_by)


# 📖 Book DetailView with discounted price via get_context_data
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.get_object()
        context['discounted_price'] = book.get_discounted_price()
        return context


# ✅ Admin check mixin
class AdminOnlyMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def handle_no_permission(self):
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied("Admins only")


# ➕ CreateView for adding new books (admin only)
class BookCreateView(LoginRequiredMixin, AdminOnlyMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'discount_percent']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')


# ✏️ UpdateView for editing books (admin only)
class BookUpdateView(LoginRequiredMixin, AdminOnlyMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'discount_percent']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')


# ❌ DeleteView for deleting books (admin only)
class BookDeleteView(LoginRequiredMixin, AdminOnlyMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')
