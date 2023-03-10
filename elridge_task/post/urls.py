from django.urls import path
from .views import PostList, PostDetail, RegisterView, LoginView

urlpatterns = [
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]