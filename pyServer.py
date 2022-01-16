import asyncio
import websockets

connections = []

async def server(ws, path):
    connections.append(ws)
    while True:
        message = await ws.recv()
        print(f'Msg>> {message}')
        if len(connections) == 2:
            idx = connections.index(ws)
            if idx == 0:
                await connections[1].send(message)
            elif idx == 1:
                await connections[0].send(message)

    
        

Server = websockets.serve(server, '127.0.0.1', 1111)

asyncio.get_event_loop().run_until_complete(Server)
asyncio.get_event_loop().run_forever()

