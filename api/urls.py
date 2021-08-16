from django.urls import path
from . import views
urlpatterns = [
path('', views.employee),
path('company/', views.companygeter),
path('post/', views.post),
]