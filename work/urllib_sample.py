import urllib.request


def get(url: str)-> None:
    with urllib.request.urlopen(url) as r:
        html = r.read()
        print(html)


if __name__=="__main__":
    get("https://churadata.okinawa/")