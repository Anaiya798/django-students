from django.urls import path
from .views import show_statistics, hello
urlpatterns = [
    path('analytics/', show_statistics),
    path('', hello),
]
