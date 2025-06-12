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


from discord.ext import commands
import discord
import asyncio

CARTAS_CANAL_ID = 1382743951454507240  # Substitua pelo ID do canal onde as cartas serão enviadas

def registrar_cartas_anonimas(bot: commands.Bot):
    @bot.event
    async def on_message(message: discord.Message):
        if message.author.bot:
            return

        # Só responde a DMs
        if isinstance(message.channel, discord.DMChannel):
            conteudo = message.content.strip()
            if not conteudo:
                await message.channel.send("❌ Sua carta não pode estar vazia.")
                return

            await message.channel.send("✉️ Para quem é essa carta? Digite o nome ou apelido que será exibido.")

            try:
                resposta = await bot.wait_for(
                    "message",
                    timeout=60.0,
                    check=lambda m: m.author == message.author and isinstance(m.channel, discord.DMChannel)
                )
            except asyncio.TimeoutError:
                await message.channel.send("⏰ Tempo esgotado. Envie a mensagem novamente se ainda quiser enviar.")
                return

            destinatario = resposta.content.strip()

            if not destinatario:
                await message.channel.send("❌ Nome inválido. A carta não foi enviada.")
                return

            canal = bot.get_channel(CARTAS_CANAL_ID)
            if canal:
                embed = discord.Embed(
                    title=f"💌 {destinatario}, você recebeu uma carta anônima",
                    description=conteudo,
                    color=discord.Color.purple()
                )
                await canal.send(embed=embed)
                await message.channel.send("✅ Sua carta foi enviada com sucesso!")
            else:
                await message.channel.send("❌ Não consegui encontrar o canal de destino.")
            return  # não processar como comando

        # Permite que comandos normais funcionem
        await bot.process_commands(message)


