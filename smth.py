from bs4 import BeautifulSoup
import requests
import pandas as pd
import random

url="https://www.xataka.com/tag/cambio-climatico"

response = requests.get(url)
bs = BeautifulSoup(response.text,"lxml")
temp = bs.find_all("article", "recent-abstract abstract-article")

dict_news = {"titulos_noticias": [], "enlaces": [], "fecha": [], "comentarios": []}

for i in temp:
  dict_news["enlaces"].append(i.h2.a.get("href"))
  dict_news["titulos_noticias"].append(i.h2.a.text)
  dict_news["comentarios"].append(i.span.text)
  dict_news["fecha"].append(i.time.text)

df_news = pd.DataFrame(dict_news, columns=["titulos_noticias", "enlaces", "comentarios", "fecha"])





def extract_article_text():
    new = random.choice(df_news["enlaces"].tolist())
    response = requests.get(new)
    soup = BeautifulSoup(response.content, 'lxml')

    article_body = soup.find('div', {'class': 'article-content'})  # Adjust if necessary
    if not article_body:
        return None

    paragraphs = article_body.find_all('p')
    return '\n'.join([para.get_text() for para in paragraphs])

def transfer():
  article_text = extract_article_text()
  return article_text