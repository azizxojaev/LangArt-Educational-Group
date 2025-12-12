import math
from environs import Env
import requests


env = Env()
env.read_env()


def custom_round(x):
    if x > int(x) + 0.5:
        return math.ceil(x)
    else:
        return math.floor(x)

def calculate_stars(course):
    total_stars = course.how_much_5stars + course.how_much_4stars + course.how_much_3stars + course.how_much_2stars + course.how_much_1stars
    stars_percent = {
        5: round(course.how_much_5stars / total_stars * 100),
        4: round(course.how_much_4stars / total_stars * 100),
        3: round(course.how_much_3stars / total_stars * 100),
        2: round(course.how_much_2stars / total_stars * 100),
        1: round(course.how_much_1stars / total_stars * 100)
    }
    stars_rating = round(((course.how_much_5stars*5) + (course.how_much_4stars*4) + (course.how_much_3stars*3) + (course.how_much_2stars*2) + (course.how_much_1stars*1)) / total_stars, 1)
    full_stars = int(custom_round(stars_rating))
    if stars_rating > full_stars:
        half_star = 1 if (stars_rating - full_stars) <= 0.5 else 0
    else:
        half_star = 1 if (full_stars - stars_rating) >= 0.5 else 0

    empty_stars = 5 - full_stars - half_star

    return stars_percent, stars_rating, total_stars, full_stars, half_star, empty_stars


def send_message(text):
    api_token = env.str('API_TOKEN')
    chat_id = env.str('CHAT_ID')
    api_url = f'https://api.telegram.org/bot{api_token}/sendMessage'

    try:
        response = requests.post(api_url, json={'chat_id': chat_id, 'text': text})
        response.raise_for_status()
    except Exception as e:
        print(f'Произошла ошибка: {e}')