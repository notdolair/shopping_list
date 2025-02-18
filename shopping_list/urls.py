from django.contrib import admin
from django.urls import path
from mylist.views import mylist, remove_item

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mylist/", mylist, name="mylist"),
    path("remove_item/", remove_item, name="remove_item"),
]
