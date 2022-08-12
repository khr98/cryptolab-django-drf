from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

app_name='accounts'

urlpatterns = [
    path('signup/', views.SignUpAPIView.as_view()),
    path('list/',views.ListUserView.as_view()),
    path('login/',views.LoginAPIView.as_view()),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
]