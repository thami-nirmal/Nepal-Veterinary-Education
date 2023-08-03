from django.urls import path
from .views import (SignupView, 
                    LoginView, 
                    UserLogout, 
                    ResetPasswordView, 
                    OTPVerificationView, 
                    RenewPasswordView,
                    VerifyEmailView,
                    )

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),

    path('signup/', SignupView.as_view(), name='signup'),

    path('logout/',UserLogout, name='user_logout'),

    path('reset-password/',ResetPasswordView.as_view(), name="reset_password"),

    path('otp-verification/<str:otp_token>/<str:email>/', OTPVerificationView.as_view(), name='otp_verification'),

    path('renew-password/<str:email>/',RenewPasswordView.as_view(), name='renew_password'),

    path('verify-email/<str:email>/', VerifyEmailView.as_view(), name="verify_email"),

]