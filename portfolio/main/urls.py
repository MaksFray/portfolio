from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.ProjectList.as_view(), name="home"),
    path("contact/", views.contact, name="contact"),
    path("project/<int:pk>/", views.ShowProject.as_view(), name="project"),
]