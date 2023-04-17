from aiogram.dispatcher.filters import BoundFilter
from aiogram import types

from main_bot.middlewares import i18n
from main_bot.database import User


class WeatherCurrentWord(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        language = await User.select('language').where(
            User.id == message.from_user.id).gino.scalar()
        return i18n.gettext('current weather', locale=language) + '🌤' == message.text
