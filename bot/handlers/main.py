from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import html, Router

from bot.dispatcher import dp

main_router = Router()
@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
