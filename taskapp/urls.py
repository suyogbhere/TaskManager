from django.urls import path
from taskapp import views

urlpatterns = [
    path('',views.Home,name='taskmanager'),
    path("signup/",views.User_Signup,name="signup"),
    path("login/",views.Login,name="login"),
    path("logout/",views.User_logout,name="logout"),
]
