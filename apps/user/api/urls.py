from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('check-phone-number/', views.UserCheckPhoneNumberApi.as_view(), name='check-phone-number'),
    path('login/', views.UserLoginApi.as_view(), name='login'),
    path('register/', views.UserRegisterApi.as_view(), name='register'),
]
