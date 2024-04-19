import requests
from bs4 import BeautifulSoup


def get(url:str):
    r = requests.get(url)
    html = BeautifulSoup(r.content, "html.parser")
    print(html)
    breakpoint()


if __name__=="__main__":
    get("https://churadata.okinawa/")