import requests
from bs4 import BeautifulSoup
import subprocess
lpr =  subprocess.Popen("/dev/usb/lp0", stdin=subprocess.PIPE)
website = 'https://www.anekdot.ru/random/anekdot/'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('div', class_='content content-min')
transcript = box.find('div', class_='text')
transcript = transcript.get_text('\n'*2, strip=True)
print(transcript, '\n' * 4, 't')
lpr.stdin.write(transcript)