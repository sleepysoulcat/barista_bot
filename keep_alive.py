from aiohttp import web

async def ping(request):
    return web.Response(text="Ainda viva, por favor pague um plano para mimmmmm")

def iniciar_webserver():
    app = web.Application()
    app.router.add_get('/', ping)
    web.run_app(app, port=3000) 
