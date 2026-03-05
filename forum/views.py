from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Topic, Post
from .forms import TopicForm, PostForm
from django.utils import timezone
from datetime import timedelta


# Список тем
class TopicListView(ListView):
    model = Topic
    template_name = "forum/topic_list.html"
    context_object_name = "topics"


# Відображення теми та її постів
class TopicDetailView(DetailView):
    model = Topic
    template_name = "forum/topic_detail.html"
    context_object_name = "topic"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm()
        context['posts'] = self.object.posts.order_by('-created_at')
        return context


# Створення нової теми
class TopicCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "forum/topic_form.html"
    success_url = reverse_lazy('forum:topic_list')

    def test_func(self):
        return self.request.user.profile.role in ['admin', 'moderator']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


# Видалення повідомлення теми
class TopicDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topic
    template_name = 'forum/topic_confirm_delete.html'
    success_url = reverse_lazy('forum:topic_list')

    def test_func(self):
        return self.request.user.profile.role in ['moderator', 'admin']


# Додавання повідомлення до теми
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.topic = get_object_or_404(Topic, pk=self.kwargs['pk'])
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('forum:topic_detail', kwargs={'pk': self.kwargs['pk']})


# Редагування повідомлення теми
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "forum/post_edit.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.created_by and (timezone.now() - post.created_at) < timedelta(minutes=30):
            return True
        return self.request.user.profile.role in ['admin', 'moderator']
    
    def get_success_url(self):
        return reverse_lazy('forum:topic_detail', kwargs={'pk': self.object.topic.pk})


# Видалення повідомлення теми
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'forum/post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        # Дозволяємо видаляти автору, модераторам або адмінам
        return self.request.user == post.created_by or self.request.user.profile.role in ['moderator', 'admin']

    def get_success_url(self):
        return reverse_lazy('forum:topic_detail', kwargs={'pk': self.object.topic.pk})