from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("list/", PostListView.as_view(), name="post_list_list"),
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name="post_detail_detail"),
    path("create/", PostCreateView.as_view(), name="post_create"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>/", PostDeleteView.as_view(), name="post_delete"),
]
