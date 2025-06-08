import discord
from discord.ext import commands
from discord import app_commands
from config import TOKEN, GUILD_ID
from comandos import registrar_comandos
from prefixos import registrar_comandos_prefixo

# tentando manter online
import threading
from keep_alive import iniciar_webserver

@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")

    # Iniciar o servidor web
    await iniciar_webserver()

    guild = discord.Object(id=GUILD_ID)
    tree.clear_commands(guild=guild)
    registrar_comandos(tree)
    registrar_comandos_prefixo(bot)
    await tree.sync(guild=guild)
    print("✅ Comandos sincronizados.")

bot.run(TOKEN)
