from django.urls import path, include
from . import views


urlpatterns = [
        path('', views.BookList.as_view(), name='book_list'),
        path('<int:pk>/detail/', views.BookDetail.as_view(), name='book_detail'),
        path('<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
        path('update/', views.NewBook.as_view(), name='book_Update'),
        path('<int:pk>/edit/', views.EditBook.as_view(), name='book_edit'),

]
