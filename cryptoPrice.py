from bs4 import BeautifulSoup
import requests
import time


def getCryptoPrice(coin):
    #Get URL
    url="https://www.google.com/search?q="+coin+"+price"
    HTML = requests.get(url)
    soup = BeautifulSoup(HTML.text,'html.parser')
    #print(soup.prettify())
    text = soup.find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return text
def main():
    lastPrice=-1
    while True:
        crypto = 'bitcoin'
        price = getCryptoPrice(crypto)
        if price != lastPrice:
            print(crypto+' price : '+price)
            lastPrice=price
        time.sleep(3)
        
main()

#print(getCryptoPrice('bitcoin'))

