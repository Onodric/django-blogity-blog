from django.contrib import admin
from .models.posts import Posts


class PostModelAdmin(admin.ModelAdmin):
    """
    A custom interface for the Posts page of the Admin site

    It adds some functionality to the default Admin Posts page, such as
    searching and filtering and sortable column headings. also included is
    the ability to edit title from the list view.
    """

    list_display = ["__str__", "title","created", "updated"]
    list_display_links = ["__str__"]
    list_filter = ["author", "title", "updated", "created"]
    search_fields = ["title", "subheading", "content"]
    list_editable = ["title"]

    class Meta:
        model = Posts


admin.site.register(Posts, PostModelAdmin)
