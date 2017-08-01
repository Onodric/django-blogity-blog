from ..models.posts import Posts
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, CreateView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_create.html'
    fields = [
        'title',
        'subheading',
        'image',
        'author',
        'content',
        'location',
    ]
    success_url = reverse_lazy('posts:post_list')
    success_message = "Post successfully CREATED"
    permission_required = 'posts.post.can_add_posts'
