import logging

import discord
import datetime
import websockets
import json
import asyncio
from redbot.core import commands

class Trakteer(commands.Cog):
    # init method or constructor
    def __init__(self, bot):
        self.bot = bot
        self.socket_task = self.bot.loop.create_task(self.wsrun('wss://socket.trakteer.id/app/2ae25d102cc6cd41100a'))
        self.log = logging.getLogger("red")

        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(self.wsrun('wss://socket.trakteer.id/app/2ae25d102cc6cd41100a'))

    async def wsrun(self, uri):
        try:
            self.log.debug("[trakteer] Attempting to connect")
            self.websocket = await asyncio.wait_for(websockets.connect(uri), 30)
            while True:
                response = json.loads(await self.websocket.recv())
                self.log.debug('[trakteer] %s' % response)
                if response['event'] == 'pusher:connection_established':
                    await self.websocket.send(json.dumps({
                        "event": "pusher:subscribe",
                        "data": {"channel": "creator-stream.n8rx3ldzx7o4wamg.trstream-t6ZPmsNYQM061wcg5slw"}
                    }))
                    await self.websocket.send(json.dumps({
                        "event": "pusher:subscribe",
                        "data": {"channel": "creator-stream-test.n8rx3ldzx7o4wamg.trstream-t6ZPmsNYQM061wcg5slw"}
                    }))
                elif response['event'] == 'Illuminate\\Notifications\\Events\\BroadcastNotificationCreated':
                    donator = json.loads(response['data'])

                    embed = discord.Embed(color=0xEE2222, title='%s mentraktir %s %s' % (donator['supporter_name'], donator['quantity'], donator['unit']), timestamp=datetime.datetime.utcnow())
                    embed.url = 'https://trakteer.id/overwatch-idn/'
                    embed.description = 'Baru saja memberikan **%s**' % donator['price']
                    embed.set_thumbnail(url=donator['unit_icon'])
                    embed.add_field(name='Klik disini untuk ikut mentraktir', value='https://trakteer.id/overwatch-idn/')
                    if 'supporter_message' in donator and len(donator['supporter_message']) > 0:
                        embed.set_footer(text= donator['supporter_message'], icon_url=donator['supporter_avatar'])

                    await self.bot.get_channel(803626623596363786).send(embed=embed)
                else:
                    await self.websocket.send(json.dumps({"event": "pusher:ping", "data": {}}))
                    await asyncio.sleep(1)
        except asyncio.exceptions.TimeoutError:
            self.log.warning("[trakteer] Attempting to reconnect due to connection timeout")
            await self.wsrun(uri)
        except websockets.exceptions.ConnectionClosed:
            self.log.warning("[trakteer] Attempting to reconnect due to exception")
            await self.wsrun(uri)

    def cog_unload(self):
        self.socket_task.cancel()
        self.bot.loop.create_task(self.websocket.close())

#Trakteer(None)