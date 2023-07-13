from django.urls import path
from .views import *


app_name = "item"

urlpatterns = [
    path("new/", new, name="new"),
    path("<int:pk>/", detail, name="detail"),
]
