from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('user-register/', views.UserRegister.as_view(), name='userRegister'),
    path('user-login/', views.UserLogin.as_view(), name='userLogin'),
    path('user-logout/', views.UserLogout.as_view(), name='userLogout'),
    path('user-password-update/', views.UserPasswordUpdate.as_view(), name='userPasswordUpdate'),
    path('user-verification/<pk>/', views.UserVerification.as_view(), name='userVerification')
]
