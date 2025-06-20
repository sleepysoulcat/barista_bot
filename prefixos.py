import discord
import random
import json
import os
from discord.ext import commands
from gifs import *



# caminho json
CONTADORES_PATH = "contadores.json"


# carregar json
def carregar_contadores():
    if os.path.exists(CONTADORES_PATH):
        with open(CONTADORES_PATH, "r") as f:
            return json.load(f)
    return {}


# salvar dados no json
def salvar_contadores(data):
    with open(CONTADORES_PATH, "w") as f:
        json.dump(data, f, indent=4)


async def comando_interacao(
        ctx, member: discord.Member, gifs, descricao, acao_passado, tipo
    ):
        author = ctx.author
        gif = random.choice(gifs)

        contadores = carregar_contadores()
        author_id = str(author.id)
        member_id = str(member.id)

        if tipo not in contadores:
            contadores[tipo] = {}

        if author_id not in contadores[tipo]:
            contadores[tipo][author_id] = {"deu": 0, "recebeu": 0}
        if member_id not in contadores[tipo]:
            contadores[tipo][member_id] = {"deu": 0, "recebeu": 0}

        contadores[tipo][author_id]["deu"] += 1
        contadores[tipo][member_id]["recebeu"] += 1

        salvar_contadores(contadores)

        deu = contadores[tipo][author_id]["deu"]
        recebeu = contadores[tipo][member_id]["recebeu"]

        embed = discord.Embed(
            description=f"**{author.display_name}** {descricao} **{member.display_name}**",
            color=discord.Color.from_rgb(0, 180, 216),
        )
        embed.set_image(url=gif)
        embed.set_footer(
            text=f"{member.display_name} got {acao_passado} {recebeu} times and {author.display_name} {acao_passado} others {deu} times"
        )
        await ctx.send(embed=embed)

def registrar_comandos_prefixo(bot: commands.Bot):

# Comando Blush
    @bot.command(name="blush")
    async def blush(ctx, member: discord.Member):
        await comando_interacao(ctx, member, blush_gifs, "is blushing at", "blushed at", "blush")

# Comando Love
    @bot.command(name="love")
    async def love(ctx, member: discord.Member):
        await comando_interacao(ctx, member, love_gifs, "is showing love to", "loved", "love")

# Comando Boop
    @bot.command(name="boop")
    async def boop(ctx, member: discord.Member):
        await comando_interacao(ctx, member, boop_gifs, "boops", "booped", "boop")

# Comando Lurk
    @bot.command(name="lurk")
    async def lurk(ctx, member: discord.Member):
        await comando_interacao(ctx, member, lurk_gifs, "is lurking around", "lurked", "lurk")

# Comando Cheer
    @bot.command(name="cheer")
    async def cheer(ctx, member: discord.Member):
        await comando_interacao(ctx, member, cheer_gifs, "is cheering up", "cheered", "cheer")

# Comando Nom
    @bot.command(name="nom")
    async def nom(ctx, member: discord.Member):
        await comando_interacao(ctx, member, nom_gifs, "noms", "nommed", "nom")

# Comando Cuddle
    @bot.command(name="cuddle")
    async def cuddle(ctx, member: discord.Member):
        await comando_interacao(ctx, member, cuddle_gifs, "is cuddling", "cuddled", "cuddle")

# Comando Nuzzle
    @bot.command(name="nuzzle")
    async def nuzzle(ctx, member: discord.Member):
        await comando_interacao(ctx, member, nuzzle_gifs, "is nuzzling", "nuzzled", "nuzzle")

# Comando Dance
    @bot.command(name="dance")
    async def dance(ctx, member: discord.Member):
        await comando_interacao(ctx, member, dance_gifs, "is dancing with", "danced with", "dance")

# Comando Pat
    @bot.command(name="pat")
    async def pat(ctx, member: discord.Member):
        await comando_interacao(ctx, member, pat_gifs, "is patting", "patted", "pat")

# Comando Feed
    @bot.command(name="feed")
    async def feed(ctx, member: discord.Member):
        await comando_interacao(ctx, member, feed_gifs, "is feeding", "fed", "feed")

# Comando Peck
    @bot.command(name="peck")
    async def peck(ctx, member: discord.Member):
        await comando_interacao(ctx, member, peck_gifs, "is pecking", "pecked", "peck")

# Comando Glomp
    @bot.command(name="glomp")
    async def glomp(ctx, member: discord.Member):
        await comando_interacao(ctx, member, glomp_gifs, "is glomping", "glomped", "glomp")

# Comando Poke
    @bot.command(name="poke")
    async def poke(ctx, member: discord.Member):
        await comando_interacao(ctx, member, poke_gifs, "is poking", "poked", "poke")

# Comando Handhold
    @bot.command(name="handhold")
    async def handhold(ctx, member: discord.Member):
        await comando_interacao(ctx, member, handhold_gifs, "is holding hands with", "held hands with", "handhold")

# Comando Pout
    @bot.command(name="pout")
    async def pout(ctx, member: discord.Member):
        await comando_interacao(ctx, member, pout_gifs, "is pouting at", "pouted at", "pout")

# Comando Happy
    @bot.command(name="happy")
    async def happy(ctx, member: discord.Member):
        await comando_interacao(ctx, member, happy_gifs, "is happy with", "was happy with", "happy")

# Comando Sleep
    @bot.command(name="sleep")
    async def sleep(ctx, member: discord.Member):
        await comando_interacao(ctx, member, sleep_gifs, "is sleeping next to", "slept next to", "sleep")

# Comando Highfive
    @bot.command(name="highfive")
    async def highfive(ctx, member: discord.Member):
        await comando_interacao(ctx, member, highfive_gifs, "gives a high five to", "high-fived", "highfive")

# Comando Thumbsup
    @bot.command(name="thumbsup")
    async def thumbsup(ctx, member: discord.Member):
        await comando_interacao(ctx, member, thumbsup_gifs, "gives a thumbs up to", "gave a thumbs up to", "thumbsup")

# Comando Hug
    @bot.command(name="hug")
    async def hug(ctx, member: discord.Member):
        await comando_interacao(ctx, member, hug_gifs, "is hugging", "hugged", "hug")

# Comando Tickle
    @bot.command(name="tickle")
    async def tickle(ctx, member: discord.Member):
        await comando_interacao(ctx, member, tickle_gifs, "is tickling", "tickled", "tickle")

# Comando Kiss
    @bot.command(name="kiss")
    async def kiss(ctx, member: discord.Member):
        await comando_interacao(ctx, member, kiss_gifs, "is kissing", "kissed", "kiss")

# Comando Wag
    @bot.command(name="wag")
    async def wag(ctx, member: discord.Member):
        await comando_interacao(ctx, member, wag_gifs, "is wagging at", "wagged at", "wag")

# Comando Laugh
    @bot.command(name="laugh")
    async def laugh(ctx, member: discord.Member):
        await comando_interacao(ctx, member, laugh_gifs, "is laughing with", "laughed with", "laugh")

# Comando Wave
    @bot.command(name="wave")
    async def wave(ctx, member: discord.Member):
        await comando_interacao(ctx, member, wave_gifs, "waves at", "waved at", "wave")

# Comando Lick
    @bot.command(name="lick")
    async def lick(ctx, member: discord.Member):
        await comando_interacao(ctx, member, lick_gifs, "is licking", "licked", "lick")



    # outros comandos -----------------------

    @bot.command()
    async def d(ctx, *, mensagem):
        cargo_permitido = "Furry"

        if not any(role.name == cargo_permitido for role in ctx.author.roles):
            return  

        try:
            await ctx.message.delete() 
        except discord.Forbidden:
            return 

        await ctx.send(mensagem)


@bot.command()
async def e(ctx, *, mensagem):
    cargo_permitido = "Furry"

    if not any(role.name == cargo_permitido for role in ctx.author.roles):
        return 

    try:
        await ctx.message.delete()  
    except discord.Forbidden:
        return  

    embed = discord.Embed(
        description=mensagem,
        color=discord.Color.from_str("#00b4d8")
    )
    await ctx.send(embed=embed)
