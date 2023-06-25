from aiogram import types
from aiogram.types import BotCommandScopeDefault


async def set_default_commands(bot):
    return await bot.set_my_commands(
        commands=[
            types.BotCommand('start', 'Start'),
        ],
        scope=BotCommandScopeDefault(),
    )
