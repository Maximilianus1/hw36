import requests
from bs4 import BeautifulSoup
def getInfo(url):
    content=requests.get(url)
    soup = BeautifulSoup(content.text, 'html.parser')
    try:
        all_ul=soup.find_all('a', {'class':"forecast-briefly__day-link"})
        for i in all_ul:
            print(i["aria-label"])
    except:
        print('nothing')
url = "https://yandex.kz/pogoda/astana"
getInfo(url)
