import requests
from bs4 import BeautifulSoup


def get_news():
    url = 'https://news.bitcoin.com'
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    
    response = requests.get(url, headers=headers)
    
    response_text = response.text
    
    soup = BeautifulSoup(response_text, 'html.parser')
    
    all_articles = soup.findAll('div', class_ = 'story')
    
    for article in all_articles:
        news_title_element = article.select_one('.story__title')
        news_url = news_title_element.parent.attrs.get('href')
        news_title = news_title_element.text.strip()
        print(f"HEADLINE: {news_title} \nURL: {news_url}\n")
        
    

get_news()