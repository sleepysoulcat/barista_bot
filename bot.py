import discord
from discord.ext import commands
from discord import app_commands
import asyncio

from config import TOKEN, GUILD_ID
from comandos import registrar_comandos
from comandos import registrar_cartas_anonimas
from prefixos import registrar_comandos_prefixo
from keep_alive import iniciar_webserver
from awawa import iniciar_troca_de_apelido

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix="Eli ", intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    print(f"🤖 Bot online como {bot.user}")
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name="Café Cósmico ★ Vol. 2")
    )

    guild = discord.Object(id=GUILD_ID)
    tree.clear_commands(guild=guild)
    registrar_comandos(tree)
    registrar_cartas_anonimas(bot)
    registrar_comandos_prefixo(bot)
    await tree.sync(guild=guild)
    print("✅ Comandos sincronizados.")
    iniciar_troca_de_apelido(bot)

async def main():
    await iniciar_webserver()   # Inicia o servidor web sem criar outro loop
    await bot.start(TOKEN)

asyncio.run(main())
