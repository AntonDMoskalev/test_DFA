from django.contrib import admin

from .models import Gallery


class GalleryAdmin(admin.ModelAdmin):
    """
    Displaying the Gallery model in the admin panel.
    """
    list_display = ("id", "author", "image")
    search_fields = ("author",)
    empty_value_display = "-pass-"


admin.site.register(Gallery, GalleryAdmin)
