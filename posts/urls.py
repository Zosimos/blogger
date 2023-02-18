from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path("", PostListView.as_view(), name="list"),
    path("int:pk>/edit/", PostUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="delete")
]