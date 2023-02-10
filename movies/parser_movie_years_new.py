import telebot

import requests
from bs4 import BeautifulSoup

import random
import fake_useragent

import configure

bot = telebot.TeleBot(configure.config['token'])

@bot.message_handler(content_types=["text"])
def movie_year(message):
    if message.chat.type == 'private':
        for i in range(5):
            try:
                if message.text == 'Фільми - 2022':
                    page = random.randint(1, 10)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми - 2022', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

                if message.text == 'Фільми - 2021':
                    page = random.randint(1, 14)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми - 2021', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

                if message.text == 'Фільми - 2020':
                    page = random.randint(1, 15)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми - 2020', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - 2019':
                    page = random.randint(1, 22)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми - 2020', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - 2018':
                    page = random.randint(1, 22)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми - 2020', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - 2017':
                    page = random.randint(1, 19)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми - 2017', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми 2016 - 2022':
                    # FIXME 
                    page = random.randint(1, 115)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми 2016 - 2022', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми 2010 - 2016':
                    page = random.randint(1, 98)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми 2010 - 2016', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

            
                if message.text == 'Фільми 2000 - 2010':
                    page = random.randint(1, 98)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми 2000 - 2010', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

    

                if message.text == 'Фільми 1990 - 2000':
                    page = random.randint(1, 69)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми 1990 - 2000', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

    

                if message.text == 'Фільми 1980 - 1990':
                    page = random.randint(1, 34)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми 1980 - 1990', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми До 80-x':
                    page = random.randint(1, 27)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_year('Фільми До 80-x', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

            except telebot.apihelper.ApiException:
                bot.send_message(message.chat.id, "Вибач, немає :(\n" + "Можеш спробувати ще раз натиснути😀")
                            

def parse_movies_by_year(year, page):
    if year == 'Фільми - 2022':
        url = "https://uakino.club/filmy/f/c.year=2022,2022/sort=date;desc/page/"
    elif year == 'Фільми - 2021':
        url = "https://uakino.club/filmy/f/c.year=2021,2021/sort=date;desc/page/"
    elif year == 'Фільми - 2020':
        url = "https://uakino.club/filmy/f/c.year=2020,2020/sort=date;desc/page/"
    elif year == 'Фільми - 2019':
        url = "https://uakino.club/filmy/f/c.year=2019,2019/sort=date;desc/page/" 
    elif year == 'Фільми - 2018':
        url = "https://uakino.club/filmy/f/c.year=2018,2018/sort=date;desc/page/"
    elif year == 'Фільми - 2017':
        url = "https://uakino.club/filmy/f/c.year=2017,2017/sort=date;desc/page/"
    elif year == 'Фільми 2016 - 2022':

        # FIXME
        url = "https://uakino.club/filmy/f/c.year=2017,2017/sort=date;desc/page/"

        
    elif year == 'Фільми 2010 - 2016':
        url = "https://uakino.club/filmy/f/c.year=2010,2016/sort=date;desc/page/"
    elif year == 'Фільми 2000 - 2010':
        url = "https://uakino.club/filmy/f/c.year=2000,2010/sort=date;desc/page/"
    elif year == 'Фільми 1990 - 2000':
        url = "https://uakino.club/filmy/f/c.year=1990,2000/sort=date;desc/page/"
    elif year == 'Фільми 1980 - 1990':
        url = "https://uakino.club/filmy/f/c.year=1980,1990/sort=date;desc/page/"
    elif year == 'Фільми До 80-x':
        url = "https://uakino.club/filmy/f/c.year=1921,1980/sort=date;desc/page/"


    # TODO: Add other years handling
    
    url_new = url + str(page)

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    response = requests.get(url_new, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", class_="content-box clearfix")
    for movie in section:
        movie = movie.find_all("div", class_="movie-item short-item")
        for item in movie:
            movie_name = item.find("a", class_="movie-title").get_text(strip=True)
            movie_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                
            quality = item.find("div", class_="full-quality").get_text(strip=True)

            movie_description = item.find("span", class_="desc-about-text").get_text(strip=True)

            return movie_name, movie_img, quality, movie_description