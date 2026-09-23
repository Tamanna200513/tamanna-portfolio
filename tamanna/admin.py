from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'short_comment',
        'created_at',
        'is_read',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'comment',
    )

    ordering = (
        '-created_at',
    )


    def short_comment(self, obj):

        if len(obj.comment) > 50:
            return obj.comment[:50] + "..."

        return obj.comment