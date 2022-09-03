from .views import BookAPIGenerics, BooksAPIGenerics, HelloAPI, bookAPI, booksAPI,BookAPIMixins,BooksAPIMixins
from django.urls import path,include
from rest_framework import routers
from .views import BookViewSet


# urlpatterns = [
#     path('hello/', HelloAPI),
#     path('fbv/books/',booksAPI),
#     path('fbv/book/<int:bid>',bookAPI),
#     path('mixin/books/',BooksAPIMixins.as_view()),
#     path('mixin/book/<int:bid>',BookAPIMixins.as_view()),
#     path('generics/books/',BooksAPIGenerics.as_view()),
#     path('generics/book/<int:bid>',BookAPIGenerics.as_view()),

# ]

router = routers.SimpleRouter()
router.register('books',BookViewSet)

urlpatterns = router.urls