from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'slug', 'content', 'preview', 'created_at')
    success_url = reverse_lazy('blog:list')


class BlogListView(ListView):
    model = Blog


