#scrapes publication date, author and blurb
#takes an url as input 
from pathlib import Path
import requests
from datetime import date
import bs4

def get_html_single_article(num,url):
    

    fpath = Path(f"{num}.html")
    UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    headers = {'User-Agent': UserAgent}

    if not fpath.exists():

        #add http:// to the urls
        link = f'http:/{url}'
        result = requests.get(link, headers=headers)
        #print(result.content.decode())
        with open(fpath, "w") as f:
            f.write(result.text)

    with open(fpath) as f:
        return f.read()

def get_trending_article_info(num,url):
    html_data = get_html_single_article(num,url) #cache-ing
    soup = bs4.BeautifulSoup(html_data, "html.parser")

    info_box= soup.find("div", class_="article-header__detail__texts" )
    title = info_box.find("h1",id="articleTitle").text.strip()
    blurb = info_box.find("p",class_="article-subtitle")
    author = info_box.find("span",class_="published-by__author").text.strip()
    pub_date = info_box.find("span", class_="published-date__since").text.strip()

    print(title, blurb,author,pub_date)

    new_item = {
        "title": {title},
        "publication_date": {pub_date},
        "author": {author},
        "blurb": {blurb}
    }

    return new_item


   