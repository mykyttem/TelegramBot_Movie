import telebot
from telebot import types

import configure

bot = telebot.TeleBot(configure.config['token'])



@bot.message_handler(content_types=["text"])
def buttons_moviee(message):
    if message.chat.type == 'private':
        if message.text == 'Жанри/рік фільма':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Роки фільмів')
            button2 = types.KeyboardButton('Жанри фільмів')

            back = types.KeyboardButton('Назад')

            markup.add(button1, button2, back)
            bot.send_message(message.chat.id, 'Жанри фільма', reply_markup=markup)



        elif message.text == 'Роки фільмів':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Фільми - 2022')
            button2 = types.KeyboardButton('Фільми - 2021')
            button3 = types.KeyboardButton('Фільми - 2020')
            button4 = types.KeyboardButton('Фільми - 2019')
            button5 = types.KeyboardButton('Фільми - 2018')
            button6 = types.KeyboardButton('Фільми - 2017')
            button7 = types.KeyboardButton('Фільми 2016 - 2022')
            button8 = types.KeyboardButton('Фільми 2010 - 2016')
            button9 = types.KeyboardButton('Фільми 2000 - 2010')
            button10 = types.KeyboardButton('Фільми 1990 - 2000')
            button11 = types.KeyboardButton('Фільми 1980 - 1990')
            button12 = types.KeyboardButton('Фільми До 80-x')


            back = types.KeyboardButton('Назад')

            markup.add(button1, button2, button3, button4, button5, button6, button7, 
            button8, button9, button10, button11, button12, back)

            bot.send_message(message.chat.id, 'Фільми за роками', reply_markup=markup)


        elif message.text == 'Жанри фільмів':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Фільми - Екшн (бойовики)')
            button2 = types.KeyboardButton('Фільми - Детективи')
            button3 = types.KeyboardButton('Фільми - Драми')
            button4 = types.KeyboardButton('Фільми - Історичні')
            button5 = types.KeyboardButton('Фільми - Комедії')
            button6 = types.KeyboardButton('Фільми - Військові')
            button7 = types.KeyboardButton('Фільми - Спортивні')
            button8 = types.KeyboardButton('Фільми - Документальні')
            button9 = types.KeyboardButton('Фільми - Трилери')
            button10 = types.KeyboardButton('Фільми - Мелодрами')
            button11 = types.KeyboardButton('Фільми - Сімейні')
            button12 = types.KeyboardButton('Фільми - Фантастичні')
            button13 = types.KeyboardButton('Фільми - Вестерни')
            button14 = types.KeyboardButton('Фільми - Кримінальні')
            button15 = types.KeyboardButton('Фільми - Фентезійні')
            button16 = types.KeyboardButton('Фільми - Оригінал')
            button17 = types.KeyboardButton('Пригодницькі Фільми')
            button18 = types.KeyboardButton('Жахи фільми')
            button19 = types.KeyboardButton('Романтичні фільми')
            item20 = types.KeyboardButton('Студії фільми')

            back = types.KeyboardButton('Назад')

            markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12,
                        button13, button14, button15, button16, button17, button18, button19, item20, back)
            bot.send_message(message.chat.id, 'Жанри фільма', reply_markup=markup)


        elif message.text == 'Пригодницькі Фільми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button18 = types.KeyboardButton('подорож в часі')
            button19 = types.KeyboardButton('про виживання')
            button20 = types.KeyboardButton('про мандри')
            button21 = types.KeyboardButton('посапокаліпсіс')



            back = types.KeyboardButton('Назад')
            markup.add(button18, button19, button20, button21, back)
            bot.send_message(message.chat.id, 'Пригодницькі', reply_markup=markup)

        elif message.text == 'Жахи фільми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button22 = types.KeyboardButton('жахи з оскаром')
            button23 = types.KeyboardButton('буде страшно')
            button24 = types.KeyboardButton('класичні монстри')
            button25 = types.KeyboardButton('Стівен Кінг')
            

            back = types.KeyboardButton('Назад')
            markup.add(button22, button23, button24, button25, back)
            bot.send_message(message.chat.id, 'Жахи', reply_markup=markup)

        


        elif message.text == 'Романтичні фільми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button26 = types.KeyboardButton('про любов')
            button27 = types.KeyboardButton('істроії кохання')
            button28 = types.KeyboardButton('романтичні комедії')
            
            back = types.KeyboardButton('Назад')
            markup.add(button26, button27, button28, back)
            bot.send_message(message.chat.id, 'Романтичні', reply_markup=markup)

        elif message.text == 'За коміксами фільми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button29 = types.KeyboardButton('Marvel')
            button30 = types.KeyboardButton('DC Comics')
            button31 = types.KeyboardButton('По манзі та аніме')

            back = types.KeyboardButton('Назад')
            markup.add(button29, button30, button31, back)
            bot.send_message(message.chat.id, 'За коміксами', reply_markup=markup)
        

        elif message.text == 'Студії фільми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button29 = types.KeyboardButton('Warner Bros')
            button30 = types.KeyboardButton('Netflix')
            button31 = types.KeyboardButton('Legendary Pictures')
            button32 = types.KeyboardButton('SONY')

            back = types.KeyboardButton('Назад')
            markup.add(button29, button30, button31, button32, back)
            bot.send_message(message.chat.id, 'Студії', reply_markup=markup)
        

        elif message.text == '🔥🔥🔥 фільми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button29 = types.KeyboardButton('на основі реальних подій')
            button30 = types.KeyboardButton("з не очікованю розв'язкою")
            button31 = types.KeyboardButton('психологічні фільми')
            

            back = types.KeyboardButton('Назад')
            markup.add(button29, button30, button31, back)
            bot.send_message(message.chat.id, '🔥🔥🔥', reply_markup=markup)
        
