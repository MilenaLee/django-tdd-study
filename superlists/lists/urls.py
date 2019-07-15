from django.contrib import admin
from django.urls import path
from lists.views import view_list, add_item, new_list

urlpatterns = [
    path("<int:pk>/", view_list, name="view_list"),
    path("<int:pk>/add_item", add_item, name='add_item'),
    path("new", new_list, name="new_list"),
]
