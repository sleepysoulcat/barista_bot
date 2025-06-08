from aiohttp import web

async def ping(request):
    return web.Response(text="✅ Estou vivo!")

async def iniciar_webserver():
    app = web.Application()
    app.router.add_get("/", ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, port=3000)
    await site.start()
