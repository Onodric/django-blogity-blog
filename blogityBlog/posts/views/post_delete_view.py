from ..models.posts import Posts
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                     SuccessMessageMixin, DeleteView):
    """
    View for deleting a specific post

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_delete.html'
    permission_required = 'posts.post.can_delete_posts'
    success_message = "Post successfully DELETED"

    def get_success_url(self):
        return reverse_lazy('posts:post_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)
