from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView

from .models import Article


class HomeView(ListView):
    model = Article


class ArticleView(DetailView):
    model = Article


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:login')
    template_name = 'blog/auth/signup.html'


class Login(LoginView):
    template_name = 'blog/auth/login.html'


class Logout(LogoutView):
    next_page = 'blog:login'
