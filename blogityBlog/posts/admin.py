from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models.posts import Posts
from .models.category import Category


class PostModelAdmin(admin.ModelAdmin):
    """
    A custom interface for the Posts page of the Admin site

    It adds some functionality to the default Admin Posts page, such as
    searching and filtering and sortable column headings. also included is
    the ability to edit title from the list view.
    """

    list_display = ["__str__", "title", "created", "updated", "category"]
    list_display_links = ["__str__"]
    list_filter = ["author", "title", "updated", "created", "category"]
    search_fields = ["title", "subheading", "content", "category"]
    list_editable = ["title"]

    class Meta:
        model = Posts


admin.site.register(Posts, MarkdownxModelAdmin)
admin.site.register(Category)
