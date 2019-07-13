from django.contrib import admin
from django.urls import path
from lists.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
    path('admin/', admin.site.urls),
]
