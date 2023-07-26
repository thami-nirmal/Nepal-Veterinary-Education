from django.urls import path
from .views import SignupView, LoginView, UserLogout

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('signup/', SignupView.as_view(), name='signup'),

    path('logout/',UserLogout, name='user_logout')
]