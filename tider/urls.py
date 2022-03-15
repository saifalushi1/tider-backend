from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('tider/post/', views.PostCreate.as_view(), name='PostCreate'),
    path('tider/post/<int:pk>', views.PostList.as_view(), name='PostList'),
    # path('tider/user/', views.UserCreate.as_view(), name='UserCreate'),
    # path('tider/user/<int:pk>', views.UserList.as_view(), name='UserList'),
    path('tider/comment/', views.CommentCreate.as_view(), name='CommentCreate'),
    path('tider/comment/<int:pk>', views.CommentList.as_view(), name='CommentList'),
    path('tider/Subreddit/', views.SubredditCreate.as_view(), name='SubredditCreate'),
    path('tider/Subreddit/<int:pk>', views.SubredditList.as_view(), name='SubredditList'),  
]