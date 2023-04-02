from pyrogram import filters, __version__ as pyrogram_version
import random 
from telethon import __version__ as telethon_version

import time
StartTime = time.time()
from pyrogram import enums 
from pyrogram.enums import ChatType
from pyrogram.types import Message
from pyrogram.types.bots_and_keyboards.inline_keyboard_button import InlineKeyboardButton
from pyrogram.types.bots_and_keyboards.inline_keyboard_markup import InlineKeyboardMarkup
from Nixera import app
from pyrogram.types import CallbackQuery

BOT_IMG = ("https://telegra.ph/file/239a076932e0a047f715e.jpg",
                       "https://telegra.ph/file/2cb897995025e09fa14c9.jpg")

        
   
HELP_TEXT = """
**Hello Dear**
**Every possibility commands of Nixera is documented here. Click below buttons to get help**
"""

HELP_BUTTON = [[
        InlineKeyboardButton('Admin', callback_data='admin_help'),
        InlineKeyboardButton('Greetings', callback_data='greet_help'),
        InlineKeyboardButton('NEKOS', callback_data='nekos_help'),
        ],[
        InlineKeyboardButton('NSFW', callback_data='nsfw_help'),
        InlineKeyboardButton('MISC', callback_data='misc_help'),
        InlineKeyboardButton('INFO', callback_data='userinfo_help'),
        ],[
        InlineKeyboardButton('MEME', callback_data='meme_help'),
        InlineKeyboardButton('FUN', callback_data='fun_help'),
        InlineKeyboardButton('SG', callback_data='sticker_help'),
        ],[
        InlineKeyboardButton('DEV', callback_data='dev_help'),
        InlineKeyboardButton('TOOLS', callback_data='tools_help')]]

ADMIN_BUTTON = [[
        InlineKeyboardButton('Promote', callback_data='anime_help'),
        InlineKeyboardButton('Disable', callback_data='admin_help'),
        InlineKeyboardButton('Pin', callback_data='nekos_help'),
        ],[
        InlineKeyboardButton('Info', callback_data='nsfw_help'),
        InlineKeyboardButton('Mute', callback_data='misc_help'),
        ],[
        InlineKeyboardButton('back 🔙', callback_data='help_back'),
        InlineKeyboardButton('close 🗑', callback_data='close')]]

GREET_BUTTON = [[
        InlineKeyboardButton('General', callback_data='admin_help'),
        InlineKeyboardButton('Welcome Section', callback_data='anime_help'),
        InlineKeyboardButton('Welcome Mute', callback_data='nekos_help'),
        ],[
        InlineKeyboardButton('Buttons Help', callback_data='nsfw_help'),
        InlineKeyboardButton('Variables Help', callback_data='misc_help'),
        InlineKeyboardButton('Examples', callback_data='userinfo_help'),
        ],[
        InlineKeyboardButton('Clean Services/Purges', callback_data='meme_help'),
        ],[
        InlineKeyboardButton('back 🔙', callback_data='help_back'),
        InlineKeyboardButton('close 🗑', callback_data='close')]]


         
@app.on_message(filters.command(["help"], ["/", ".", "?"]))
async def start(_, m: Message):
   await m.reply_photo(random.choice(BOT_IMG),caption=HELP_TEXT.format(m.from_user.mention),
                      reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
           
  
@app.on_callback_query(filters.regex("help_back"))
async def help(_, query: CallbackQuery):
    await query.message.edit_caption(HELP_TEXT,
                                    reply_markup=InlineKeyboardMarkup(HELP_BUTTON),)
               
@app.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
           query = query.message
           await query.delete()
         
 
ANIME_TEXT = """
anime themed fun & search:

• `/anime {name}` - Search animes in myanimelist.net.
• `/character {name}` - Search Character in myanimelist.net.
• `/upcoming` - details in upcoming animes in myanimelist.net.
• `/quotes` - random anime quotes.
"""

BUTTON = [[InlineKeyboardButton("back 🔙", callback_data="help_back"),
            InlineKeyboardButton("close 🗑", callback_data='close'),]]


@app.on_callback_query(filters.regex("anime_help"))
async def animehelp(_, query: CallbackQuery):
     await query.message.edit_caption(ANIME_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
USERINFO_TEXT = """
user info chat info:
• /id - userid & chatid.
• /info - userinformation.
• /ginfo - chat information.
• /json - full intention about user & chat.
"""

@app.on_callback_query(filters.regex("userinfo_help"))
async def userinfohelp(_, query: CallbackQuery):
     await query.message.edit_caption(USERINFO_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

ADMIN_TEXT = """
usage of admin cmds:
• /ban- ban a user.
• /unban - unban a user. 
• /del - delete a message.
• /purge - delete msg multi.
• /pin - pin a message.
• /unpin - unpin a message.
• /unpinall - unpin all msg.
• /setgtitle - set group title.
• /setgpic - set group pic.
• /rgpic - remove group pic.
"""

@app.on_callback_query(filters.regex("admin_help"))
async def adminhelp(_, query: CallbackQuery):
     await query.message.edit_caption(ADMIN_TEXT,
                                      reply_markup=InlineKeyboardMarkup(ADMIN_BUTTON),)
NEKOS_TEXT = """
anime themed sfw:
**image:**
neko, waifu

**animation:**
cry, kill, smile, 
highfive, slap, kick, 
hug, pat, punch,
sleep, wink, think, 
feed, tickle, shoot, 
thumbsup, smug, laugh, 
bore, baka, dance,
blush, facepalm, stare, 
pout, handhold, wave, 
cuddle, poke, shrug
"""

@app.on_callback_query(filters.regex("nekos_help"))
async def sfwhelp(_, query: CallbackQuery):
     await query.message.edit_caption(NEKOS_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

NSFW_TEXT = """
this type of plugins fully Hentai 🔞
so don't use public groups
using: Waifu.pics

• /hneko - hentai nekos img.
• /hwaifu - hentai waifu img.
• /blowjob - hentai blowjob gif.
• /trap - hentai trap img.
• /lewd - get anime lewd img.
• /ero - get anime ero img. 
• /pussy - get smile pussy img.
"""

@app.on_callback_query(filters.regex("nsfw_help"))
async def nsfwhelp(_, query: CallbackQuery):
     await query.message.edit_caption(NSFW_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

MISC_TEXT = """
**random misc tools:**

/font {text}: for style fonts.
/tm: reply to media for upload telegraph.
/txt {pagename}: reply to text for upload telegraph.
/pastet: reply to msg paste.
/rename: rename files.
/encrypt: reply to msg encrypt.
/decrypt: reply to msg decrypt.
/spell: reply to msg convert correct spelling.
/wall {text}: get awesome wallpaper.
/tr {code}: reply to msg translate.
/lang: translate language codes.
/reddit {text}: search on reddit.
/ud {text}: ward definition.
/share: reply to msg get share link.
"""

@app.on_callback_query(filters.regex("misc_help"))
async def mischelp(_, query: CallbackQuery):
     await query.message.edit_caption(MISC_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
MEME_TEXT = """
**Memes & jokes:**
/ameme: read a random anime memes.
/meme: read a random memes.
/hmeme: read a hentai based memes.
/joke: read some random jokes.
"""

@app.on_callback_query(filters.regex("meme_help"))
async def memehelp(_, query: CallbackQuery):
     await query.message.edit_caption(MEME_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

STICKER_TEXT = """
/getsticker: reply to sticker for get photo document type. 
/stickers {text}: for search stickers.
/stickerid: reply to sticker to get I'd.
/gifid: reply to gif for get gif I'd 
"""
@app.on_callback_query(filters.regex("sticker_help"))
async def stickerhelp(_, query: CallbackQuery):
     await query.message.edit_caption(STICKER_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
FUN_TEXT = """
<b>Fun commands:</b>
/react: reply to msg react.
/gban: fake gban for fun.
`good morning`: regex cmd tell good morning.
`good night`: regex cmd tell good night.
/dare: reply to user give dare.
/truth: reply to user give truth. 
/write {text}: note written photo type.
/hack: reply to user hack.
/love: animation love story. 
"""

@app.on_callback_query(filters.regex("fun_help"))
async def funhelp(_, query: CallbackQuery):
     await query.message.edit_caption(FUN_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

DEV_TEXT = """
/logs: get bot logs.
/eval: run codes.
/ping: bot server start time & end time.
/sh: run codes.
/leave: bot left the chat. 
/pyupload: get plugins document type.
/devlist: list of developer.
"""
@app.on_callback_query(filters.regex("dev_help"))
async def devhelp(_, query: CallbackQuery):
     await query.message.edit_caption(DEV_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)

TOOLS_TEXT = """
/feedback {text}: give feedback about bot.
/img {text}: download img to google.
/logo {text}: random logo generate.
/logohq {text}: hight quality logo generate. 
/reverse: reply to image for search on google.  
/wiki {text}: Wikipedia search.
/song {text: download songs with high quality.
/countryinfo {text}: generate country information.
/github {text}: github user profile information.
"""
@app.on_callback_query(filters.regex("tools_help"))
async def toolshelp(_, query: CallbackQuery):
     await query.message.edit_caption(TOOLS_TEXT,
                                      reply_markup=InlineKeyboardMarkup(BUTTON),)
GREET_TEXT = """
Give your members a warm welcome with the greetings module! Also available some security systems...!

**Click below buttons to get available commands**
"""
@app.on_callback_query(filters.regex("greet_help"))
async def toolshelp(_, query: CallbackQuery):
     await query.message.edit_caption(GREET_TEXT,
                                      reply_markup=InlineKeyboardMarkup(GREET_BUTTON),)



