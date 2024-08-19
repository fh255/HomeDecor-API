from django.db import models
from posts.models import Post

class Tag(models.Model):
    """
    Tag model to categorize posts.
    A tag is linked to multiple posts, allowing flexible categorization.
    """
    name = models.CharField(max_length=50, unique=True)
    posts = models.ManyToManyField(Post, related_name='tags')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

