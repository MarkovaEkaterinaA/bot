import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
import logging
from handlers import common, carier_choice





async def main():
    #Включаем логгирование
    logging.basicConfig(level=logging.INFO)

    #Создаем объект бота
    bot = Bot(token=config.token)

    #Диспетчер
    dp = Dispatcher()

    dp.include_router(carier_choice.router)
    dp.include_router(common.router)


    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run (main())
      

