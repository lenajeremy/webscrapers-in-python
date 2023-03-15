import requests
from bs4 import BeautifulSoup

def get_crypto_prices():
    url = 'https://coinmarketcap.com'
    response_text = requests.get(url).text
    
    soup = BeautifulSoup(response_text, 'html.parser')
    
    # get all the table rows
    table_rows = soup.findAll('tr')
    
    # iterate through all the table rows and get the required data
    for table_row in table_rows:
        crypto_name = table_row.find('p', class_ = 'sc-e225a64a-0 ePTNty')
        shortened_crypto_name = table_row.find('p', class_ = 'sc-e225a64a-0 dfeAJi coin-item-symbol')
        crypto_img_url = table_row.find('img')
        crypto_price = table_row.find('div', class_ = 'sc-8bda0120-0 dskdZn')
        
        if crypto_name is None or shortened_crypto_name is None or crypto_price is None:
            continue
        else:
            crypto_name = crypto_name.text
            shortened_crypto_name = shortened_crypto_name.text
            crypto_img_url = crypto_img_url.attrs.get('src')
            crypto_price = crypto_price.text
        
            print(f"Name: {crypto_name} ({shortened_crypto_name}) \nPrice: {crypto_price} \nImage URL: {crypto_img_url}\n")
    

get_crypto_prices()