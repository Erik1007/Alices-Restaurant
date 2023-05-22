from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('status', 'created_on')
    list_filter = ('status', 'created_on')
    summernote_fields = ('content',)
    actions = ['approve_post']

    def approve_post(self, request, queryset):
        queryset.update(approved=True)

