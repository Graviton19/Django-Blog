from django.urls import path
from . import views

urlpatterns = [
    path('BlogPosts/', views.BlogPostListCreate.as_view(), name = "blogpost-view-create"),
    path(
        'BlogPosts/<int:pk>/',
         views.BlogPostRetrieveUpdateDestroy.as_view(),
         name = 'update',
         ),
]
