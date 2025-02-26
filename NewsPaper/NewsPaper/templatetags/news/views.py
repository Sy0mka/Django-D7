from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

class NewsCreate(CreateView):
    form_class = PostForm
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'news'
        return super().form_valid(form)

class ArticleCreate(CreateView):
    form_class = PostForm
    template_name = 'news/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.post_type = 'article'
        return super().form_valid(form)

class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_edit.html'

class PostDelete(DeleteView):
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('news_list')


def news_detail():
    return None


def news_list():
    return None