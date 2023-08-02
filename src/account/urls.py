from django.urls import path
from .views import SignupView, LoginView, UserLogout, ResetPasswordView, OTPVerificationView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('signup/', SignupView.as_view(), name='signup'),

    path('logout/',UserLogout, name='user_logout'),

    path('reset-password/',ResetPasswordView.as_view(), name="reset_password"),
    
    path('otp-verification/<str:otp_token>', OTPVerificationView.as_view(), name='otp_verification'),
]