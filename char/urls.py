from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.addExp, name="addExp"),
    path('note/<str:notification>', views.home, name="notification"),
]
