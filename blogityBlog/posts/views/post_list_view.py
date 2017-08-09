from ..models.posts import Posts
from django.views.generic.list import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from ..models.category import Category


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
        if title is None:
            title = ''
        if title != '' or title != ' ':
            object_list = Posts.objects.filter(Q(title__icontains=title) | Q(subheading__icontains=title) | Q(content__icontains=title)).order_by('-publish')
        else:
            object_list = Posts.objects.all().order_by('-publish')
        return object_list

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        print("listview context keys: {}".format(context.keys()))
        for key, value in context.items():
            print("{}: {}".format(key, value))
        context['object_list'].category = Category.objects.all()
        return context
