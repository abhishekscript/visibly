
from django.urls import path

from account import views

urlpatterns = [
    path('user/signup', views.UserSignUp.as_view(), name='user_singup'),
    path('user/signin', views.UserSignIn.as_view(), name='user_signin'),
    path('user/social/facebook', views.FacebookUserSetup.as_view(), name='facebook_user_setup'),
    path('user/social/google', views.GoogleUserSetup.as_view(), name='google_user_setup'),
    path('user/test', views.TestPayment.as_view(), name='payments_razorpay')
]
