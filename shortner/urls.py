from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.shortner, name="register"),
    path("details/<str:url>/", views.url_detail, name="url detail"),

    path("disable/<str:url>/", views.url_disable, name="url disable"),
    path("enable/<str:url>/", views.url_enable, name="url enable"),
    path("delete/<str:url>/", views.url_delete, name="url delete"),


    path("<str:url>/", views.view_url, name="view"),
]
