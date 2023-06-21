import requests
import win32com.client as win32
from bs4 import BeautifulSoup

URL = 'https://www.kabum.com.br/produto/95566/mouse-gamer-hyperx-pulsefire-surge-rgb-16000-dpi-4p5q1aa'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 OPR/96.0.0.0"}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

title = soup.find('h1', class_ = "sc-fb499f01-5 cMCMNo").get_text()

price = soup.find('h4', class_ = "sc-d6a30908-1 hOGpJJ finalPrice").get_text()

nun_price = price[3:8]
nun_price = float(nun_price.replace('.','').replace(',','.'))

print('Valor atual:',nun_price)
print('Nome do produto:', title)


if nun_price < 200:
    outlook = win32.Dispatch('outlook.application')
    email = outlook.CreateItem(0)
    email.To = 'screppizinho@gmail.com'
    email.Subject = 'Seu produto ta quentinho! Vem pegar'
    email.Body = f'CORREEEE!!!!! Chegou o seu momento. :D \nO produto {title[0:20]} ta mais barato!! \n{URL}'
    email.Send()
