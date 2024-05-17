import os
import twitchio
from twitchio.ext import commands
import websockets
import asyncio

access_token = os.getenv("TWITCH_ACCESS_TOKEN")
channel = os.getenv("TWITCH_CHANNEL")

class ServerBot(commands.Bot):
    def __init__(self):
        print("!def __init__(self):!")
        super().__init__(token=access_token, prefix='!', initial_channels=[channel])
        self.ws_payload_queue = asyncio.Queue()

    async def websocketserver(self, ws, path):
        print("!async def websocketserver(self ws, path):!")
        while True:
            print("ws_payload sent to wsclientscript.gd.")
            ws_payload = await self.ws_payload_queue.get()
            await ws.send(ws_payload)

    async def event_ready(self):
        print("!async def event_ready(self):!")
        self.ws_server = await websockets.serve(self.websocketserver, "localhost", 1116)

    async def event_message(self, message):
        print("!async def event_message(self, message):!")
        if message.echo:
            return
        await self.handle_commands(message)
        raw_ws_payload = f"NAME[{message.author.name}]CONTENT[{message.content}]"
        print(f"raw_ws_payload: NAME[{message.author.name}]CONTENT[{message.content}]")
        await self.ws_payload_queue.put(raw_ws_payload)

if __name__ == "__main__":
    serverbot = ServerBot()
    serverbot.run()