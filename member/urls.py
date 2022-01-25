from django.urls import path
from . import views

app_name = 'member'
urlpatterns = [
    path('signup/', views.signup_custom, name='signup'),
    path('login/', views.login_custom, name='login'),
    path('logout/', views.logout_custom, name='logout'),
]