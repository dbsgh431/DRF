from .views import HelloAPI, bookAPI, booksAPI,BookAPIMixins,BooksAPIMixins
from django.urls import path,include


urlpatterns = [
    path('hello/', HelloAPI),
    path('fbv/books/',booksAPI),
    path('fbv/book/<int:bid>',bookAPI),
    path('mixin/books/',BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>',BookAPIMixins.as_view()),

]