import logging

from aiogram import Bot, Dispatcher, executor, types


TOKEN = '5956035637:AAEbxPzOZiayOEgORc2LN7lOfcStNQ0YzN0'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
