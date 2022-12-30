import time
import logging

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

TOKEN = "5676282322:AAHAP7zm_yGLrTfz8WqNySmzmdalP6OXmFQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)




# Запуск бота
# Запуск бота и вопрос.
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="ДА Code'ил"),
            types.KeyboardButton(text="НЕТ не Code'ил")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="ПОЛОЖИТЕЛЬНЫЙ ОТВЕТ?)))")
    # Вопрос на после старта бота
    await message.answer(f'Проограммировал ли ты сегодня?', reply_markup=keyboard)


# 1.1.1)  Первый вопрос, первого ответа!
@dp.message_handler(lambda message: message.text == "ДА Code'ил")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Один час"),
            types.KeyboardButton(text="Два часа")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Продолжай в том же духе!!!")
    # await message.reply("ОЧЕНЬ ХОРОШО,ТЫ МОЛОДЕЦ!", reply_markup=keyboard)
    await message.answer(f'ОЧЕНЬ ХОРОШО,ТЫ МОЛОДЕЦ!', reply_markup=keyboard)
    await message.answer(f'Сколько времени программировал?', reply_markup=keyboard)


# 1.2.1) Первый вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "НЕТ не Code'ил")
async def without_puree(message: types.Message):
    for i in range(7):
        print(i)
        time.sleep(0.5)
        await message.answer("ОЧЕНЬ ПЛОХО!")


# 2.1.1 Второй вопрос, первого ответа!
@dp.message_handler(lambda message: message.text == "Один час")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Да, МОГУ!!!"),
            types.KeyboardButton(text="Нет, времени нет")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Ты идешь на вершину!")
    # await message.reply("Никто, кроме тебя, этого не сделает!", reply_markup=keyboard)
    await message.answer(f'Ты движишся в нужном направление!', reply_markup=keyboard)
    await message.answer(f'Мог бы больше?', reply_markup=keyboard)


# 2.2.1 Второй вопрос, первого ответа!
@dp.message_handler(lambda message: message.text == "Да, МОГУ!!!")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Да"),
            types.KeyboardButton(text="Нет")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Какой ты молодец")
    # await message.reply("Никто, кроме тебя, этого не сделает!", reply_markup=keyboard)
    await message.answer(f"Будешь каждый день Code'ить? ", reply_markup=keyboard)


# 3.2.1 Третий вопрос, третьего ответа!
@dp.message_handler(lambda message: message.text == "Да, МОГУ!!!")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Да"),
            types.KeyboardButton(text="Нет")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Ты Лучший!!!")
    # await message.reply("Никто, кроме тебя, этого не сделает!", reply_markup=keyboard)
    await message.answer(f"Будешь каждый день Code'ить ?", reply_markup=keyboard)


# 1.3.1) Первый вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "Нет, времени нет")
async def without_puree(message: types.Message):
    for i in range(7):
        print(i)
        time.sleep(0.5)
        await message.answer("Ищи ВРЕМЯ!!!")


# 2.3.1 Второй вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "Я это сделал!")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Еще чуть чуть"),
            types.KeyboardButton(text="Я уже прогер")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Продолжай!!")
    await message.answer("Очень даже не плохо)", reply_markup=keyboard)
    await message.answer(f'Будешь стримиться к лучшему', reply_markup=keyboard)


# 2.4.1 Второй вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "Еще чуть чуть")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Еще долго"),
            types.KeyboardButton(text="Уже сделал")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Продолжай!!")
    await message.answer("Очень даже не плохо)", reply_markup=keyboard)
    await message.answer(f'Будешь стримиться к лучшему', reply_markup=keyboard)


# 2.5.1 Второй вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "Еще долго")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Уже сделал"),
            types.KeyboardButton(text="Давай быстрее")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Продолжай!!")
    await message.answer("Ты становишься лучше)", reply_markup=keyboard)
    await message.answer(f'Стримитремись к лучшему', reply_markup=keyboard)


# 2.2.1 Второй вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "Два часа")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я это сделал!"),
            types.KeyboardButton(text="Получиться ЛУЧШЕ!")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Продолжай!!")
    await message.answer("Очень даже не плохо)", reply_markup=keyboard)
    await message.answer(f'Еще часок добавим?', reply_markup=keyboard)


# 2.6.1 Второй вопрос, второго ответа!
@dp.message_handler(lambda message: message.text == "Получиться ЛУЧШЕ")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Да получиться"),
            types.KeyboardButton(text="нет не получится")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Продолжай!!")
    await message.answer("Очень)", reply_markup=keyboard)
    await message.answer(f'Еще ?', reply_markup=keyboard)


# 3.2.1 Третий вопрос, третьего ответа!
@dp.message_handler(lambda message: message.text == "Да")
async def with_puree(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Программист!"),
            types.KeyboardButton(text="Нет")
        ],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb,
                                         resize_keyboard=True,
                                         input_field_placeholder="Ты Лучший!!!")
    # await message.reply("Никто, кроме тебя, этого не сделает!", reply_markup=keyboard)
    await message.answer(f"ТЫ программист!)", reply_markup=keyboard)
    await message.answer(f"Уже программист", reply_markup=keyboard)


# 3.4.1 Четвертый вопрос, третьего ответа!
@dp.message_handler(lambda message: message.text == "Программист!")
async def with_puree(message: types.Message):
    for i in range(7):
        print(i)
        time.sleep(0.5)
        await message.answer("Теперь ты программист!")
    #     await message.answer("Теперь ты Лучший!")
    # await message.reply("Никто, кроме тебя, этого не сделает!", reply_markup=keyboard)





if __name__ == "__main__":
    executor.start_polling(dp)
