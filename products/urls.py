from django.urls import path
from .views import *

urlpatterns = [
    path("", products, name="products"),
    path("<int:id>/", product,name="product"),
    path("category/<int:pk>/", category ,name="category")
] 