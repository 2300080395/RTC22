from django.urls import path, include
from . import views
app_name='user_app'
urlpatterns = [
    path('',views.UserHomePage, name="userhome"),

]
