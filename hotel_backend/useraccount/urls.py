from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView,LogoutView,UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns=[
    path('register/',RegisterView.as_view(),name='rest_register'),
    path('login/',LoginView.as_view(),name='rest_login'),
    path('logout/',LogoutView.as_view(),name='rest_logout'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)