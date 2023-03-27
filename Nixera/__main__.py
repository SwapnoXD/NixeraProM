import asyncio
import importlib

from pyrogram import idle
from Nixera import LOG
from Nixera.plugins import ALL_MODULES


async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module("Nixera.plugins." + all_module)
    LOG.print("[bold yellow]Vixera Started.")
    await idle() 
    LOG.print("[bold red]Vixera Started Successfully.")



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
    
