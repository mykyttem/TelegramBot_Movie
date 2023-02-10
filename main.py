import telebot
from telebot import types

import requests
from bs4 import BeautifulSoup
import fake_useragent
import random

# import from folder movie
from movies.buttons_movie import buttons_moviee
# from movies.parser_movie_years import movie_year
from movies.parser_movie import genre_movie
from movies.parser_movie_years_new import movie_year

# import from folder series
from series.buttons_series import buttons_seriess
from series.parser_series import genre_series
from series.parser_series_year import year_series

import configure

bot = telebot.TeleBot(configure.config['token'])

# FIXME щось з жанром "субтитри не так" у серіалів


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard =  True)
    

    button0 = types.KeyboardButton('Останні надходження')
    button1 = types.KeyboardButton('Жанри/рік фільма')
    button2 = types.KeyboardButton('Жанри/рік серіалів')
    button3 = types.KeyboardButton('Всі серіали')
    button4 = types.KeyboardButton('Всі фільми')

    
    markup.add(button0, button1, button2, button3, button4)

    bot.send_message(message.chat.id, 'Привіт, я бот', reply_markup = markup)

 


@bot.message_handler(content_types=["text"])
def buttons(message):

    # Using fuction from files

    buttons_moviee(message)
    movie_year(message)
    genre_movie(message)

    buttons_seriess(message)
    genre_series(message)
    year_series(message)

    
    if message.chat.type == 'private':
        if message.text == 'Останні надходження':
            url = "https://uakino.club/page/"
            number = random.randint(1, 1239)
            urlls = url + str(number)

            user = fake_useragent.UserAgent().random
            header = {'user-agent': user}
            response = requests.get(urlls, headers=header)

            soup = BeautifulSoup(response.text, "html.parser")

            section = soup.find_all("div", class_="right-side")
            for movie in section:
                movie = movie.find_all("div", class_="movie-item short-item")
                for item in movie:
                    series_name = item.find("a", class_="movie-title").get_text(strip=True)
                    series_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                           
                    quality = item.find("div", class_="full-quality").get_text(strip=True)

                    series_description = item.find("span", class_="desc-about-text").get_text(strip=True)


                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nЯкість: " + quality + "\nОпис: " + series_description)
   


        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton('Останні надходження')
            button2 = types.KeyboardButton('Жанри/рік фільма')
            button3 = types.KeyboardButton('Жанри/рік серіалів')
            button4 = types.KeyboardButton('Всі серіали')
            button5 = types.KeyboardButton('Всі фільми')
            markup.add(button1, button2, button3, button4, button5)

            bot.send_message(message.chat.id, 'Привіт, знову', reply_markup = markup)



bot.polling(none_stop=True)