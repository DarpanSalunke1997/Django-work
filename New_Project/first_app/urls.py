from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name=""),
    path('home/',views.Home,name=""),
    path('users/',views.User,name=""),
    path('forms/',views.form_user,name=""),
    path('model_forms/',views.Model_Form_User,name=""),
]
