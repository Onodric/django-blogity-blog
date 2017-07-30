from django.conf.urls import url
from .views.post_list_view import PostListView
from .views.post_create_view import PostCreateView
from .views.post_update_view import PostUpdateView
from .views.post_delete_view import PostDeleteView
from .views.post_detail_view import PostDetailView

app_name = 'posts'
urlpatterns = [
    url(r'^list/', PostListView.as_view(), name='post_list'),
    url(r'^create/', PostCreateView.as_view(), name='post_create'),
    url(r'^update/', PostUpdateView.as_view(), name='post_update'),
    url(r'^delete/', PostDeleteView.as_view(), name='post_delete'),
    url(r'^detail/(?P<pk>[0-9]+)/$', PostDetailView.as_view(),
        name='post_detail'),
]

