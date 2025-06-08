import discord
from discord.ext import commands
from discord import app_commands
from config import TOKEN, GUILD_ID
from comandos import registrar_comandos
from prefixos import registrar_comandos_prefixo

# tentando manter online
import threading
from keep_alive import iniciar_webserver
threading.Thread(target=iniciar_webserver).start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="Eli ", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")

    guild = discord.Object(id=GUILD_ID)

    tree.clear_commands(guild=guild)
    registrar_comandos(tree)             # Slash (/)
    registrar_comandos_prefixo(bot)      # Prefixo (Eli )

    await tree.sync(guild=guild)
    print("✅ Comandos sincronizados.")

bot.run(TOKEN)
