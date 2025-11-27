import asyncio
import os
import json
import logging
from aiohttp import web
import nats

# --- Configuration ---
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
PORT = 8080

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SwarmDashboard")

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    request.app['websockets'].add(ws)
    logger.info("Websocket connection opened")

    try:
        async for msg in ws:
            pass # We only push data, don't expect much from client
    finally:
        request.app['websockets'].discard(ws)
        logger.info("Websocket connection closed")
    return ws

async def index_handler(request):
    return web.FileResponse('./body/hands/swarm_dashboard.html')

async def nats_listener(app):
    try:
        nc = await nats.connect(NATS_URL)
        logger.info(f"Connected to NATS at {NATS_URL}")
        
        async def msg_handler(msg):
            data = msg.data.decode()
            # Broadcast to all connected websockets
            for ws in set(app['websockets']):
                try:
                    await ws.send_str(data)
                except Exception as e:
                    logger.error(f"Error sending to WS: {e}")

        await nc.subscribe("hfo.heartbeat.>", cb=msg_handler)
        
        # Keep connection alive in app context if needed, or just let the loop handle it
        app['nats_nc'] = nc
        
        # Wait until app stops
        try:
            while True:
                await asyncio.sleep(3600)
        except asyncio.CancelledError:
            await nc.close()
            
    except Exception as e:
        logger.error(f"NATS Error: {e}")

async def start_background_tasks(app):
    app['nats_task'] = asyncio.create_task(nats_listener(app))

async def cleanup_background_tasks(app):
    app['nats_task'].cancel()
    await app['nats_task']

async def init_app():
    app = web.Application()
    app['websockets'] = set()
    app.router.add_get('/', index_handler)
    app.router.add_get('/ws', websocket_handler)
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)
    return app

if __name__ == '__main__':
    # Bind to 0.0.0.0 to ensure visibility across container/host boundaries
    web.run_app(init_app(), host='0.0.0.0', port=PORT)
