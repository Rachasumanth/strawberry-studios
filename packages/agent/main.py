
from fastapi import FastAPI, WebSocket
import json

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("Client connected")
    try:
        while True:
            data = await websocket.receive_text()
            message = json.loads(data)
            if message.get("type") == "ping":
                response = {"type": "pong", "status": "online"}
                await websocket.send_text(json.dumps(response))
    except Exception as e:
        print(f"Client disconnected: {e}")
