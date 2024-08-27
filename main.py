import os
import datetime
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.dispatcher import dispatcher
from aiogram.types import Message

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

async def send_message_every_10_sec():
   
    await bot.send_message(chat_id=os.getenv('ID'), text='H3110 FR13ND')
    while True:
        await bot.send_message(chat_id=os.getenv('ID'), text=datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'), disable_notification=True)
        await asyncio.sleep(10)

async def main():
    asyncio.create_task(send_message_every_10_sec())
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
