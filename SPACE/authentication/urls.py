from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('signup_organization',views.signup_organization,name="signup_organization"),
    path('signup_freelance_teacher',views.signup_freelance_teacher,name="signup_freelance_teacher"),
    path('signup_student',views.signup_student,name="signup_student"),
    path('Org_login_page',views.Org_login_page,name="Org_login_page"),
    path('Flt_login_page',views.Flt_login_page,name="Flt_login_page"),
    path('Student_login_page',views.Student_login_page,name="Student_login_page"),
    path('Prg_login_page',views.Prg_login_page,name="Prg_login_page"),
    path('Dept_login_page',views.Dept_login_page,name="Dept_login_page"),
    path('vision',views.vision,name="vision")

]