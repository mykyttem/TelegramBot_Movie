import telebot
from telebot import types

import configure

bot = telebot.TeleBot(configure.config['token'])


@bot.message_handler(content_types=["text"])
def buttons_seriess(message):
    if message.chat.type == 'private':
        if message.text == 'Жанри/рік серіалів':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Роки серіалів')
            button2 = types.KeyboardButton('Жанри серіалів')

            back = types.KeyboardButton('Назад')

            markup.add(button1, button2, back)
            bot.send_message(message.chat.id, 'Жанри фільма', reply_markup=markup)

        elif message.text == 'Жанри серіалів':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button29 = types.KeyboardButton('Мелодрами')
            button30 = types.KeyboardButton("Детективи")
            button31 = types.KeyboardButton('Драми')
            button32 = types.KeyboardButton('Комедії')
            button33  = types.KeyboardButton("Історичні")
            button34  = types.KeyboardButton('Фантастичні')
            button35 = types.KeyboardButton('Дорами')
            button36 = types.KeyboardButton("Турецькі")
            button37 = types.KeyboardButton('Пригодницькі')
            button38 = types.KeyboardButton('Трилери')
            button39 = types.KeyboardButton('Жахи')
            button40 = types.KeyboardButton('Субтитри')
            button41 = types.KeyboardButton('Реальні події')
            button42 = types.KeyboardButton('Топ міні-серіали')
            button44 = types.KeyboardButton('За коміксами Marvel')
            button45 = types.KeyboardButton('Netional Geographic')
            button46 = types.KeyboardButton('BBC')
            button47 = types.KeyboardButton('Студії - Netflix')
            button48 = types.KeyboardButton('Студії - HBO')
            button49 = types.KeyboardButton('Студії - THE CW')



            back = types.KeyboardButton('Назад')
            markup.add(button29, button30, button31, button32, button33, button34, button35, button36, button37, button38, button39, button40,
             button41, button42, button44, button45, button46, button47, button48, button49, back)
            bot.send_message(message.chat.id, '🔥🔥🔥', reply_markup=markup)



        elif message.text == 'Роки серіалів':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('2022')
            button2 = types.KeyboardButton('2021')
            button3 = types.KeyboardButton('2020')
            button4 = types.KeyboardButton('2019')
            button5 = types.KeyboardButton('2018')
            button6 = types.KeyboardButton('2017')
            button7 = types.KeyboardButton('2016 - 2022')
            button8 = types.KeyboardButton('2010 - 2016')
            button9 = types.KeyboardButton('2000 - 2010')
            button10 = types.KeyboardButton('1990 - 2000')
            button11 = types.KeyboardButton('1980 - 1990')
            button12 = types.KeyboardButton('До 80-x')


            back = types.KeyboardButton('Назад')

            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, back)
            bot.send_message(message.chat.id, 'Фільми за роками', reply_markup=markup)

