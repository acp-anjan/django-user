from django.urls import path
from app_user import views

app_name = 'app_user'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registration, name='register'),
    path('login/', views.u_login, name='u_login'),
    path('logout/', views.u_logout, name='u_logout'),
    path('special/', views.special, name='special'),
]
