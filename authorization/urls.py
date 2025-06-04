from django.urls import path
from authorization import views

urlpatterns = [
    path('login/', None, 'login'),
    path('register/', None, 'register'),
    path('logout/', None, 'logout'),
]
