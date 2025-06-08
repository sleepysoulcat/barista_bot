from discord import app_commands, Interaction, Object
from config import GUILD_ID

# Comando: /falar (só para moderadores)
@app_commands.command(name="falar", description="O bot repete a mensagem (somente mods podem usar)")
@app_commands.describe(mensagem="Mensagem para o bot falar")
async def falar(interaction: Interaction, mensagem: str):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("❌ Você não tem permissão para usar este comando.", ephemeral=True)
        return

    await interaction.response.send_message(mensagem)


# Função para registrar os comandos no bot
def registrar_comandos(tree: app_commands.CommandTree):
    tree.add_command(falar, guild=Object(id=GUILD_ID))

