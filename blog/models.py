import telebot
from decouple import config

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from comment.models import Comment
from rating.models import Rating
from reaction.models import Reaction


@receiver(post_save, sender=Comment, dispatch_uid="comment_created")
def comment_created(sender, instance, **kwargs):
    chat_id = config('CHAT_ID')
    TOKEN = config('TOKEN')
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(chat_id, instance)
    # print(instance)


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
