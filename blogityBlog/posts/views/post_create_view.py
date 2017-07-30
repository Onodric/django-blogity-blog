from ..models.posts import Posts
from django.views.generic.base import TemplateView


class PostCreateView(TemplateView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    template_name = 'blogityBlog/post_create.html'

    def get_context_data(self, **kwargs):
        post_list = Posts.objects.filter(author=kwargs['pk'])
        return {'post_list': post_list}
