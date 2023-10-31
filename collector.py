from pathlib import Path
import requests
from datetime import date
import bs4

def get_html_data():
    

    today = str(date.today())

    #cache: only request at most once per day 
    print(today)  
    fpath = Path(f"{today}.html")

    UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    url = "https://montrealgazette.com/category/news/"
    headers = {'User-Agent': UserAgent}


    if not fpath.exists():

        result = requests.get(url, headers=headers)
        #print(result.content.decode())
        with open(fpath, "w") as f:
            f.write(result.text)

    with open(fpath) as f:
        return f.read()


def main():
    
    html_data = get_html_data()
    soup = bs4.BeautifulSoup(html_data, "html.parser")

    trend_list_widget= soup.find("div", class_="col-xs-12 top-trending" )
    articles = trend_list_widget.find_all("div", class_="article-card__details")
    

    for article in articles:
        title = article.find("span").text.strip()
        link = article.find("a")['href']


        print(link)

if __name__ == "__main__":
    main()

    


    