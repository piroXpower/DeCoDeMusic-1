# This is the file that is going to run it all
import os
from pyrogram import Client as bot
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import *
from Assistant.helper.chatfilter import user_admin
# kick_chat_member


@bot.on_message(filters.command("ban") & filters.group)
def ban(bot, message):
    await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Banned Successfully")
try:
   except Exception as exc:
    await message.reply_to_message.reply(f"{exc}")
   
# unban_chat_member
@bot.on_message(filters.command("unban") & filters.group)

def unban(bot, message):
    await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
    await bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.mention} Unban Successfully")
try:
   except Exception as exc:
    await message.reply_to_message.reply(f"{exc}")

