
import asyncio
import websockets
import json

async def test_ping():
    async with websockets.connect("ws://localhost:7331/ws") as websocket:
        await websocket.send(json.dumps({"type": "ping"}))
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.run(test_ping())
