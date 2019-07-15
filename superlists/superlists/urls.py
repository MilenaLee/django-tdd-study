from django.contrib import admin
from django.urls import path
from lists.views import home_page, view_list, add_item, new_list

urlpatterns = [
    path("", home_page, name="home"),
    path("lists/<int:pk>/", view_list, name="view_list"),
    path("lists/<int:pk>/add_item", add_item, name='add_item'),
    path("lists/new", new_list, name="new_list"),
    path('admin/', admin.site.urls),
]
