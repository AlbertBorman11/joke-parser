import requests
import logging
import time
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)

def get_random_joke():
    russian_url = 'https://anekdot.ru/random/anekdot'
    english_url = 'https://icanhazdadjoke.com'
    headers = {"Accept": "application/json"}

    # Get a random Russian joke
    russian_response = requests.get(russian_url, headers=headers)
    russian_web = russian_response.text
    russian_soup = BeautifulSoup(russian_web, "lxml")
    russian_joke_element = russian_soup.select_one('.topicbox .text')
    if russian_joke_element:
        russian_joke = russian_joke_element.get_text().replace("<br/>", "\n")
        print("Russian Joke:", russian_joke)

    # Get a random English joke
    english_response = requests.get(english_url, headers=headers)
    english_data = english_response.json()
    if 'joke' in english_data:
        english_joke = english_data['joke']
        print("English Joke:", english_joke)

while True:
    get_random_joke()
    time.sleep(20)
