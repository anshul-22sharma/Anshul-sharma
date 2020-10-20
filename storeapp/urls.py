from django.urls import path
from storeapp import views
# from storeapp.views import Loginview
from . import views 


urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('signup/',views.signup.as_view()),
    path('login/', views.loginview.as_view()),
    
]