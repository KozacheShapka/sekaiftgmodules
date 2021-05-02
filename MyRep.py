from .. import loader, utils

@loader.tds
class MyRepMod(loader.Module):
    """Модуль с вашей репутацией | creator seen"""
    strings={"name":"Май rep"}

    async def client_ready(self, message, db):
        self.db=db
        self.db.set("MyRep", "repstatus", True)

    async def repcmd(self, message):
        """Включить режим репутаций."""
        repstatus = self.db.get("MyRep", "repstatus")
        if repstatus is not True:
            self.db.set("MyRep", "repstatus", True)
            await message.edit(f"<b>[MyRepMod] ✅Включено!</b>")
        else:
            self.db.set("MyRep", "repstatus", False)
            await message.edit(f"<b>[MyRepMod] ❌Выключено!</b>")

    async def myrepcmd(self, message):
        """Посмотреть свою репутацию. Используй: .myrep clear (очистка репутации)."""
        args = utils.get_args_raw(message)
        if args == "clear":
            self.db.set("MyRep", "my_repa", 0)
            return await message.edit("<b>[MyRepMod] ✅Репутация успешно очищена!</b>")
        myrep = self.db.get("MyRep", "my_repa")
        repstatus = self.db.get("MyRep", "repstatus")
        if repstatus is not False:
            msg_repstatus = "[<i>✅</i>]"
        else:
            msg_repstatus = "[<i>❌</i>]"
        await message.edit(f"♻️ <b>[</b><i>MyRepMod</i><b>]</b> ♻️\n<b>Статус режима: </b>{msg_repstatus}<b>\nКол-во моих репутации: <i>{myrep}</i>.</b>")

    async def watcher(self, message):
        try:
            number = self.db.get("MyRep", "my_repa", 0)
            repstatus = self.db.get("MyRep", "repstatus")
            if message.mentioned:
                if message.text == "+":
                    if repstatus is not False:
                        number += 1
                        self.db.set("MyRep", "my_repa", number)
                        await message.reply(f"<b>⭐️ПОВЫШЕНИЕ РЕПУТАЦИИ!⭐️ \nСпасибо что повысил мою репутацию❤️ \nТеперь у меня: {number} репутации!</b>")
                    else:
                        await message.edit(f"[MyRepMod] Отключен.")
        except: pass