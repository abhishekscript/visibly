'''
from django.urls import path

from user_app import views

urlpatterns = [
    path('setup/', views.UserApplicationView.as_view(), name='user_app_setup'),
]
'''
from django.urls import path
from rest_framework import routers
from user_app import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'post', views.UserApplicationView, basename='userapplication')

urlpatterns = router.urls