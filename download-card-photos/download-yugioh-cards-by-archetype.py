import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

"""
https://yugioh.fandom.com/wiki/Ally_of_Justice
https://yugioh.fandom.com/wiki/Alien
https://yugioh.fandom.com/wiki/Allure_Queen
https://yugioh.fandom.com/wiki/Black_Luster_Soldier_(archetype)
https://yugioh.fandom.com/wiki/Blackwing
https://yugioh.fandom.com/wiki/Gishki
https://yugioh.fandom.com/wiki/Gusto
"""

# Archetype URL like 'https://yugioh.fandom.com/wiki/Lightsworn'
base_arquetype_url = 'https://yugioh.fandom.com/wiki/Black_Luster_Soldier_(archetype)'
base_next_page = 'https://yugioh.fandom.com'

# Make HTTP Request and convert with soap
response = requests.get(base_arquetype_url)
if(response.status_code != 200):
  print(url, 'Erro Code')
  quit()
soup_page = BeautifulSoup(response.text, 'html5lib')

# get all <ul class="smw-format ul-format">
font_links = soup_page.find_all('ul', attrs = {'class' : 'smw-format ul-format'})
# get href in <a href="/wiki/Glorious_Illusion"> and make next page url
nexts_links = []
for line in font_links:
  nexts = line.find_all('a')
  for j in nexts:
    nexts_links.append(base_next_page + j['href'])

# To each url that has the image
for url in nexts_links:
  print(url)
  response = requests.get(url)
  if(response.status_code != 200):
    print(url, 'Erro Code')
    quit()
  card_page = BeautifulSoup(response.text, 'html5lib')
  # get part where is the iamge link <td class="cardtable-cardimage" rowspan="50">
  td_part = card_page.find('td', attrs = {'class' : 'cardtable-cardimage'})
  url_image = td_part.a['href']
  # get name of image in <img alt="EhrenLightswornMonk-SR02-EN-C-1E.png"
  image_name = td_part.find('img')['alt']
  # Dowload Image
  r = requests.get(url_image)
  with open(image_name, "wb") as f:
    f.write(r.content)


