from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Posts(models.Model):
    """
    Post table representing a blog post, created by a specific user

    Attributes:
        Title: the name of the post (headline
        Subheading: a subheading for the article
        Content: the contents of the field. This will be populated with
            markdown converted text
        Author: A user byline, probably just one.
        Location: The location for the filing
        Created: The on-creation date and time, using UTC.
        Updated: The last modified date, in UTC.
    """

    class Meta:
        verbose_name_plural = 'posts'

    title = models.CharField(max_length=120, blank=False)
    subheading = models.CharField(max_length=180)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               default="bdmarks4")
    location = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        """
        The string representation method for a single Post
        :return:
        """
        return '{0}, by {1} {2}'.format(self.title, self.author.first_name,
                                        self.author.last_name)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
