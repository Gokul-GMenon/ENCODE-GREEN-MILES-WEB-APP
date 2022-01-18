from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.get_all_data),
    path('create/', views.post_data),
    path('all/<str:pk>/', views.get_data)
]