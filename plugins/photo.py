from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters


@Client.on_message(filters.photo & filters.private)
async def photo(client: Client, message: Message):
    try:
        await client.send_message(
            chat_id=message.chat.id,
            text="ՏᎬᏞᎬᏟͲ ᎽϴႮᎡ ᎡᎬϘႮᏆᎡᎬᎠ ᎷϴᎠᎬ ҒᎡϴᎷ ᏴᎬᏞϴᏔ!ㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="𝙱𝚁𝙸𝙶𝙷𝚃", callback_data="bright"),
                        InlineKeyboardButton(text="𝙼𝙸𝚇𝙴𝙳", callback_data="mix"),
                        InlineKeyboardButton(text="𝙱 & 𝚆", callback_data="b|w"),
                    ],
                    [
                        InlineKeyboardButton(text="𝙲𝙸𝚁𝙲𝙻𝙴", callback_data="circle"),
                        InlineKeyboardButton(text="𝙱𝙻𝚄𝚁", callback_data="blur"),
                        InlineKeyboardButton(text="𝙱𝙾𝚁𝙳𝙴𝚁", callback_data="border"),
                    ],
                    [
                        InlineKeyboardButton(text="𝚂𝚃𝙸𝙲𝙺𝙴𝚁", callback_data="stick"),
                        InlineKeyboardButton(text="𝚁𝙾𝚃𝙰𝚃𝙴", callback_data="rotate"),
                        InlineKeyboardButton(text="𝙲𝙾𝙽𝚃𝚁𝙰𝚂𝚃", callback_data="contrast"),
                    ],
                    [
                        InlineKeyboardButton(text="𝚂𝙴𝙿𝙸𝙰", callback_data="sepia"),
                        InlineKeyboardButton(text="𝙿𝙴𝙽𝙲𝙸𝙻", callback_data="pencil"),
                        InlineKeyboardButton(text="𝙲𝙰𝚁𝚃𝙾𝙾𝙽", callback_data="cartoon"),
                    ],
                    [
                        InlineKeyboardButton(text="𝙸𝙽𝚅𝙴𝚁𝚃", callback_data="inverted"),
                        InlineKeyboardButton(text="𝙶𝙻𝙸𝚃𝙲𝙷", callback_data="glitch"),
                        InlineKeyboardButton(text="𝚁𝙴𝙼𝙾𝚅𝙴-𝙱𝙶", callback_data="removebg"),
                    ],
                    [
                        InlineKeyboardButton(text="ᏟᏞϴՏᎬ", callback_data="close_data"),
                    ],
                ]
            ),
            reply_to_message_id=message.message_id,
        )
    except Exception as e:
        print("photomarkup error - " + str(e))
        if "USER_IS_BLOCKED" in str(e):
            return
        else:
            try:
                await message.reply_text("Something went wrong!", quote=True)
            except Exception:
                return
