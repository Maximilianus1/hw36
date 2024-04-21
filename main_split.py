import requests
def getInfo(url):
    content=requests.get(url)

    try:
        a=content.text
        b=a.split('"')
        for i in b:
            if "днём " in i:
                print(i)
    except:
        print('nothing')
url = "https://yandex.kz/pogoda/astana"
getInfo(url)
