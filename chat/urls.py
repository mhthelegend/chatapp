from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from chat.views import ChatView

urlpatterns = [
    path('', ChatView.as_view(), name="chat"),
]