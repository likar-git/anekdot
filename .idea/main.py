import requests
from bs4 import BeautifulSoup
website = 'https://www.anekdot.ru/random/anekdot/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('div', class_='content content-min')
transcript = box.find('div', class_='text')
transcript = transcript.get_text('\n', strip=True)
print(transcript)