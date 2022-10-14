from django.urls import path
from .import views

urlpatterns = [
    path('',views.register,name='register'),
    path('sign_up',views.sign_up,name='sign_up'),
    path('load_loginpage',views.load_loginpage,name='load_loginpage'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('load_admin_home',views.load_admin_home,name='load_admin_home'),
    path('load_welcome_page',views.load_welcome_page,name='load_welcome_page'),
    path('admin_details/<int:pk>',views.admin_details,name='admin_details'),
    path('logout/',views.logout,name="logout"),
    path('profile/', views.profile, name='profile'),
    path('course1/',views.course1,name='course1'),
    path('student1/',views.student1,name='student1'),
    path('add_student/',views.add_student,name="add_student"),
    path('add_course/',views.add_course,name="add_course"),
    path('show_student_details/',views.show_student_details,name="show_student_details"),
    path('show_student_details2/',views.show_student_details2,name="show_student_details2"),
    path('welcomeadmin/',views.welcomeadmin,name="welcomeadmin"),
    path('edit_tutor/',views.edit_tutor,name="edit_tutor"),
    path('update_tutor/',views.update_tutor,name="update_tutor"),
    path('delete_tutor/<int:pk>',views.delete_tutor,name="delete_tutor"),
    path('delete_std/<int:pk>',views.delete_std,name="delete_std"),
    path('edit_std/<int:pk>',views.edit_std,name="edit_std"),


]