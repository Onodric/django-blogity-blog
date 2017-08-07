from ..models.posts import Posts
from django.views.generic.list import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

class PostListView(ListView):
    """
    View for displaying the post lists

    Author: Ben Marks
    """

    model = Posts
    template_name = 'blogityBlog/post_list.html'
    context_object_name = "posts"
    paginate_by = 10
    # queryset = Posts.objects.all().order_by('-publish')

    def get_latest(self):
        return Posts.objects.order_by('-publish').first()

    def get_queryset(self):
        title = self.request.GET.get('searcher')
        print('title: {}'.format(title))
        if title is None:
            title = ''
        if title != '' or title != ' ':
            object_list = Posts.objects.filter(Q(title__icontains=title) | Q(subheading__icontains=title) | Q(content__icontains=title)).order_by('-publish')
        else:
            object_list = Posts.objects.all().order_by('-publish')
        print("object: {}".format(object_list))
        return object_list
