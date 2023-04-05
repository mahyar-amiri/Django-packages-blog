from django.urls import path

from .views import HomeView, ArticleView, SignUp, Login, Logout, UserView

app_name = 'blog'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
    path('profile/', UserView.as_view(), name='profile'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]
