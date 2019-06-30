from django.urls import path
from django.contrib.auth import views as auth_views

from twitter import views

app_name = 'twitter'

urlpatterns = [
    path('', views.MainWebPageView.as_view(), name="index"),
    path('compose/', views.TweetComposeView.as_view(), name="compose"),
    path('login/', auth_views.LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='twitter/logout.html'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('tweet/<int:pk>/', views.TweetDetailView.as_view(),
         name='tweet-detail'),
    path('user/<int:pk>/', views.AuthorDetailView.as_view(),
         name='author-detail'),
]