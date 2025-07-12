from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

# Токен и ID админа
BOT_TOKEN = "7713969328:AAFJro-iiBcWhm5gcULXCHACmNSj-cWpBIU"
ADMIN_ID = 6091849057

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Ссылка на Mini App
MINI_APP_URL = "https://giveaway-app-production.up.railway.app"

# Команда /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Используй `/app`, чтобы участвовать в розыгрыше",
    )

# Команда /app — отправляет кнопку Web App
@dp.message(F.text == "/app")
async def open_app(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Участвовать", web_app={"url": MINI_APP_URL})]
    ])
    await message.answer("Открыть мини-приложение:", reply_markup=keyboard)

# Инлайн-режим (синяя кнопка Play)
@dp.inline_query()
async def inline_app(query: InlineQuery):
    result = InlineQueryResultArticle(
        id="1",
        title="Участвовать в розыгрыше",
        input_message_content=InputTextMessageContent(
            message_text="Нажмите на кнопку ниже, чтобы участвовать:"
        ),
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🎮 Участвовать", web_app={"url": MINI_APP_URL})]
        ]),
    )
    await query.answer(results=[result], cache_time=1)

# Точка входа
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())