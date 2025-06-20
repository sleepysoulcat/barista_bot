import discord
import asyncio
from discord import app_commands, Interaction, Object
from config import GUILD_ID

@app_commands.command(name="falar", description="O bot repete a mensagem (somente mods podem usar)")
@app_commands.describe(mensagem="Mensagem para o bot falar")
async def falar(interaction: Interaction, mensagem: str):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("❌ Você não tem permissão para usar este comando.", ephemeral=True)
        return

    await interaction.response.send_message(mensagem)


def registrar_comandos(tree: app_commands.CommandTree):
    tree.add_command(falar, guild=Object(id=GUILD_ID))
    tree.add_command(ApelidoControlador(), guild=Object(id=GUILD_ID))


class ApelidoControlador(app_commands.Group):
    @app_commands.command(name="pararnomedasilva", description="não quero maissss aaaaaaaaaaaa :c")
    async def parar(self, interaction: discord.Interaction):
        if interaction.user.id != ID_USUARIO:
            await interaction.response.send_message("Você não tem permissão para usar esse comando.", ephemeral=True)
            return

        global apelido_ativo
        apelido_ativo = False
        await interaction.response.send_message("ta bom parei :c.", ephemeral=True)



class ApelidoControlador2(app_commands.Group):
    @app_commands.command(name="voltamudarnome", description="volta ter nomes de veio aleatorio")
    async def parar(self, interaction: discord.Interaction):
        if interaction.user.id != ID_USUARIO:
            await interaction.response.send_message("você nnnnnnn.", ephemeral=True)
            return

        global apelido_ativo
        apelido_ativo = True
        await interaction.response.send_message("eba vou te ajudar a escolher um nome :pray:", ephemeral=True)

def setup_comandos(bot):
    bot.tree.add_command(ApelidoControlador())

from discord.ext import commands

CARTAS_CANAL_ID = 1382743951454507240  # Substitua pelo ID do canal onde as cartas serão enviadas
e1 = "<:aubrey_twirl:1382754308268757122>"
e2 = "<:comfyy:1375943688638824562>"


def registrar_cartas_anonimas(bot: commands.Bot):
    @bot.event
    async def on_message(message: discord.Message):
        if message.author.bot:
            return

        # Só responde a DMs
        if isinstance(message.channel, discord.DMChannel):
            conteudo = message.content.strip()
            if not conteudo:
                await message.channel.send("(¬_¬ )   | Hey, você não escreveu nada, quer enganar quem?")
                return

            await message.channel.send("( ˙꒳​˙ )  | Para quem é esse fax?")

            try:
                resposta = await bot.wait_for(
                    "message",
                    timeout=60.0,
                    check=lambda m: m.author == message.author and isinstance(m.channel, discord.DMChannel)
                )
            except asyncio.TimeoutError:
                await message.channel.send("( ~°-°)~  | Acabou o tempo.")
                return

            destinatario = resposta.content.strip()

            if not destinatario:
                await message.channel.send("(⇀‸↼‶)  | nome errado!")
                return

            canal = bot.get_channel(CARTAS_CANAL_ID)
            if canal:
                embed = discord.Embed(
                    title=f"📠 {destinatario}, você recebeu um fax anônimo",
                    description=conteudo,
                    color=discord.Color.from_str("#00b4d8")
                )
                await canal.send(embed=embed)
                await message.channel.send("( ´ ω ` )  | Fax enviado!")
            else:
                await message.channel.send("(⇀‸↼‶)  | Não encontrei o canal.")
            return  # não processar como comando

        # Permite que comandos normais funcionem
        await bot.process_commands(message)


