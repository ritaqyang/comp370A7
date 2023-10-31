#this file scrapes publication date, author and blurb using an url 
from pathlib import Path
import requests
from datetime import date
import bs4

def get_html_single_article(num,url):
    

    fpath = Path(f"{num}.html")
    UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    headers = {'User-Agent': UserAgent}

    if not fpath.exists():

        result = requests.get(url, headers=headers)
        #print(result.content.decode())
        with open(fpath, "w") as f:
            f.write(result.text)

    with open(fpath) as f:
        return f.read()

