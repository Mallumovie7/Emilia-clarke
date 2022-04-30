"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "𝚈𝙾𝚄 𝙰𝚁𝙴 𝙽𝙾𝚃 𝙳𝙴𝙰𝙳. 𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝚂𝚃𝙸𝙻𝙻 𝙷𝙴𝚁𝙴. 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙽𝙾 𝙻𝙾𝚅𝙴 𝙵𝙾𝚁 𝙼𝙴 𝙽𝙾𝚆 𝙾𝙺𝙰𝚈 .. 𝚈𝙾𝚄'𝚛𝚎 𝙽𝙾𝚃 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝙻𝙸𝙺𝙴 𝚈𝙾𝚄 𝚄𝚂𝙴𝙳 𝚃𝙾 𝙱𝙴 .. 𝙹𝚄𝚂𝚃 𝚂𝚃𝙰𝚁𝚃 /start 𝙾𝙽𝙴 𝙰𝚃 𝙰 𝚃𝙸𝙼𝙴.."
REPO = "<b>𝚃𝙷𝙸𝚂 𝙸𝚂 𝙽𝙾𝚃 𝙾𝙿𝙴𝙽 𝚂𝙾𝚄𝚁𝙲𝙴 𝙿𝚁𝙾𝙹𝙴𝙲𝚃 </b>"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://youtube.com/channel/UCl1EnIFvBwT7dPtgfOYnvPA\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/Tamil_moviesdaa</b>\n\n<b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/RBLunainline</b> ez</b>"
JOKER = "<b>𝙱𝙾𝚃 ›› https://t.me/rb_luna_bot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("repo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("group", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("luna", COMMAND_HAND_LER) & f_onw_fliter)
async def joker(_, message):
    await message.reply_text(JOKER)




