from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=250)
    vote = models.IntegerField()
    description = models.CharField(max_length=700)
    hashtags = models.CharField(max_length=200, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Post: @{self.title}"

class Comment(models.Model):
    body = models.CharField(max_length=250)
    vote = models.IntegerField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment on: @{self.post}"
    

class Subreddit(models.Model):
    title = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=300)
    users = models.ManyToManyField(User)
    posts = models.ManyToManyField(Post, blank=True, null=True)

    def __str__(self):
        return f"Subreddit: @{self.title}"
