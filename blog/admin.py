from django.contrib import admin
from .models import SingleBlog

class SingleBlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'introduction', )
    list_display_links = ('title',)


admin.site.register(SingleBlog,SingleBlogAdmin)