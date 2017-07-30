from ..models.posts import Post
from django.views.generic.base import TemplateView


class PostDetailView(TemplateView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    template_name = 'blogityBlog/post_detail.html'
    model = Post
