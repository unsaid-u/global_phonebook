from django.urls import path
from .views import auth, user

# These URLs are now relative to "/user/"
urlpatterns = [
    path('login', auth.LoginView.as_view(), name='login'),
    path('register', auth.RegisterView.as_view(), name='register'),
    path('<str:user_id>', user.UserDetailView.as_view(), name='user_detail'),
]


