from django.urls import path
from .views import *

urlpatterns = [
    path("",feedback_create, name="feedback_create"),
] 