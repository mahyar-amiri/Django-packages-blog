from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from comment.models import Comment
from rating.models import Rating
from reaction.models import Reaction


class Article(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article_images', null=True, blank=True)

    comments = GenericRelation(Comment)
    ratings = GenericRelation(Rating)
    reactions = GenericRelation(Reaction)

    def __str__(self):
        return self.title
