import logging
from config import Config
from pyrogram import Client
from rich.console import Console



#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.BOT_TOKEN
OWNER_ID = Config.OWNER_ID
START_PIC = Config.START_PIC
if not START_PIC:
    START_PIC = "https://graph.org/file/c1c19fee2ac7b458087f7.jpg"

#rich
LOG = Console()


logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "Nixera",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    
app.start()
bot = app.get_me()
BOT_ID = bot.id
BOT_USERNAME = bot.username
print(BOT_ID)

