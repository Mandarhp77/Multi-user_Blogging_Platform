from django.contrib import admin
from .models import Post, Details


class PostAdmin(admin.ModelAdmin):
    list_display = ("image_tag",'title','add_date',"category","username")
    search_fields = ('title',)
    list_filter = ('category',)
    list_per_page = 50
'''
class ImageAdmin(admin.ModelAdmin):
    list_display = ("image_tag",'title')
    list_per_page = 50'''

#admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
#admin.site.register(Image, ImageAdmin)
admin.site.register(Details)

