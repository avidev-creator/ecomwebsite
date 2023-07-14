from django.urls import path
from .views import *


app_name = "item"

urlpatterns = [
    path("", items, name="items"),
    path("new/", new, name="new"),
    path("<int:pk>/", detail, name="detail"),
    path("<int:pk>/delete/", delete, name="delete"),
    path("<int:pk>/edit/", edit, name="edit"),
]
