from ..models.posts import Posts
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_create.html'
    fields = [
        'title',
        'subheading',
        'author',
        'content',
        'location',
    ]
    success_url = reverse_lazy('posts:post_list')
