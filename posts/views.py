from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .forms import PostForm
from .mixins import SuperUserRequiredMixin
from .models import Post


class PostCreate(SuperUserRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/posts-create.html'

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts-list.html'


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/posts-detail.html'


class PostUpdate(SuperUserRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/posts-update.html'

    def get_success_url(self):
        return reverse('posts:post_detail', kwargs={'pk': self.object.pk})


class PostDelete(SuperUserRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:post_list')
    template_name = 'posts/post-delete.html'
