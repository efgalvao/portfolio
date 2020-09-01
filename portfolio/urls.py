from django.urls import path
from . import views


urlpatterns = [
    #path("", views.project_index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("project/", views.project_index, name="project_index"),
    path("project/<int:pk>", views.project_detail, name="project_detail"),

]
