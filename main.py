from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import (
    Message,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# Токен и настройки
BOT_TOKEN = "7713969328:AAFJro-iiBcWhm5gcULXCHACmNSj-cWpBIU"
ADMIN_ID = 6091849057
MINI_APP_URL = "https://giveaway-app.up.railway.app "

# Бот и диспетчер
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Используйте `/app`, чтобы участвовать в розыгрыше")

# Команда /app — отправляет кнопку Web App
@dp.message(Command("app"))
async def open_app(message: Message):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Участвовать", web_app={"url": MINI_APP_URL})
    ])
    await message.answer("Открыть мини-приложение:", reply_markup=markup)

# Инлайн-режим — синяя кнопка Play
@dp.inline_query()
async def inline_query_handler(query: InlineQuery):
    result = InlineQueryResultArticle(
        id="1",
        title="Участвовать",
        input_message_content=InputTextMessageContent(
            message_text="Нажмите на кнопку ниже, чтобы участвовать:"
        ),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🎮 Участвовать", web_app={"url": MINI_APP_URL})]
        ]),
    )
    await query.answer(results=[result], cache_time=1)