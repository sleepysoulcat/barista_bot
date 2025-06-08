import discord
import random
import json
import os
from discord.ext import commands

# gifs
hug_gifs = [
    "https://cdn.discordapp.com/attachments/708671169867546634/708671816276639804/VMnfxoeWIAk.gif?ex=684638cf&is=6844e74f&hm=00222d07afbc5006de87c0ec904cb7675f595c488305bc9c4b98f9534ecbcfba&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671819770626048/RKhPGj0y3H.gif?ex=684638d0&is=6844e750&hm=f1979205c5db0993982c8488356437e5d671e3b91a0ce220c0a696768b13941f&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671953170464828/Rg6aOvuqRar.gif?ex=684638f0&is=6844e770&hm=649678c14b4891a9a3c3c99ba87d8b7c65a77b7cd81f906dfe69eaec16e2c715&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671869162749952/cAlH4eoeRTN.gif?ex=684638dc&is=6844e75c&hm=7a2c35991c8a61c011c0bd00bba36bd82c3772c9c2d0d673dffdf4c3b2fbe5b8&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671944811348049/Rf9cnXUyBbm.gif?ex=684638ee&is=6844e76e&hm=2a452383698729c6666bd91237cf580af8c90b9f5be2b9227711cf0ab6844f0e&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671878453264424/d7GEKxdmcXF.gif?ex=684638de&is=6844e75e&hm=80f4f0229ceb4b119e459ff745f2a3df92ef6eb867329a48d13d12eca0b29efc&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671953120264222/tQsTjsDCr-h.gif?ex=684638f0&is=6844e770&hm=eb48b7a0ae6e50e13cab2d8f7a4215e7ac5e40e63a49ec82e887033db8413a6c&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671854591606815/40GtwAsAvuV.gif?ex=684638d8&is=6844e758&hm=7aa9f04ada48fdce8ed233af75d4ec6727e8e269fd81421c45b6d9eed7dc7da1&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671918869446696/jz7xK5wHTUi.gif?ex=684638e7&is=6844e767&hm=f887a728e00313043a4204aba8bb51e2bb2d90fd3e9b6d570118800a64cfeba5&",
    "https://cdn.discordapp.com/attachments/708671169867546634/708671891900071977/f3SntdcZ96M.gif?ex=684638e1&is=6844e761&hm=ca213d5a308408dbf7c2b5583a2a831be4eff4e33ca2eeeb137a082795fcaac5&",
]

pat_gifs = [
    "https://cdn.discordapp.com/attachments/708671684491739199/708672413545660507/LR8lKzjm1Eo.gif?ex=6846395d&is=6844e7dd&hm=0579ad48971856bcdcea9c9c5e4218e8fd98a989e4f9d778dcdccae2291c3d2a&",
    "https://cdn.discordapp.com/attachments/708671684491739199/708672410475560970/ko9MR4Q5E3y.gif?ex=6846395d&is=6844e7dd&hm=7d36e0d0ce528eb290ebc26742ba0b4e9bfb43760e33df2d1e675097220c3688&",
]

kiss_gifs = [
    "https://cdn.discordapp.com/attachments/708671674534330420/708672191918637086/CVVSUrcwQtH.gif?ex=68463929&is=6844e7a9&hm=48caf1fa26f09a5ada11fcd25cc97c3171123b7284fd2416ff553e96b6f8605b&",
    "https://cdn.discordapp.com/attachments/708671674534330420/708672219282145331/TKnSC7HK_wd.gif?ex=6846392f&is=6844e7af&hm=318b7d922ab8a4990bbeeb41d55403f54bedb2da90051321c49b274cd3e0ea69&",
    "https://cdn.discordapp.com/attachments/708671674534330420/708672190404624436/-egcN4ZQDV3.gif?ex=68463928&is=6844e7a8&hm=bd029a69eb9a76e2101e5b6fb9d2aa802f393524163ba79778695912c6e11111&",
    "https://cdn.discordapp.com/attachments/708671674534330420/708672249380470884/WPLZxjm8Ou9.gif?ex=68463936&is=6844e7b6&hm=24e2e6d83421f8e211caafa06f905cd1e8dd9338a80470721ef1ccaa5e33bede&",
]

slap_gifs = [
    "https://cdn.discordapp.com/attachments/713915370867654777/713938521106415675/sHnvo6dkr-p.gif?ex=6846440f&is=6844f28f&hm=8fdc68925fb8b374ac727bf3d2d8db3bdd83689df3b4b4ea2424d23e2510a990&"
]

nuzzles_gifs = [
    "https://cdn.discordapp.com/attachments/713915167951421451/713936952138661938/qQTAY1q-loP.gif?ex=68464299&is=6844f119&hm=58e00b793f503c60b029df01dd1c55638171e5e0fbb3b6b55572988ecae2ea6c&",
    "https://cdn.discordapp.com/attachments/713915167951421451/713936911433203753/r04M3J_gm64.gif?ex=6846428f&is=6844f10f&hm=c9a23c0b5fbf0198852a124ef6bb8eb9fd6b002d8d81bdfa5c3ea907eeee578f&",
]

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


def registrar_comandos_prefixo(bot: commands.Bot):

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

    # Comando hug
    @bot.command(name="hug")
    async def hug(ctx, member: discord.Member):
        await comando_interacao(ctx, member, hug_gifs, "is hugging", "hugged", "hug")

    # Comando pat
    @bot.command(name="pat")
    async def pat(ctx, member: discord.Member):
        await comando_interacao(ctx, member, pat_gifs, "is patting", "patted", "pat")

    # Comando kiss
    @bot.command(name="kiss")
    async def kiss(ctx, member: discord.Member):
        await comando_interacao(ctx, member, kiss_gifs, "is kissing", "kissed", "kiss")

    # Comando slap
    @bot.command(name="slap")
    async def slap(ctx, member: discord.Member):
        await comando_interacao(
            ctx, member, slap_gifs, "is slapping", "slapped", "slap"
        )

    # Comando nuzzles
    @bot.command(name="nuzzle")
    async def nuzzle(ctx, member: discord.Member):
        await comando_interacao(
            ctx, member, nuzzles_gifs, "is nuzzling", "nuzzled", "nuzzle"
        )

    # outros comandos -----------------------

    @bot.command()
    async def d(ctx, *, mensagem):
    # Nome do cargo permitido
        cargo_permitido = "Furry"

    # Verifica se o autor tem o cargo
        if not any(role.name == cargo_permitido for role in ctx.author.roles):
            return  # Silenciosamente ignora quem não tem o cargo

        try:
            await ctx.message.delete()  # Apaga a mensagem do usuário
        except discord.Forbidden:
            return  # Silenciosamente ignora caso não possa apagar

        await ctx.send(mensagem)
