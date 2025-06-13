import discord
from discord.ext import tasks
import random

ID_SERVIDOR = 1303533306372952084  # server_id
ID_USUARIO = 709048346706444320    # user_id
ID_CANAL_AVISO = 1303533306372952087  # alert_ch_id
apelido_ativo = True  # I/O


primeiros_nomes = [
    "Seu Joaquim", "Dona Lourdes", "Antônio", "Maria do Socorro", "João Batista", "Sebastião",
    "Gertrudes", "Otacílio", "Josefina", "Francisco", "Neide", "Adelino", "Eugênia", "Arlindo",
    "Hermínia", "Clementina", "Benedito", "Idalina", "Vicente", "Lurdes", "Camilo", "Zuleide",
    "Anísio", "Filomena", "Josias", "Isolina", "Nicanor", "Belarmina", "Onofre", "Candinha"
]

sobrenomes = [
    "Pereira", "Silva", "Barros", "Almeida", "da Cruz", "Moreira", "Ramos", "Fernandes",
    "Cardoso", "Bento", "Camargo", "Rocha", "Prado", "Macedo", "Ferreira", "Souza", "Oliveira",
    "Martins", "Monteiro", "Ribeiro", "Costa", "Teixeira", "Andrade", "Lima", "Moura", "Sales",
    "Bezerra", "Furtado", "Vieira", "Castro"
]

nomes_aleatorios = [f"{p} {s} 🐢" for p in primeiros_nomes for s in sobrenomes]

def iniciar_troca_de_apelido(bot: discord.ext.commands.Bot):
    @tasks.loop(hours=24)
    async def mudar_apelido():
        await bot.wait_until_ready()

        if not apelido_ativo:
            print("Troca de apelido pausada.")
            return
            
        guild = bot.get_guild(ID_SERVIDOR)
        canal = bot.get_channel(ID_CANAL_AVISO)

        if not guild:
            print("Não achei o servidor...")
            return

        membro = guild.get_member(ID_USUARIO)
        if not membro:
            print("Não encontrei o membro...")
            return

        novo_nome = random.choice(nomes_aleatorios)
        try:
            await membro.edit(nick=novo_nome)
            print(f"🔁 Apelido de {membro} alterado para {novo_nome}")
            if canal:
                await canal.send(f"O seu novo nome agora é {membro.mention} da silva")
        except discord.Forbidden:
            print("Não me deixam mais mudar nome da silva;-;")

    mudar_apelido.start()
