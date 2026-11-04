"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views.main_views import MainViews
from api.views.post_sort_view import PostsSortView
from api.views.comment_list_view import CommentListView
from api.views.like_toggle_view import PostLikeView, CommentLikeView
from django.contrib.auth import views as auth_views
from api.views.comment_create_view import CommentCreateView

urlpatterns = [
    path('', MainViews.as_view(), name='index'),
    path('posts/sort/', PostsSortView.as_view(), name='posts_sort'),
    path('posts/<int:post_id>/comments/', CommentListView.as_view(), name='post_comments'),
    path('posts/<int:post_id>/comments/add/', CommentCreateView.as_view(), name='add_post_comments'),
    path('posts/<int:post_id>/like/', PostLikeView.as_view(), name='post_like'),
    path('comments/<int:comment_id>/like/', CommentLikeView.as_view(), name='comment_like'),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
