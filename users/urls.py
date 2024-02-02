from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views


urlpatterns = [
    path("user/", views.UserView.as_view()),
    path("users/<int:user_id>/", views.UsersView.as_view()),
    path("register/", views.RegisterUserView.as_view()),
    path("token/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
