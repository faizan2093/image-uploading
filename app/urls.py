from django.urls import path , include
from . import views

urlpatterns = [
    path("", views.IndexPage, name="index"),
    path("upload/", views.Uploadimage, name="uploadimage"),
    path("show/", views.ImageFetch, name="show")
]
