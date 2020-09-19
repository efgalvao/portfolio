from django.urls import path
from . import views


urlpatterns = [
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("project/", views.project_index, name="project_index"),
    path("project/<int:pk>", views.project_detail, name="project_detail"),

]
