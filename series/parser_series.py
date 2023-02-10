import telebot

import requests
from bs4 import BeautifulSoup

import random
import fake_useragent

import configure

bot = telebot.TeleBot(configure.config['token'])

@bot.message_handler(content_types=["text"])
def genre_series(message):
    if message.chat.type == 'private':
        for i in range(5):
            try:
                if message.text == 'Мелодрами':
                    page = random.randint(1, 43)
                    series_name, series_img, season, quality, series_description = parse_seriees('Мелодрами', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)
                            

                if message.text == 'Детективи':
                    page = random.randint(1, 99)
                    series_name, series_img, season, quality, series_description = parse_seriees('Детективи', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Драми':
                    page = random.randint(1, 255)
                    series_name, series_img, season, quality, series_description = parse_seriees('Драми', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Комедії':
                    page = random.randint(1, 96)
                    series_name, series_img, season, quality, series_description = parse_seriees('Комедії', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Історичні':
                    page = random.randint(1, 15)
                    series_name, series_img, season, quality, series_description = parse_seriees('Історичні', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Фантастичні':
                    page = random.randint(1, 69)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Фантастичні', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Дорами':
                    page = random.randint(1, 4)
                    series_name, series_img, season, quality, series_description = parse_seriees('Дорами', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Турецькі':
                    page = random.randint(1, 2)
                    series_name, series_img, season, quality, series_description = parse_seriees('Турецькі', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Пригодницькі':
                    page = random.randint(1, 50)
                    series_name, series_img, season, quality, series_description = parse_seriees('Пригодницькі', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Трилери':
                    page = random.randint(1, 82)
                    series_name, series_img, season, quality, series_description = parse_seriees('Трилери', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Жахи':
                    page = random.randint(1, 24)
                    series_name, series_img, season, quality, series_description = parse_seriees('Жахи', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Субтитри':
                    try:
                        page = random.randint(1, 20)
                        series_name, series_img, season, quality, series_description = parse_seriees('Субтитри', page)
                        bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)
                    except AttributeError:
                        bot.send_message(message.chat.id, "Помилка =(")



                if message.text == 'Реальні події':
                    page = random.randint(1, 3)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Реальні події', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Топ міні-серіали':
                    page = random.randint(1, 2)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Топ міні-серіали', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


    
                if message.text == 'За коміксами Marvel':
                        page = None
                        series_name, series_img, season, quality, series_description = parse_seriees_other_html('За коміксами Marvel', page)
                        bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == 'Netional Geographic':
                    page = random.randint(1, 2)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Netional Geographic', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


        
                if message.text == 'BBC':
                    page = random.randint(1, 3)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('BBC', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Студії - Netflix':
                    page = random.randint(1, 8)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Студії - Netflix', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Студії - HBO':
                    page = random.randint(1, 2)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Студії - HBO', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Студії - THE CW':
                    page = random.randint(1, 2)
                    series_name, series_img, season, quality, series_description = parse_seriees_other_html('Студії - THE CW', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'Всі серіали':
                    page = random.randint(1, 80)
                    series_name, series_img, season, quality, series_description = parse_seriees('Фантастичні', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


            except telebot.apihelper.ApiException:
                bot.send_message(message.chat.id, "Вибач, немає :(\n" + "Можеш спробувати ще раз натиснути😀")


def parse_seriees(jannre, page):
    if jannre == 'Мелодрами':
        url = "https://uakino.club/seriesss/love_story_series/page/"
    elif jannre == 'Детективи':
        url = "https://uakino.club/seriesss/detective_series/page/"
    elif jannre == 'Драми':
        url = "https://uakino.club/seriesss/drama_series/page/"
    elif jannre == 'Комедії':
        url = "https://uakino.club/seriesss/comedy_series/page/"
    elif jannre == 'Історичні':
        url = "https://uakino.club/seriesss/historical_series/page/"     
    elif jannre == 'Дорами':
        url = "https://uakino.club/seriesss/doramy/page/"
    elif jannre == 'Турецькі':
        url = "https://uakino.club/seriesss/turecki-serialy/page/"
    elif jannre == 'Пригодницькі':
        url = "https://uakino.club/seriesss/adventure_series/page/"
    elif jannre == 'Трилери':
        url = "https://uakino.club/seriesss/thriller_series/page/"        
    elif jannre == 'Жахи':
        url = "https://uakino.club/seriesss/horror_series/page/"
    elif jannre == 'Субтитри':
        url = "https://uakino.club/seriesss/subtitle-serials/page/"
    elif jannre == 'Всі серіали':
        url = "https://uakino.club/seriesss/page/"

    
    # FIXME "За коміксами Marvel"
    # FIXME "Всі серіали"


    new_url = url + str(page)

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    
    response = requests.get(new_url, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", class_="coloredgray")
    for series in section:
        series = series.find_all("div", class_="movie-item short-item")
        for item in series:
            series_name = item.find("a", class_="movie-title").get_text(strip=True)
            series_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")

            season = item.find("div", class_="full-season").get_text(strip=True)
            quality = item.find("div", class_="full-quality").get_text(strip=True)

            series_description = item.find("span", class_="desc-about-text").get_text(strip=True)

            return series_name, series_img, season, quality, series_description



def parse_seriees_other_html(jannre, page):
    if jannre == 'Реальні події':
        url = "https://uakino.club/colections/serialy-na-osnovi-realnuh-podij/"
    elif jannre == 'Топ міні-серіали':
        url = "https://uakino.club/colections/best-mini-series/page/"
    elif jannre == 'За коміксами Marvel':
        url = "https://uakino.club/colections/serialy-po-komiksah-marvel/"
    elif jannre == 'Netional Geographic':
        url = "https://uakino.club/colections/national-geographic/page/"
    elif jannre == 'BBC':
        url = "https://uakino.club/colections/serialy-bbc/page/"
    elif jannre == 'Студії - Netflix':
        url = "https://uakino.club/colections/serialy-netflix/page/"
    elif jannre == 'Студії - HBO':
        url = "https://uakino.club/colections/serialy-hbo/page/"
    elif jannre == 'Студії - THE CW':
        url = "https://uakino.club/colections/serialy-the-cw/page/"
    elif jannre == 'Фантастичні':
        url = "https://uakino.club/seriesss/fantastic_series/page/"


    new_url = url + str(page)


    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}
    
    response = requests.get(new_url, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", id="dle-content")
    for series in section:
        series = series.find_all("div", class_="movie-item short-item")
        for item in series:
            series_name = item.find("a", class_="movie-title").get_text(strip=True)
            series_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                
            season = item.find("div", class_="full-season").get_text(strip=True)

            quality = item.find("div", class_="full-quality").get_text(strip=True)


            series_description = item.find("span", class_="desc-about-text").get_text(strip=True)

            return series_name, series_img, season, quality, series_description