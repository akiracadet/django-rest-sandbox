from django.test import TestCase
from books.models import Book


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='Book Title', author='Book Title Author', isbn=('1' * 13))


    def test_title(self):
        book = Book.objects.get(id=1)
        expected = 'Book Title'

        self.assertEquals(book.title, expected)


    def test_author(self):
        book = Book.objects.get(id=1)
        expected = 'Book Title Author'

        self.assertEquals(book.author, expected)


    def test_isbn(self):
        book = Book.objects.get(id=1)
        expected = ('1' * 13)

        self.assertEquals(book.isbn, expected)
