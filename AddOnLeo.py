#clown... again :/ by @Sekai_Yoneya

from asyncio import sleep
import random
from telethon import functions
from userbot.events import register
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events
from .. import loader, utils

def register(cb):
    cb(AddOnLeoMod())

class AddOnLeoMod(loader.Module):
    """Дополнения к Леонардо Дайвинчику"""
    strings = {'name': 'AddOnLeo'}

    def init(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client

    async def afkcmd(self, event):
        chat = '@leomatchbot'
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users= 1234060895 ))
                await event.client.send_message(chat, '💤')
                response = await response
            except YouBlockedUserError:
                await event.edit('<code>Разблокируй @leomatchbot</code>')
                return
            await event.edit(response.text)