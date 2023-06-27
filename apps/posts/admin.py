from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("headline", "author", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("headline",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    readonly_fields = ("uuid", "created_at", "updated_at")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "headline",
                    "content",
                    "author",
                    "image",
                    "status",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "headline",
                    "content",
                    "author",
                    "image",
                    "status",
                )
            },
        ),
    )
