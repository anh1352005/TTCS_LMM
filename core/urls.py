from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserView,RegisterView,LoginView

router=DefaultRouter()
router.register(r'users',UserView)

urlpatterns=[
    path('',include(router.urls)),
    path('auth/register/',RegisterView.as_view(),name='register'),
    path('auth/login/',LoginView.as_view(),name='login'),
]