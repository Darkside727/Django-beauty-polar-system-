from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

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
    path("AllAppoiments", views.View_appoiment_all, name="View_appoiment_all"),
    path("View_new_appoiments", views.View_new_appoiments, name="View_new_appoiments"),
    path("View_Confrim_Appointement", views.View_Confrim_Appointement, name="View_Confrim_Appointement"),
    path("UserProfile", views.profile, name="profile"),
    path("editprofile", views.Edit_profile, name="Edit_profile"),
    path("services", views.All_services, name="All_services"),
    path("Book_appointment", views.Book_appointment, name="Book_appointment"),
    path("Appoiments", views.View_appoiments, name="View_appoiments"),
    path('RemoveAppoi(?P<int:pid>)', views.del_appoiments, name="del_appoiments"),
    path("Selected_Appointment(?P<int:pid>)", views.book_selected_appoitment, name="book_selected_appoitment"),
    path("Addservices", views.Add_service, name="Add_service"),
    path("viewService", views.view_Services, name="view_Services"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
