# import pytest
# import telebot
# from telebot import types
# import time
#
# import config
# import main
# from main import bot as tb
#
#
# @pytest.mark.skipif(True, reason="No environment variables configured")
# class TestTeleBot:
#     def test_message_handler_start(self):
#         @tb.message_handler(commands=['start'])
#         def command_handler(message):
#             pass
#         assert '1' == '1'
#         return 0
#
#     def test_message_handler_finish(self):
#         @tb.message_handler(commands=['start'])
#         def command_handler(message):



# import unittest
# from telebot import types
# from unittest.mock import Mock
# import main as bot
#
#
# class MyTestCase(unittest.TestCase):
#     async def test_something(self):
#         message = unittest.mock.AsyncMock()
#         msg = bot.welcome(message)
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем клавиатуру с "Да" и "Выйти"
#         item1 = types.KeyboardButton('Да')
#         item2 = types.KeyboardButton('Выйти')
#         markup.add(item1, item2)
#         bot.bot.send_message(msg.chat.id, 'Я не знаю, что ответить')(
#             text="Привет, я Бот-повар\nЯ создан для того, чтобы помочь тебе найти простые рецепты, кроме доширака",
#             reply_markup=markup)


# class MyTestCase(unittest.TestCase):
#     async def test_something(self):
#         message = unittest.mock.AsyncMock()
#         await bot.kkk(message)
#         message.answer.assrt_called_with(text="У нас представлены некоторые рецепты. \n"
#                                               "Выберете, что у вас есть в холодильнике", reply_markup=bot.rec)


if __name__ == '__main__':
    pytest.main()
