from django.urls import path
from .views import home

app_name = "recipes"

# I want to have a custom homepage instead of the default Django welcome page when \
# 'http://127.0.0.1:8000/' is visited. Since nothing is written after the main \
# 'http://127.0.0.1:8000/' URL, the route parameter is currently empty '', in (path('', ...)).
# This specifies that when “http://127.0.0.1:8000/” is visited, you’ll see the page specified by \
# home, rather than the default Django welcome page.
urlpatterns = [
    path("", home),
]
