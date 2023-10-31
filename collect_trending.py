from pathlib import Path
import requests
from datetime import date
import bs4
import single_article_scraper
import json

def get_html_main(): #get html from the main page 
    

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



def get_trending_article_urls():
    html_data = get_html_main()
    soup = bs4.BeautifulSoup(html_data, "html.parser")

    trend_list_widget= soup.find("div", class_="col-xs-12 top-trending" )
    articles = trend_list_widget.find_all("div", class_="article-card__details")
    
    links = []
    for article in articles:
        title = article.find("span").text.strip()
        link = article.find("a")['href']


        print(link)
        links.append(link)
    return links

def main():

    data = {}
    list_of_urls = get_trending_article_urls()
    i = 0 #count number of articles to input into the single article scraper 
    # url = list_of_urls[1]
    # test = single_article_scraper.get_trending_article_info(1,url)

    for url in list_of_urls:
        article_item = single_article_scraper.get_trending_article_info(i,url)
        data.append(article_item)
        i +=1
    
    with open("trending.json", "w") as json_file:
        json.dump(data, json_file, indent=4)



if __name__ == "__main__":
    main()

    


    