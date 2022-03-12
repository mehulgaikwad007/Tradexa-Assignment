from django.contrib import admin
from django.urls import path,include
from . import views

app_name='User'
urlpatterns = [
    path('',views.home,name='home'),
    path("register/", views.register_view, name="register_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view"),
    path("post/",views.viewpost,name="post"),
    path("create/",views.createpost,name="createpost"),
    path('post/update/<int:id>',views.updatePost,name="updatePost"),
]