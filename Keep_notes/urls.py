from django.urls import path,include
from . import views
# from .views import create_notes
urlpatterns = [
    path("create_notes/",views.create_notes,name="create_notes"),
    path("",views.bydefualt,name="bydefault"),
    path("delete/<int:Id>",views.delete,name="delete"),
    path("edit/<int:id>",views.edit,name="edit"),
    path("update/<int:Id>",views.update,name="update"),
    path("watch/", views.watch , name="watch")
]