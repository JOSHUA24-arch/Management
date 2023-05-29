
from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('', views.Home, name="home"),
    path('plan', views.plan, name='plan'),
    path('calculate_pension', views.calculate_pension, name='calculate_pension'),
]