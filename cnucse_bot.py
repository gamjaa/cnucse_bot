import requests
from bs4 import BeautifulSoup
import re
import telegram
import os

f = open(os.path.dirname(os.path.realpath(__file__))+'/article_num.txt', 'r')
last = int(f.readline())
current = 0
f.close()

bot = telegram.Bot(os.environ['TELEGRAM_API_TOKEN'])

# 학사공지
req = requests.get('http://computer.cnu.ac.kr/index.php?mid=notice')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
board = soup.select('#bd_187_0 > div.bd_lst_wrp > table > tbody')
notice = board[0].find_all('a')

for i in notice:
    if i.get('class') is not None:
        if i.get('class')[0] == "replyNum":
            continue

    num = int(re.sub("[^0-9]+", "", i.get('href')))
    if last < num:
        title = re.sub("\s\s+", " ", i.text)
        url = i.get('href')
        bot.sendMessage(chat_id='@cnucse', text='[학사] ' + title + '\n' + url)
        if current < num:
            current = num

# 일반소식
req = requests.get('http://computer.cnu.ac.kr/index.php?mid=gnotice')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
board = soup.select('#bd_189_0 > div.bd_lst_wrp > table > tbody')
notice = board[0].find_all('a')

for i in notice:
    if i.get('class') is not None:
        if i.get('class')[0] == "replyNum":
            continue

    num = int(re.sub("[^0-9]+", "", i.get('href')))
    if last < num:
        title = re.sub("\s\s+", " ", i.text)
        url = i.get('href')
        bot.sendMessage(chat_id='@cnucse', text='[일반] ' + title + '\n' + url)
        if current < num:
            current = num

# 사업단소식
req = requests.get('http://computer.cnu.ac.kr/index.php?mid=saccord')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
board = soup.select('#bd_191_0 > div.bd_lst_wrp > table > tbody')
notice = board[0].find_all('a')

for i in notice:
    if i.get('class') is not None:
        if i.get('class')[0] == "replyNum":
            continue

    num = int(re.sub("[^0-9]+", "", i.get('href')))
    if last < num:
        title = re.sub("\s\s+", " ", i.text)
        url = i.get('href')
        bot.sendMessage(chat_id='@cnucse', text='[사업단] ' + title + '\n' + url)
        if current < num:
            current = num

# 취업정보
req = requests.get('http://computer.cnu.ac.kr/index.php?mid=job')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
board = soup.select('#bd_193_0 > div.bd_lst_wrp > table > tbody')
notice = board[0].find_all('a')

for i in notice:
    if i.get('class') is not None:
        if i.get('class')[0] == "replyNum":
            continue

    num = int(re.sub("[^0-9]+", "", i.get('href')))
    if last < num:
        title = re.sub("\s\s+", " ", i.text)
        url = i.get('href')
        bot.sendMessage(chat_id='@cnucse', text='[취업] ' + title + '\n' + url)
        if current < num:
            current = num

if last < current:
    f = open(os.path.dirname(os.path.realpath(__file__))+'/article_num.txt', 'w')
    f.write(str(current))
    f.close()
