from aiohttp import web

async def handle(request):
    return web.Response(text="Bot está vivo!")

app = web.Application()
app.add_routes([web.get("/", handle)])

async def iniciar_webserver():
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 3000)
    await site.start()
    print("🌐 Servidor web iniciado na porta 3000")
