from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path('sharecab1/', views.cab1, name='cab1'),
    path('all/', views.get_all_data),
    path('create/', views.post_data),
    path('all/<str:pk>/', views.get_data)
]
urlpatterns += staticfiles_urlpatterns()