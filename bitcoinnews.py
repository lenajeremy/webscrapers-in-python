import requests
from bs4 import BeautifulSoup


def get_news():
    url = 'https://coinmarketcap.com/'
    
    response = requests.get(url)
    response_text = response.text
    
    soup = BeautifulSoup(response_text, 'html.parser')
    
    file = open('articles.txt', 'w')
    
    file.write(str(soup))
    
    file.close()
    
    
    
get_news()