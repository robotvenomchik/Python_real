from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json
router= APIRouter(
    prefix="/ws",

)
@router.websocket('/')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        text= await websocket.receive_text()
        await websocket.send_text(f'Your text: {text}')
        await websocket.send_json(json.dumps({'count': 5}))