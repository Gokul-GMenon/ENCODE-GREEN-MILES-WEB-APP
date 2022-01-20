from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.home, name='home'),
    path('sharecab1/<str:pk>/', views.cab1, name='cab1'),
    # path('loading/<str:pk>/', views.loading, name='loading'),
    path('sharecab2/<str:pk>/', views.cab2, name='cab2'),
    path('sharecab3/<str:pk>/', views.cab3, name='cab3'),
    path('add/', views.add, name='add'),
    path('profile/', views.profile, name='usp'),
    path('profile/<str:pk>/', views.profile, name='usp'),
    path('retry/<str:pk>/', views.retry, name='retry'),
]
urlpatterns += staticfiles_urlpatterns()