from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register_page,name='register'),
    path('login/',views.login_page,name='login'),
]
