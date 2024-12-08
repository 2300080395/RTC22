from django.urls import path, include
from . import views
app_name='manager_app'
urlpatterns = [
    path('',views.managerhomepage, name="managerhome"),

]
