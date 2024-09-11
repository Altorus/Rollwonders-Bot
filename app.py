import pdb

from aiogram import Bot, Router, Dispatcher, types
import asyncio
import logging
from aiogram import filters

router = Router()


@router.message(filters.CommandStart())
async def send_web_app(msg: types.Message, command: filters.CommandStart):
    web_app_button = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Открыть приложение",
                                           web_app=types.WebAppInfo(url="https://mhand.ru/")),
            ]
        ]
    )
    await msg.answer(
        text="Добро пожаловать в приложение Rollwonders",
        reply_markup=web_app_button
    )


async def set_web_app_menu_button(bot: Bot):
    menu_button = types.MenuButtonWebApp(
        text="Создать рецепт",
        web_app=types.WebAppInfo(url="https://mhand.ru/about/")
    )

    await bot.set_chat_menu_button(menu_button=menu_button)


async def main():
    bot = Bot("7206171797:AAH5BKRIstM3Xfy-3bPs7Z8fIz6RICCuNJo")
    logging.basicConfig(level=logging.DEBUG)
    dp = Dispatcher()

    dp.include_router(router)

    await set_web_app_menu_button(bot)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
