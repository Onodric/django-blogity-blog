from ..models.posts import Posts
from django.views.generic.list import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class PostListView(ListView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_list.html'
    context_object_name = "posts"
    paginate_by = 3
    queryset = Posts.objects.all().order_by('-created')

    def get_latest(self):
        return Posts.objects.order_by('-created').first()
