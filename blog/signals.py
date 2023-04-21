import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from comment.models import Comment, Reaction
from rating.models import UserRating
from reaction.models import UserReaction


chat_id = config('CHAT_ID')
TOKEN = config('TOKEN')
bot = telebot.TeleBot(TOKEN, parse_mode='HTML')
User = get_user_model()


def markup_kb(urlhash):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton('Accept ✅', callback_data=f'cb_accept_{urlhash}'), InlineKeyboardButton('Reject ❌', callback_data=f'cb_reject_{urlhash}'))
    markup.add(InlineKeyboardButton('Accept Edit ✅', callback_data=f'cb_edit_accept_{urlhash}'), InlineKeyboardButton('Reject Edit ❌', callback_data=f'cb_edit_reject_{urlhash}'))
    markup.add(InlineKeyboardButton('Pin 📌', callback_data=f'cb_pin_{urlhash}'), InlineKeyboardButton('Spoiler 👁️‍🗨️', callback_data=f'cb_spoiler_{urlhash}'))
    return markup


@receiver(post_save, sender=User, dispatch_uid="user")
def user(sender, instance, **kwargs):
    message = f'#User\n\n#{instance.username} logged in' if instance.last_login else f'#User\n\n#{instance.username} joined us 🎉'
    bot.send_message(chat_id, message)


@receiver(post_save, sender=Comment, dispatch_uid="comment")
def comment(sender, instance, **kwargs):
    comment_type = f'replied to #{instance.parent.user.username}' if instance.parent else 'commented'
    comment_content = instance.content_main if instance.status_edited != 'd' else f'<s>{instance.content_main}</s>\n{instance.content}'
    comment_content = f'<tg-spoiler>{comment_content}</tg-spoiler>' if instance.is_spoiler else comment_content
    message = f'#Comment\n\n#{instance.user.username} {comment_type} on <b>{instance.content_object}</b>\n\n<i>{comment_content}</i>'
    bot.send_message(chat_id, message, reply_markup=markup_kb(instance.urlhash))


@receiver(post_save, sender=Reaction, dispatch_uid="comment_reaction")
def comment_reaction(sender, instance, **kwargs):
    message = f'#Comment_Reaction\n\n#{instance.user.username} reacted {instance.react.emoji} to <b>{instance.comment.content_object}</b> comment.\n\n#{instance.comment.user.username} : \n{instance.comment.content_main}'
    bot.send_message(chat_id, message)


@receiver(post_save, sender=UserRating, dispatch_uid="rating")
def rating(sender, instance, **kwargs):
    user_rate = f'[{instance.rate}]⭐' if instance.rating.settings.slug == 'default-config' else '❤️'
    message = f'#Rating\n\n#{instance.user.username} rated {user_rate} to <b>{instance.rating.content_object}</b>'
    bot.send_message(chat_id, message)


@receiver(post_save, sender=UserReaction, dispatch_uid="reaction")
def reaction(sender, instance, **kwargs):
    message = f'#Reaction\n\n#{instance.user.username} reacted {instance.react.emoji} to <b>{instance.reaction.content_object}</b>'
    bot.send_message(chat_id, message)
