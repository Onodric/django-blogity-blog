from ..models.posts import Posts
from django.views.generic.list import ListView
from django.utils import timezone


class PostListView(ListView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_list.html'

    def all_posts(self, **kwargs):
        return Posts.objects.all().order_by('-created')

    def get_latest(self):
        return Posts.objects.order_by('-created')[0]
