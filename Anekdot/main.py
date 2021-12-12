import requests
from bs4 import BeautifulSoup
import  RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    inputValue = GPIO.input(18)
    if (inputValue == False):
        website = 'https://www.anekdot.ru/random/anekdot/'
        result = requests.get(website)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')
        box = soup.find('div', class_='content content-min')
        transcript = box.find('div', class_='text')
        transcript = transcript.get_text('\n'*2, strip=True)
        print(transcript, '\n' * 4)
    time.sleep(0.3)
