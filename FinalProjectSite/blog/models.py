from django.db import models
from django.contrib.auth.models import User

POST_STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)

class Post(models.Model):
    title = models.CharField(max_length = 200, unique = True)
    slug = models.SlugField(max_length = 200, unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices = POST_STATUS, default = 0)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

