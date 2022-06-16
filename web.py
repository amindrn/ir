from turtle import title
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
from tqdm import tqdm


def scrapAll():
    page = 2
    scraptedData = []
    while True:

        page_url = f'https://www.tabnak.ir/fa/archive?service_id=-1&sec_id=-1&cat_id=-1&rpp=20&from_date=1384/01/01&to_date=1401/03/24&p={page}'
        html = requests.get(page_url).text
        soap = BeautifulSoup(html, 'lxml')
        links = soap.findAll("div", {"class": "linear_news"})
        # links = soap.find_all('h3')
        page += 1
        for link in tqdm(links):
            news_url = 'https://www.tabnak.ir'+link.a['href']
            try:
                article = Article(news_url)
                article.download()
                article.parse()
            except:
                print('fuck')
            scraptedData.append({
                'url': news_url,
                'text': article.text,
                'title': article.title
            })
        if page == 150:
            break
        # print(links[2])

        # print(len(links))
    df = pd.DataFrame(scraptedData)
    df.to_csv(f'tabnak150Page.csv')
    # print(scraptedData)


scrapAll()
