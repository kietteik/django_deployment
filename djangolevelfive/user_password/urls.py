from django.urls import path
from user_password import views

app_name = 'user_password'

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('user_login/', views.user_login, name='user_login')
]
