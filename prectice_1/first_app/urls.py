from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/',views.login,name='login'),
    path('djangoForm/',views.django_form_func, name ='dform'),

]