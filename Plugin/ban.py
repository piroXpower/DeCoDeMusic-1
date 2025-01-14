# This is the file that is going to run it all
import os
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import *
from helpers.decorators import authorized_users_only
# kick_chat_member


@bot.on_message(filters.command("ban") & filters.group)
@authorized_users_only
def ban(bot, message):
    bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Banned Successfully")
   
# unban_chat_member
@bot.on_message(filters.command("unban") & filters.group)
@authorized_users_only
def unban(bot, message):
    bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unban Successfully")
