from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.addExp, name="addExp"),
    path('add2/', views.addExp2, name="addExp2"),
    path('note/<str:notification>', views.home, name="notification"),
]
