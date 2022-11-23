from django.contrib import admin
from .models import Books, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'book', 'creat_at', 'status', 'recommend',)


admin.site.register(Books)
admin.site.register(Comment)
