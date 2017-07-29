from django.contrib import admin
from .models.posts import Post


class PostModelAdmin(admin.ModelAdmin):
    """
    A custom interface for the Posts page of the Admin site
    """

    list_display = ["__str__", "title","created", "updated"]
    list_display_links = ["__str__"]
    list_filter = ["author", "title", "updated", "created"]
    search_fields = ["title", "subheading", "content"]
    list_editable = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)
