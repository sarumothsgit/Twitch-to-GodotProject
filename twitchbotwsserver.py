import os
import twitchio
from twitchio.ext import commands
import websockets
import asyncio

s_i = "TBWSS:" #Twitch Bot WebSocket Server Python script

access_token = os.getenv("TWITCH_ACCESS_TOKEN")
channel = os.getenv("TWITCH_CHANNEL")

class BotServer(commands.Bot):
    def __init__(self):
        print(s_i + "!def __init__(self):!")
        super().__init__(token=access_token, prefix='!', initial_channels=[channel])
        self.ws_payload_queue = asyncio.Queue()

    async def websocketserver(self, ws, path):
        print(s_i + "!async def websocketserver(self ws, path):!")
        while True:
            ws_payload = await self.ws_payload_queue.get()
            if ws_payload:
                await ws.send(ws_payload)
                print(s_i + "ws_payload sent to wsclient.gd.")
            else:
                print(s_i + "Empty payload received. Nothing sent.")

    async def event_ready(self):
        print(s_i + "!async def event_ready(self):!")
        self.ws_server = await websockets.serve(self.websocketserver, "localhost", 1116)

    async def event_message(self, message):
        print(s_i + "!async def event_message(self, message):!")
        if message.echo:
            return
        await self.handle_commands(message)
        raw_ws_payload = f"NAME[{message.author.name}]CONTENT[{message.content}]"
        print(s_i + f"raw_ws_payload received: NAME[{message.author.name}]CONTENT[{message.content}]")
        await self.ws_payload_queue.put(raw_ws_payload)

if __name__ == "__main__":
    botserver = BotServer()
    botserver.run()