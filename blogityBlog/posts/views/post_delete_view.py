from ..models.posts import Post
from django.views.generic.base import TemplateView


class PostDeleteView(TemplateView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    template_name = 'blogityBlog/post_delete.html'

    def get_context_data(self, **kwargs):
        post_list = Post.objects.filter(author=kwargs['pk'])
        return {'post_list': post_list}
