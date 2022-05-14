import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("𝙲𝙻𝙾𝚂𝙴", callback_data='close_data')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo="https://telegra.ph/file/361547246d26056583ee4.jpg",
        caption=covid_info(query),
        quote=True
    )

def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**𝙲𝙾𝚅𝙸𝙳 𝟷𝟿 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽**--
᚛› 𝙲𝙾𝚄𝙽𝚃𝚁𝚈 : `{country}`
᚛› 𝙰𝙲𝚃𝙸𝚅𝙴𝙳 : `{active}`
᚛› 𝙲𝙾𝙽𝙵𝙸𝚁𝙼𝙴𝙳 : `{confirmed}`
᚛› 𝙳𝙴𝙰𝚃𝙷𝚂 : `{deaths}`
᚛› 𝙸𝙳 : `{info_id}`
᚛› 𝙻𝙰𝚂𝚃 𝚄𝙿𝙳𝙰𝚃𝙴 : `{last_update}`
᚛› 𝙻𝙰𝚃𝙸𝚃𝚄𝙳𝙴 : `{latitude}`
᚛› 𝙻𝙾𝙽𝙶𝙸𝚃𝚄𝙳𝙴 : `{longitude}`
᚛› 𝚁𝙴𝙲𝙾𝚅𝙴𝚁𝙴𝙳 : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error
