from ..models.posts import Posts
from django.views.generic.detail import DetailView


class PostDetailView(DetailView):
    """
    View for displaying the post details

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_detail.html'

