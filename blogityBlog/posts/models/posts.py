from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from .category import Category
from markdownx.utils import markdownify
from ..utils import get_read_time


def upload_location(instance, filename):
    PostModel = instance.__class__
    if PostModel.objects.order_by('id').last():
        new_id = PostModel.objects.order_by('id').last().id + 1
        return "post-{}/{}".format(new_id, filename)
    else:
        return "post-{}/{}".format(1, filename)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Posts.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "{}-{}".format(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
    if instance.content:
        html_string = markdownify(instance.content)
        read_time = get_read_time(html_string)
        instance.read_time = read_time


class Posts(models.Model):
    """
    Post table representing a blog post, created by a specific user

    Attributes:
        Title: the name of the post (headline)
        Category: The Foreign key of a category
        Slug: the slugfield representing a more user-friendly address
        Subheading: a subheading for the article
        Image: An optional image for the blog post
        height_field: int, size for image
        width_field: int, size for image
        Content: the contents of the field. This will be populated with
            markdown converted text
        Author: A user byline, probably just one.
        Location: The location for the filing
        Draft: Boolean for draft status
        Publish: the publish date
        Created: The on-creation date and time, using UTC.
        Updated: The last modified date, in UTC.
    """

    class Meta:
        verbose_name_plural = 'posts'

    title = models.CharField(max_length=120, blank=False)
    category = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)
    subheading = models.CharField(max_length=180)
    image = models.ImageField(upload_to=upload_location,
                              null=True, blank=True,
                              width_field='width_field',
                              height_field='height_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = MarkdownxField(blank=False)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               default="bdmarks4")
    location = models.CharField(max_length=30)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    read_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        """
        The string representation method for a single Post
        :return:
        """
        return '{0}, by {1} {2}'.format(self.title, self.author.first_name,
                                        self.author.last_name)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})


pre_save.connect(pre_save_post_receiver, sender=Posts)
