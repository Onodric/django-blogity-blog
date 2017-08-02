from ..models.posts import Posts
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, UpdateView):
    """
    View for editing a specific post

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_update.html'
    fields = [
        'title',
        'draft',
        'publish',
        'subheading',
        'image',
        'author',
        'content',
        'location',
    ]
    success_message = "Post successfully UPDATED"
    permission_required = 'posts.post.can_change_posts'

    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={'slug': self.object.slug})
