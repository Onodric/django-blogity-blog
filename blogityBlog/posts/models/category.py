from django.db import models


class Category(models.Model):
    """
    Category table representing a blog post, created by a specific user

    Attributes:
        Title: the name of the category (or tag)
    """

    class Meta:
        verbose_name_plural = 'Categories'

    title = models.CharField(max_length=120, blank=False)

    def __str__(self):
        """
        The string representation method for a single category
        :return:
        """
        return '{0}'.format(self.title)
