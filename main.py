import logging

from aiogram import Bot, Dispatcher, executor, types

token = '1061746452:AAFLmh9nt4I43cwKRCZXkVZ1UZxSc4TZXi0'


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
	await message.answer(message.text)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)	