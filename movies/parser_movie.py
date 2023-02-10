import telebot

import requests
from bs4 import BeautifulSoup

import random
import fake_useragent


import configure

bot = telebot.TeleBot(configure.config['token'])

@bot.message_handler(content_types=["text"])
def genre_movie(message):
    if message.chat.type == 'private':
        for i in range(5):
            try:
                if message.text == 'Фільми - Екшн (бойовики)':
                    page = random.randint(1, 60)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Екшн (бойовики)', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Драми':
                    page = random.randint(1, 96)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Драми', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Історичні':
                    page = random.randint(1, 10)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Історичні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Комедії':
                    page = random.randint(1, 73)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Комедії', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Військові':
                    page = random.randint(1, 9)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Військові', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Спортивні':
                    page = random.randint(1, 6)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Спортивні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Документальні':
                    page = random.randint(1, 6)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Документальні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Трилери':
                    page = random.randint(1, 70)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Трилери', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)



                if message.text == 'Фільми - Мелодрами':
                    page = random.randint(1, 19)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Мелодрами', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Сімейні':
                    page = random.randint(1, 20)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Сімейні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Фантастичні':
                    page = random.randint(1, 28)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Фантастичні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Вестерни':
                    page = random.randint(1, 5)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Вестерни', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

    
                if message.text == 'Фільми - Кримінальні':
                    page = random.randint(1, 42)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Кримінальні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Фентезійні':
                    page = random.randint(1, 23)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Фентезійні', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Детективи':
                    page = random.randint(1, 25)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Детективи', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Фільми - Оригінал':
                    page = random.randint(1, 37)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Фільми - Оригінал', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'подорож в часі':
                    page = random.randint(1, 5)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('подорож в часі', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'про виживання':
                    page = random.randint(1, 7)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('про виживання', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'про мандри':
                    page = random.randint(1, 4)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('про мандри', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'посапокаліпсіс':
                    page = random.randint(1, 5)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('посапокаліпсіс', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'жахи з оскаром':
                    # page = random.randoin(???)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('жахи з оскаром', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'буде страшно':
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('буде страшно', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)



                if message.text == 'класичні монстри':                
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('класичні монстри', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Стівен Кінг':
                    page = random.randint(1, 2)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('Стівен Кінг', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'про любов':
                    page = random.randint(1, 4)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('про любов', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'істроії кохання':
                    page = random.randint(1, 1239)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('істроії кохання', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

    
                if message.text == 'романтичні комедії':
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('романтичні комедії', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

    
                if message.text == 'Marvel':
                    page = random.randint(1, 4)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('Marvel', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

    
                if message.text == 'DC Comics':
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('DC Comics', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'По манзі та аніме':
                    page = random.randint(1, 1239)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('По манзі та аніме', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Warner Bros':
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('Warner Bros', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Netflix':
                    page = random.randint(1, 11)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('Netflix', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Legendary Pictures':
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('Legendary Pictures', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)



                if message.text == 'SONY':
                    page = random.randint(1, 8)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('SONY', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'на основі реальних подій':
                    page = random.randint(1, 8)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('на основі реальних подій', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

                            
                if message.text == "з не очікованю розв'язкою":
                    page = random.randint(1, 3)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html("з не очікованю розв'язкою", page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == "психологічні фільми":
                    page = random.randint(1, 5)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre_other_html('психологічні фільми', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)


                if message.text == 'Всі фільми':
                    page = random.randint(1, 204)
                    movie_name, movie_img, quality, movie_description = parse_movies_by_janre('Всі фільми', page)
                    bot.send_photo(message.chat.id, movie_img, caption="Назва: " + movie_name + "\nЯкість: " + quality + "\n" + movie_description)

            except telebot.apihelper.ApiException:
                bot.send_message(message.chat.id, "Вибач, немає :(\n" + "Можеш спробувати ще раз натиснути😀")
                            

def parse_movies_by_janre(janre, page):
    # FIXME треба поладити під-жанри, наприкалад, там де відрізняється HTML


    if janre == 'Фільми - Екшн (бойовики)':
        url = "https://uakino.club/filmy/genre-action/page/"
    elif janre == 'Фільми - Драми':
        url = "https://uakino.club/filmy/genre_drama/page/"
    elif janre == 'Фільми - Історичні':
        url = "https://uakino.club/filmy/genre_historic/page/"
    elif janre == 'Фільми - Комедії':
        url = "https://uakino.club/filmy/genre_comedy/page/"
    elif janre == 'Фільми - Військові':
        url = "https://uakino.club/filmy/militaries/page/"
    elif janre == 'Фільми - Спортивні':
        url = "https://uakino.club/filmy/genre_sport/page/"
    elif janre == 'Фільми - Документальні':
        url = "https://uakino.club/filmy/documentaries/page/"
    elif janre == 'Фільми - Трилери':
        url = "https://uakino.club/filmy/genre_thriller/page/"
    elif janre == 'Фільми - Мелодрами':
        url = "https://uakino.club/filmy/genre_melodrama/page/"
    elif janre == 'Фільми - Сімейні':
        url = "https://uakino.club/filmy/family/page/"
    elif janre == 'Фільми - Фантастичні':
        url = "https://uakino.club/filmy/genre_science_fictions/page/"
    elif janre == 'Фільми - Вестерни':
        url = "https://uakino.club/filmy/western/page/"
    elif janre == 'Фільми - Кримінальні':
        url = "https://uakino.club/filmy/genre_crime/page/"
    elif janre == 'Фільми - Фентезійні':
        url = "https://uakino.club/filmy/genre_fantastic/page/"
    elif janre == 'Фільми - Детективи':
        url = "https://uakino.club/filmy/genre_detective/page/"
    elif janre == 'Фільми - Оригінал':
        url = "https://uakino.club/filmy/subtitles/page/"
    elif janre == 'про мандри':
        url = "https://uakino.club/colections/flmi-pro-podorozh/page/"
    elif janre == 'посапокаліпсіс':
        url = "https://uakino.club/colections/filmy-pro-postapocalipsys/page/"
    elif janre == 'жахи з оскаром':
        url = "https://uakino.club/colections/oskar-jahiv/"
    elif janre == 'буде страшно':
        url = "https://uakino.club/colections/bude-strashno/page/"
    elif janre == 'класичні монстри':
        url = "https://uakino.club/colections/klasychni-kinomonstry/page/"
    elif janre == 'Стівен Кінг':
        url = "https://uakino.club/colections/stiven-king/page/"
    elif janre == 'про любов':
        url = "https://uakino.club/colections/filmi-pro-lybov/page/"
    elif janre == 'істроії кохання':
        url = "https://uakino.club/colections/enom_love/page/4"
    elif janre == 'романтичні комедії':
        url = "https://uakino.club/colections/romantychni-komedii/page/"
    elif janre == 'Marvel':
        url = "https://uakino.club/colections/marvel-comics/page/"
    elif janre == 'DC Comics':
        url = "https://uakino.club/colections/dc/page/"
    elif janre == 'По манзі та аніме':
        url = "https://uakino.club/colections/filmy-manga-anime/"
    elif janre == 'Warner Bros':
        url = "https://uakino.club/colections/warner-bros-naikraschi-filmy/page/"
    elif janre == 'Netflix':
        url = "https://uakino.club/colections/netflix/page/"
    elif janre == 'Legendary Pictures':
        url = "https://uakino.club/colections/legendary-pictures/page/"
    elif janre == 'SONY':
        url = "https://uakino.club/colections/sony-filmy/page/"
    elif janre == 'на основі реальних подій':
        url = "https://uakino.club/colections/realni-podiji/page/"
    elif janre == "з не очікованю розв'язкою":
        url = "https://uakino.club/colections/neperedbachyvanuj-final/page/"
    elif janre == 'психологічні фільми':
        url = "https://uakino.club/colections/psykholohichni_filmy/page/"
    elif janre == 'Всі фільми':
        url = "https://uakino.club/filmy/page/"
 
    
    url_new = url + str(page)

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    response = requests.get(url_new, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", class_="coloredgray")
    for movie in section:
        movie = movie.find_all("div", class_="movie-item short-item")
        for item in movie:
            movie_name = item.find("a", class_="movie-title").get_text(strip=True)
            movie_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                
            quality = item.find("div", class_="full-quality").get_text(strip=True)

            movie_description = item.find("span", class_="desc-about-text").get_text(strip=True)

            return movie_name, movie_img, quality, movie_description




def parse_movies_by_janre_other_html(janre, page):
    # FIXME треба поладити під-жанри, наприкалад, там де відрізняється HTML

    if janre == 'подорож в часі':
        url = "https://uakino.club/colections/filmy-pro-podoroj-v-chasi/page/"
    elif janre == 'про виживання':
        url = "https://uakino.club/filmy/genre_science_fictions/page/"
    elif janre == 'про мандри':
        url = "https://uakino.club/colections/flmi-pro-podorozh/page/"
    elif janre == 'посапокаліпсіс':
        url = "https://uakino.club/colections/filmy-pro-postapocalipsys/page/"
    elif janre == 'жахи з оскаром':
        url = "https://uakino.club/colections/oskar-jahiv/"
    elif janre == 'буде страшно':
        url = "https://uakino.club/colections/bude-strashno/page/"
    elif janre == 'класичні монстри':
        url = "https://uakino.club/colections/klasychni-kinomonstry/page/"
    elif janre == 'Стівен Кінг':
        url = "https://uakino.club/colections/stiven-king/page/"
    elif janre == 'про любов':
        url = "https://uakino.club/colections/filmi-pro-lybov/page/"
    elif janre == 'істроії кохання':
        url = "https://uakino.club/colections/enom_love/page/4"
    elif janre == 'романтичні комедії':
        url = "https://uakino.club/colections/romantychni-komedii/page/"
    elif janre == 'Marvel':
        url = "https://uakino.club/colections/marvel-comics/page/"
    elif janre == 'DC Comics':
        url = "https://uakino.club/colections/dc/page/"
    elif janre == 'По манзі та аніме':
        url = "https://uakino.club/colections/filmy-manga-anime/"
    elif janre == 'Warner Bros':
        url = "https://uakino.club/colections/warner-bros-naikraschi-filmy/page/"
    elif janre == 'Netflix':
        url = "https://uakino.club/colections/netflix/page/"
    elif janre == 'Legendary Pictures':
        url = "https://uakino.club/colections/legendary-pictures/page/"
    elif janre == 'SONY':
        url = "https://uakino.club/colections/sony-filmy/page/"
    elif janre == 'на основі реальних подій':
        url = "https://uakino.club/colections/realni-podiji/page/"
    elif janre == "з не очікованю розв'язкою":
        url = "https://uakino.club/colections/neperedbachyvanuj-final/page/"
    elif janre == 'психологічні фільми':
        url = "https://uakino.club/colections/psykholohichni_filmy/page/"


    # FIXME: "жахи з оскаром"
    
    url_new = url + str(page)

    user = fake_useragent.UserAgent().random
    header = {'user-agent': user}

    response = requests.get(url_new, headers=header)

    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find_all("div", id="dle-content")
    for movie in section:
        movie = movie.find_all("div", class_="movie-item short-item")
        for item in movie:
            movie_name = item.find("a", class_="movie-title").get_text(strip=True)
            movie_img = item.find("i", class_="fa fa-play-circle go-watch").get("data-link")
                
            quality = item.find("div", class_="full-quality").get_text(strip=True)

            movie_description = item.find("span", class_="desc-about-text").get_text(strip=True)

            return movie_name, movie_img, quality, movie_description