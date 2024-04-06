from django.urls import path
from . import views

app_name= "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="entry"), #here <str:title> means title==CSS(CSS is and example) hence ine your entry function your can use title to represent the current title
    path("search/", views.search, name= "search"),
    path("newpage/", views.newpage, name="newpage"),
    path("editpage/", views.editpage, name="editpage"),
    path("save_edit/", views.save_edit, name="save_edit"),
    path("randumb/",views.randumb, name="randumb"),
]
