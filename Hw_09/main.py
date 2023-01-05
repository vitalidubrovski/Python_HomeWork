from aiogram import executor
from handlers import dp


async def on_startup(_):
    print('Бот запущен.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# homework_candy_bot название бота, ключ оставил внутри.
# 5989854134:AAFM7UAUdJsBNLfXkuw4vN4wS_U3CzSKkjg
