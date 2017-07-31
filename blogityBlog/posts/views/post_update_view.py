from ..models.posts import Posts
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class PostUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    View for editing a specific post

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_update.html'
    fields = [
        'title',
        'subheading',
        'image',
        'author',
        'content',
        'location',
    ]

    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={'pk': self.object.id})

    success_message = "Post successfully UPDATED"
