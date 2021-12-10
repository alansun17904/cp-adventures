import writeups.views as views
from django.urls import path

app_name = 'writeups'

urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('posts/add', views.PostCreateView.as_view(), name='add'),
    path('posts/edit/<int:pk>', views.PostUpdateView.as_view(), name='edit'),
    path('posts/detail/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path('posts/delete/<int:pk>', views.PostDeleteView.as_view(), name='delete'),
    path('login', views.UserLoginView.as_view(), name='login')
]
