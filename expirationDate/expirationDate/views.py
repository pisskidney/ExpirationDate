from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render


class HomePage(TemplateView):
    template_name = "homepage.html"


class LoginView(View):
    pass


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
