from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic import ListView, DetailView

from .models import Article

User = get_user_model()


class HomeView(ListView):
    model = Article


class ArticleView(DetailView):
    model = Article


class UserView(LoginRequiredMixin, TemplateView):
    login_url = 'blog:login'
    template_name = 'blog/auth/profile.html'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:login')
    template_name = 'blog/auth/signup.html'


class Login(LoginView):
    template_name = 'blog/auth/login.html'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        else:
            return reverse_lazy('blog:profile')


class Logout(LogoutView):
    next_page = 'blog:login'


def error_404(request, exception):
    return render(request, 'blog/utils/404.html', {'exception': exception})
