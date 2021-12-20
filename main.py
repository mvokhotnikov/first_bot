import telebot
from telebot import types
import config
from datetime import datetime
from data_base import free_dates as f_d
from data_base import register_date as r_d
from data_base import finish as clean_all

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    """

    :param message:
    Данный параметр является командой к началу работы бота(/start)
    В этой функции мы отправляем приветсявие и добавляем клавиатуру с разрешенными сообщениями

    """
    """ В терминале выводим данные пользователя """
    config.chat_id[message.chat.id] = [2]
    """ В словаре создаем список необходимых значений для определенного юзера и добавляем в него счетчик "Да" """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем клавиатуру с "Да" и "Выйти"
    item1 = types.KeyboardButton('Да')
    item2 = types.KeyboardButton('Выйти')
    markup.add(item1, item2)  # Закончили создавать
    hour_now = int(datetime.now().strftime('%H:%M:%S')[:2])  # Находим который час
    config.chat_id[message.chat.id].append(
        message.from_user.first_name)  # В словарь добавляем в список имя пользователя"
    config.chat_id[message.chat.id].append(
        message.from_user.last_name)  # В словарь добавляем в список фамилию пользователя"
    if 5 <= hour_now <= 11:
        hello = 'Доброе утро, '
    elif 12 <= hour_now <= 16:
        hello = 'Добрый день, '
    elif 17 <= hour_now <= 23:
        hello = 'Добрый вечер, '
    else:
        hello = 'Здравствуйте, '
    bot.send_message(message.chat.id,
                     hello + '{0.first_name} {0.last_name}\nВы желаете записаться на одну из наших секций?'.format(
                         message.from_user), parse_mode='html', reply_markup=markup)  #
    # Отправили в боте сообщение с приветсвием и закрепили клавиатура с "Да" и "Выйти"


@bot.message_handler(content_types=['text'])
def kkk(message):
    """

    :param message:
    В зависимости от команды мы либо предоставляем список клубов, либо выходим
    """
    if message.chat.type == 'private':
        if message.text == 'Выйти':  # Если сообщение 'Выйти', то прощаемся с пользователем, добавляем кнопку '/start'
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item = types.KeyboardButton('/start')
            markup.add(item)
            bot.send_message(message.chat.id, 'Всего вам хорошего', reply_markup=markup)
            clean_all(message.chat.id)  # Удаляем из словарь с данными пользователя
        elif message.text == 'Да' and config.chat_id[message.chat.id][0] == 2:  #
            # Пользователь хочет узнать список курсов, значит отправляем ему этот список
            config.chat_id[message.chat.id][0] = 1  # Изменяем счетчик с 2 до 1
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(config.club1, callback_data='Клуб 1')
            item2 = types.InlineKeyboardButton(config.club2, callback_data='Клуб 2')
            item3 = types.InlineKeyboardButton(config.club3, callback_data='Клуб 3')
            markup.add(item1).add(item2).add(item3)
            config.chat_id[message.chat.id].append(markup)  # Добавим в наш словарь структуру markup со списком курсов
            bot.send_message(message.chat.id, 'Выберите ваш курс', reply_markup=markup)
        elif message.text == 'Да' and config.chat_id[message.chat.id][0] == 1:  # Пользователь хочет узнать свободное
            # время для данного курса, значит отправляем ему этот список
            config.chat_id[message.chat.id][0] = 0  # Изменяем счетчик с 2 до 1
            config.chat_id[message.chat.id].append(f_d(config.chat_id[message.chat.id][4]))
            markup = types.InlineKeyboardMarkup(row_width=len(config.chat_id[message.chat.id][5]))  #
            # В словаре под индексом 5 находится список свободного времени для определенного курса
            for date in config.chat_id[message.chat.id][5]:
                item = types.InlineKeyboardButton(date[0], callback_data=date[0])
                markup.add(item)
            bot.send_message(message.chat.id, 'Выберете дату', reply_markup=markup)

        else:
            bot.send_message(message.chat.id, 'Я не знаю, что ответить')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    """
    Данная функция отвечает за ловлю инлайновских сообщений.
    В ней мы предоставляем описание курсов или записываем на него
    """
    try:
        if call.message:
            if call.data == 'Клуб 1':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton('Раскрыть', callback_data='Раскрыть')
                markup.add(item)
                wish = 'Желаете записаться?'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=config.club1 + '\n' + config.club1_description + '\n' + wish,
                                      reply_markup=markup)
                if len(config.chat_id[call.message.chat.id]) == 4:
                    config.chat_id[call.message.chat.id].append(config.club1)  # Добавляем название курса в словарь
                else:
                    config.chat_id[call.message.chat.id][4] = config.club1  # Изменяем название курса в словаре
            elif call.data == 'Клуб 2':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton('Раскрыть', callback_data='Раскрыть')
                markup.add(item)
                wish = 'Желаете записаться?'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=config.club2 + '\n' + config.club2_description + '\n' + wish,
                                      reply_markup=markup)
                if len(config.chat_id[call.message.chat.id]) == 4:
                    config.chat_id[call.message.chat.id].append(config.club2)  # Добавляем название курса в словарь
                else:
                    config.chat_id[call.message.chat.id][4] = config.club2  # Изменяем название курса в словаре
            elif call.data == 'Клуб 3':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item = types.InlineKeyboardButton('Раскрыть', callback_data='Раскрыть')
                markup.add(item)
                wish = 'Желаете записаться?'
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text=config.club3 + '\n' + config.club3_description + '\n' + wish,
                                      reply_markup=markup)
                if len(config.chat_id[call.message.chat.id]) == 4:
                    config.chat_id[call.message.chat.id].append(config.club3)  # Добавляем название курса в словарь
                else:
                    config.chat_id[call.message.chat.id][4] = config.club3  # Изменяем название курса в словаре
            elif call.data == 'Раскрыть':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Список курсов',
                                      reply_markup=config.chat_id[call.message.chat.id][3])  #
                # Вставляем зарание сохраненный в словарь markup
            else:  #
                # Человек выбрал время для определенного курса. Записываем человека.
                config.chat_id[call.message.chat.id].append(call.data)  # Добавили в словарь конкретное время
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item = types.KeyboardButton('/start')
                markup.add(item)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Спасибо, что записались к нам',
                                      reply_markup=None)
                bot.send_message(call.message.chat.id, 'Надеемся увидеть вас вновь', reply_markup=markup)
                r_d(config.chat_id[call.message.chat.id][4], config.chat_id[call.message.chat.id][6],
                    config.chat_id[call.message.chat.id][2], config.chat_id[call.message.chat.id][1],
                    config.chat_id[call.message.chat.id][5])  #
                # Запускаем функцию для записи (курс, дата, фамилия, имя, список свободных времен)
                clean_all(call.message.chat.id)  # Удаляем из словарь с данными пользователя

    except Exception as e:
        print(e)


# RUN
if __name__ == '__main__':
    bot.polling(none_stop=True, skip_pending=True)
