from aiogram import Bot, Router, Dispatcher, types
import asyncio
import logging
import aiohttp
from aiogram import Bot, Router, Dispatcher, types
from aiogram.filters import CommandStart

router = Router()

@router.message(CommandStart())
async def send_web_app(msg: types.Message, command: CommandStart):
    await msg.answer(
        text="Добро пожаловать в бот для лидов",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text="Открыть приложение",
                                      web_app=types.WebAppInfo(url=f"https://mhand.ru/"))]
            ],
            resize_keyboard=True
        )
    )


async def main():
    bot = Bot("7206171797:AAH5BKRIstM3Xfy-3bPs7Z8fIz6RICCuNJo")
    logging.basicConfig(level=logging.DEBUG)
    dp = Dispatcher()

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
