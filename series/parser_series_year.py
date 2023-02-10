import telebot

import requests
from bs4 import BeautifulSoup

import random
import fake_useragent

import configure

bot = telebot.TeleBot(configure.config['token'])

@bot.message_handler(content_types=["text"])
def year_series(message):
    if message.chat.type == 'private':
        for i in range(5):
            try:
                if message.text == '2022':
                    page = random.randint(1, 13)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2022', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                
                if message.text == '2021':
                    page = random.randint(1, 13)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2021', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)

                        
                if message.text == '2020':
                    page = random.randint(1, 9)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2020', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == '2019':
                    page = random.randint(1, 9)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2019', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == '2018':
                    page = random.randint(1, 10)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2018', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == '2017':
                    page = random.randint(1, 10)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2017', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == '2016 - 2022':
                    page = random.randint(1, 69)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2016 - 2022', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == '2010 - 2016':
                    page = random.randint(1, 5)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2010 - 2016', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == '2000 - 2010':
                    page = random.randint(1, 38)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('2000 - 2010', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == '1990 - 2000':
                    page = random.randint(1, 12)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('1990 - 2000', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)


                if message.text == '1980 - 1990':
                    page = random.randint(1, 4)
                    series_name, series_img, quality, series_description, season = parse_movies_by_year('1980 - 1990', page)
                    bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nКількість: " + season + "\nЯкість: " + quality + "\nОпис: " + series_description)



                if message.text == 'До 80-x':
                    url = "https://uakino.club/seriesss/f/c.year=1921,1980/sort=date;desc/"

                    response = requests.get(url, headers={'User-Agent': "Safari/537.36"})

                    soup = BeautifulSoup(response.text, "html.parser")
                    section = soup.find_all("div", id="dle-content")
                    for series in section:
                        series = series.find_all("div", class_="movie-item short-item")
                        for item in series:
                            series_name = item.find("a", class_="movie-title").get_text(strip=True)
                            series_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                                
                            # season = item.find("div", class_="full-season").get_text(strip=True)
                            

                            quality = item.find("div", class_="full-quality").get_text(strip=True)

                            series_description = item.find("span", class_="desc-about-text").get_text(strip=True)

                            bot.send_photo(message.chat.id, series_img, caption="Назва: " + series_name + "\nЯкість: " + quality + "\nОпис: " + series_description)
            except telebot.apihelper.ApiException:
                bot.send_message(message.chat.id, "Вибач, немає :(\n" + "Можеш спробувати ще раз натиснути😀")


def parse_movies_by_year(year, page):
    if year == '2022':
        url = "https://uakino.club/seriesss/f/c.year=2022,2022/sort=date;desc/page/"
    elif year == '2021':
        url = "https://uakino.club/seriesss/f/c.year=2021,2021/sort=date;desc/page/"
    elif year == '2020':
        url = "https://uakino.club/seriesss/f/c.year=2020,2020/sort=date;desc/page/"
    elif year == '2019':
        url = "https://uakino.club/seriesss/f/c.year=2019,2019/sort=date;desc/page/"
    elif year == '2018':
        url = "https://uakino.club/seriesss/f/c.year=2018,2018/sort=date;desc/page/"
    elif year == '2017':
        url = "https://uakino.club/seriesss/f/c.year=2017,2017/sort=date;desc/page/"
    elif year == '2016 - 2022':
        url = "https://uakino.club/seriesss/f/c.year=2016,2022/sort=date;desc/page/"
    elif year == '2010 - 2016':
        url = "https://uakino.club/seriesss/f/c.year=2010,2016/sort=date;desc/page/"
    elif year == '2000 - 2010':
        url = "https://uakino.club/seriesss/f/c.year=2000,2010/sort=date;desc/page/"
    elif year == '1990 - 2000':
        url = "https://uakino.club/seriesss/f/c.year=1990,2000/sort=date;desc/page/"
    elif year == '1980 - 1990':
        url = "https://uakino.club/seriesss/f/c.year=1980,1990/sort=date;desc/page/"


    # FIXME: fix 80-x

    
    url_new = url + str(page)

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    response = requests.get(url_new, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", class_="content-box clearfix")
    for movie in section:
        movie = movie.find_all("div", class_="movie-item short-item")
        for item in movie:
            series_name = item.find("a", class_="movie-title").get_text(strip=True)
            series_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                
            season = item.find("div", class_="full-season").get_text(strip=True)

            quality = item.find("div", class_="full-quality").get_text(strip=True)

            series_description = item.find("span", class_="desc-about-text").get_text(strip=True)

            return series_name, series_img, quality, series_description, season