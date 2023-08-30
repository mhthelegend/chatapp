from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import View


class ChatView(View):
    def get(self, request):
        users = User.objects.all()
        context = {
            'users': users
        }
        return render(request, "chat.html", context)