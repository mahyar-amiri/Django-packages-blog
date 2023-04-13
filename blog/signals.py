import telebot
from decouple import config

from django.db.models.signals import post_save
from django.dispatch import receiver

from comment.models import Comment
from rating.models import Rating
from reaction.models import Reaction

chat_id = config('CHAT_ID')
TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN)


@receiver(post_save, sender=Comment, dispatch_uid="comment")
def comment_created(sender, instance, **kwargs):
    bot.send_message(chat_id, instance)


@receiver(post_save, sender=Rating, dispatch_uid="rating")
def comment_created(sender, instance, **kwargs):
    bot.send_message(chat_id, instance)


@receiver(post_save, sender=Reaction, dispatch_uid="reaction")
def comment_created(sender, instance, **kwargs):
    bot.send_message(chat_id, instance)
