from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    body = models.TextField(max_length=250, default='')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.body

