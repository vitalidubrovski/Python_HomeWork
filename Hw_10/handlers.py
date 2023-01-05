import random

from aiogram.types import Message
from config import dp
import game


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(
        text=f'{message.from_user.first_name}, привет. \n'
             f'Для начала новой игры введи /new_game. \n'
             f'Для настройки количества конфет введи /total_candy и целое число. \n'
             f'Для настройки уровня сложности введи /bot_mind')


@dp.message_handler(commands=['new_game'])
async def new_game(message: Message):
    game.new_game()
    if game.get_game():
        draw = random.randint(0, 1)
        if draw:
            await player_turn(message)
        else:
            await bot_turn(message)


@dp.message_handler(commands=['total_candy'])
async def set_total(message: Message):
    if not game.get_game():
        max_total = message.text.split()
        if (len(max_total) > 1) and max_total[1].isdigit():
            game.set_max_total(int(max_total[1]))
            await message.reply(text=f'Максимальное количество конфет = {max_total[1]}')
        else:
            await message.reply(
                text='Команда для настройки максимального количества конфет. Введите /total_candy и целое число.')
    else:
        await message.reply(text='Настроить команду можно до или после игры')


@dp.message_handler(commands=['bot_mind'])
async def set_difficulty(message: Message):
    if not game.get_game():
        game.change_difficulty()
        await message.reply(text=f'Уровень сложности теперь {game.get_difficulty()}')
    else:
        await message.reply(
            text='Настроить команду можно до или после игры. Введите команду /bot_mind,чтобы изменить сложность.')


async def player_turn(message: Message):
    await message.answer(f'{message.from_user.first_name}, сколько возьмешь конфет? Твой ход')


@dp.message_handler()
async def take(message: Message):
    name = message.from_user.first_name
    if game.get_game():
        if message.text.isdigit():
            take = int(message.text)
            if (0 < take < 29) and take <= game.get_total():
                game.take_candy(take)
                if await check_win(message, take, 'player'):
                    return
                await message.answer(f'{name} взял {take} конфет. Осталось {game.get_total()} конфет. ')
                await bot_turn(message)
            else:
                await message.answer('Слишком много, возьми от 1 до 28.')


async def bot_turn(message):
    total = game.get_total()
    take = 0
    if game.get_difficulty() == 'Easy':
        if total <= 28:
            take = total
        else:
            take = random.randint(1, 29)
    else:
        if total <= 28:
            take = total
        else:
            hard = (game.get_total() - 29) % 28
            take = hard if hard > 0 else random.randint(1, 29)

    game.take_candy(take)
    await message.answer(f'Бот взял {take} конфет, осталось {game.get_total()} конфет.')
    if await check_win(message, take, 'Бот'):
        return
    await player_turn(message)


async def check_win(message, take, player: str):
    if game.get_total() <= 0:
        if player == 'player':
            await message.answer(f'{message.from_user.first_name} взял {take} и победил.')
        else:
            await message.answer(f'Бот взял {take} и победил.')
        game.new_game()
        return True
    else:
        return False
