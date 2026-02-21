from django.urls import path
from .views import HomePageView, AboutPageView, BlogPageView

# URL patterns for the pages app
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),  # Root URL
    path("about/", AboutPageView.as_view(), name="about"),  # About page URL
    path("blog/", BlogPageView.as_view(), name="blog"),  # Blog page URL
]