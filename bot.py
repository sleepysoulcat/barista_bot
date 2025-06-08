import discord
from discord.ext import commands
from discord import app_commands
import asyncio

from config import TOKEN, GUILD_ID
from comandos import registrar_comandos
from prefixos import registrar_comandos_prefixo
from keep_alive import iniciar_webserver

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="Eli ", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")
    guild = discord.Object(id=GUILD_ID)
    tree.clear_commands(guild=guild)
    registrar_comandos(tree)
    registrar_comandos_prefixo(bot)
    await tree.sync(guild=guild)
    print("✅ Comandos sincronizados.")

async def main():
    await iniciar_webserver()   # Inicia o servidor web sem criar outro loop
    await bot.start(TOKEN)

asyncio.run(main())
