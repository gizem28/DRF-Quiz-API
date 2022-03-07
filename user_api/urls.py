from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from .views import  logout_view, RegisterView, LoginView # ,registration_view
from rest_framework.authtoken import views

urlpatterns = [
    # path('auth/', include('dj_rest_auth.urls')),
    # path('login/', views.obtain_auth_token, name='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]