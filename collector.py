from pathlib import Path
import requests
from datetime import date


def get_html_data():
    

    today = str(date.today())
    print(today)  
    fpath = Path(f"{today}.html")

    UserAgent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    url = "https://montrealgazette.com/category/news/"
    headers = {'User-Agent': UserAgent}


    if not fpath.exists():

        result = requests.get(url, headers=headers)
        print(result.content.decode())
        with open(fpath, "w") as f:
            f.write(result.text)

    with open(fpath) as f:
        return f.read()


def main():
    
    html_data = get_html_data()
    print(html_data)

if __name__ == "__main__":
    main()

    


    