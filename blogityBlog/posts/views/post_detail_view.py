from ..models.posts import Posts
from django.views.generic.detail import DetailView
from django.utils import timezone


class PostDetailView(DetailView):
    """
    View for displaying the post details

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
