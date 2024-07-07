from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView
from pytils.translit import slugify
from django.forms import inlineformset_factory

from blog.forms import VersionForm
from blog.models import Blog, Version


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', "price", 'preview', 'published')
    success_url = reverse_lazy('blog:list')
    permission_required = 'blog.add_blog'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Blog, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = VersionFormset(
                self.request.POST, instance=self.object
            )
        else:
            context_data["formset"] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        form.instance.owner = self.request.user

        if form.is_valid() and formset.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            return super().form_valid(form)

        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content', 'preview', 'published', "price")
    success_url = reverse_lazy('blog:list')
    permission_required = 'blog.change_blog'

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    permission_required = 'blog.delete_blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

