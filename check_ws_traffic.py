import asyncio
import aiohttp


async def main():
    session = aiohttp.ClientSession()
    try:
        async with session.ws_connect("http://localhost:8080/ws") as ws:
            print("Connected to WebSocket")
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    print(f"Received WS Message: {msg.data[:100]}...")
                    break  # Just need one to prove it works
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    print("ws connection closed with exception %s", ws.exception())
    except Exception as e:
        print(f"WS Error: {e}")
    finally:
        await session.close()


if __name__ == "__main__":
    asyncio.run(main())
