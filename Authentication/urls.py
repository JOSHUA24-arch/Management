
from django.urls import path
from . import views
from .views import UserRegister
app_name = 'authenticate'
urlpatterns = [
    path('register', UserRegister.as_view(), name="register"),
    path('login', views.login, name="login"),
]