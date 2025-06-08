from aiohttp import web
import os

async def handle(request):
    return web.Response(text="Bot está vivo!")

app = web.Application()
app.add_routes([web.get("/", handle)])

def iniciar_webserver():
    port = int(os.environ.get("PORT", 3000))
    web.run_app(app, port=port, handle_signals=False)
