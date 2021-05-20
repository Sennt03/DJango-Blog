from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_category/', views.add_categoria, name='add_categoria'),
    path('add_entrada/', views.add_entrada, name='add_entrada'),
    path('delete_article/<int:id>/', views.delete_article, name='delete_article'),
    path('edit_article/<int:id>/', views.edit_article, name="edit_article"),
    path('category/<int:id>/', views.category, name="category"),
    path('user/<int:id>', views.user, name="user")
]