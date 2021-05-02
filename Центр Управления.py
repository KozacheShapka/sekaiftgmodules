from .. import loader
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon import events

class CenterBotMod(loader.Module):
    """Центр упраления @YoneyaBS_bot"""
    strings = {'name': 'Центр управления'}

    async def restartbotcmd(self, message):
        """Перезапуск бота"""
        chat = 'yoneyabs_bot'
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users= 1705701465 ))
                await message.client.send_message(chat, '/restart')
                response = await response
            except YouBlockedUserError:
                return await message.edit('<code>Разблокируй @yoneyabs_bot</code>')
            await message.client.send_file(message.to_id, response.media)
            
    async def pingbotcmd(self, message):
        """Пинг бота"""
        chat = 'yoneyabs_bot'
        async with message.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True, from_users= 1705701465 ))
                await message.client.send_message(chat, '/ping')
                response = await response
            except YouBlockedUserError:
                return await message.edit('<code>Разблокируй @yoneyabs_bot</code>')
            await message.client.send_file(message.to_id, response.media)