from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from writeups.models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    template_name = 'writeups/writeups_list.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'writeups/writeups_detail.html'
    model = Post


class PostCreateView(CreateView, LoginRequiredMixin):
    template_name = 'writeups/writeups_add.html'
    model = Post
    fields = ('title', 'url', 'text', 'tags')


class PostUpdateView(UpdateView, LoginRequiredMixin):
    template_name = 'writeups/writeups_edit.html'
    model = Post
    fields = ('title', 'url', 'text', 'tags')


class TagCreateView(CreateView, LoginRequiredMixin):
    pass


class PostDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'writeups/writeups_delete_confirm.html'
    model = Post
    success_url = reverse_lazy('writeups:list')


class UserLoginView(LoginView):
    template_name = 'writeups/login.html'