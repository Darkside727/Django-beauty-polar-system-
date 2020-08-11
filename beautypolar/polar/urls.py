from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("login", views.loginUser, name="loginUser"),
    path("register", views.register, name="register"),
    path("admin_login", views.admin_login, name="admin_login"),
    path("admin_home", views.admin_home, name="admin_home"),
    path("logout", views.logoutUser, name="logoutUser"),
    path("UserList", views.View_user, name="View_user"),
    path('removeUserList(?P<int:pid>)', views.remove_allUser, name="remove_allUser"),
    path("requestedUser", views.View_new_user, name="View_new_user"),
    path("AssignStatus(?P<int:pid>)", views.Assign_user_status, name="Assign_user_status"),


]
