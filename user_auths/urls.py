from django.urls import path
from user_auths import views


app_name = 'userauths'

urlpatterns = [
    path('register/',views.register_view,name="register"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
]
