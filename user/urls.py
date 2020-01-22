from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.RegisterUser, name='register-page'),
    path('', auth_views.LoginView.as_view(template_name='html/login.html',redirect_authenticated_user=True), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='html/logout.html'), name='logout-page'),
]
