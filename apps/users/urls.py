from django.urls import path

from apps.users.views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
