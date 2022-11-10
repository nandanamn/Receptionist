from django.urls import path
from .import views

app_name = 'receptionist'

urlpatterns = [
    path('register',views.register, name="register"),
    # path('appoinment',views.appoinment, name="appoinment")
    ]