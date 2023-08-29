from django.db import models
from django.utils.html import format_html

class Details(models.Model):
    did = models.AutoField(primary_key=True)
    name = models.TextField(max_length=10)
    sirname = models.TextField(max_length=10)
    username = models.TextField(max_length=25)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = "Details"

class Post(models.Model):
    pid = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    image = models.URLField()
    category = models.CharField(max_length=100)
    username = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Posts"

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px; height:40px;"/>'.format(self.image))




